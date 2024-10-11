---
title: QuestionAnsweringTrainer 설명
date: 2024-10-01
categories: machine-learning
---

```python
# coding=utf-8
# Copyright 2020 The HuggingFace Team All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
A subclass of `Trainer` specific to Question-Answering tasks
"""

import math
import time

from transformers import Trainer, is_torch_xla_available
from transformers.trainer_utils import PredictionOutput, speed_metrics


if is_torch_xla_available():
    import torch_xla.core.xla_model as xm
    import torch_xla.debug.metrics as met


class QuestionAnsweringTrainer(Trainer):
    def __init__(self, *args, eval_examples=None, post_process_function=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.eval_examples = eval_examples
        self.post_process_function = post_process_function

    def evaluate(self, eval_dataset=None, eval_examples=None, ignore_keys=None, metric_key_prefix: str = "eval"):
        eval_dataset = self.eval_dataset if eval_dataset is None else eval_dataset
        eval_dataloader = self.get_eval_dataloader(eval_dataset)
        eval_examples = self.eval_examples if eval_examples is None else eval_examples

        # Temporarily disable metric computation, we will do it in the loop here.
        compute_metrics = self.compute_metrics
        self.compute_metrics = None
        eval_loop = self.prediction_loop if self.args.use_legacy_prediction_loop else self.evaluation_loop
        start_time = time.time()
        try:
            output = eval_loop(
                eval_dataloader,
                description="Evaluation",
                # No point gathering the predictions if there are no metrics, otherwise we defer to
                # self.args.prediction_loss_only
                prediction_loss_only=True if compute_metrics is None else None,
                ignore_keys=ignore_keys,
                metric_key_prefix=metric_key_prefix,
            )
        finally:
            self.compute_metrics = compute_metrics
        total_batch_size = self.args.eval_batch_size * self.args.world_size
        if f"{metric_key_prefix}_jit_compilation_time" in output.metrics:
            start_time += output.metrics[f"{metric_key_prefix}_jit_compilation_time"]
        output.metrics.update(
            speed_metrics(
                metric_key_prefix,
                start_time,
                num_samples=output.num_samples,
                num_steps=math.ceil(output.num_samples / total_batch_size),
            )
        )
        if self.post_process_function is not None and self.compute_metrics is not None and self.args.should_save:
            # Only the main node write the results by default
            eval_preds = self.post_process_function(eval_examples, eval_dataset, output.predictions)
            metrics = self.compute_metrics(eval_preds)

            # Prefix all keys with metric_key_prefix + '_'
            for key in list(metrics.keys()):
                if not key.startswith(f"{metric_key_prefix}_"):
                    metrics[f"{metric_key_prefix}_{key}"] = metrics.pop(key)
            metrics.update(output.metrics)
        else:
            metrics = output.metrics

        if self.args.should_log:
            # Only the main node log the results by default
            self.log(metrics)

        if self.args.tpu_metrics_debug or self.args.debug:
            # tpu-comment: Logging debug metrics for PyTorch/XLA (compile, execute times, ops, etc.)
            xm.master_print(met.metrics_report())

        self.control = self.callback_handler.on_evaluate(self.args, self.state, self.control, metrics)
        return metrics

    def predict(self, predict_dataset, predict_examples, ignore_keys=None, metric_key_prefix: str = "test"):
        predict_dataloader = self.get_test_dataloader(predict_dataset)

        # Temporarily disable metric computation, we will do it in the loop here.
        compute_metrics = self.compute_metrics
        self.compute_metrics = None
        eval_loop = self.prediction_loop if self.args.use_legacy_prediction_loop else self.evaluation_loop
        start_time = time.time()
        try:
            output = eval_loop(
                predict_dataloader,
                description="Prediction",
                # No point gathering the predictions if there are no metrics, otherwise we defer to
                # self.args.prediction_loss_only
                prediction_loss_only=True if compute_metrics is None else None,
                ignore_keys=ignore_keys,
                metric_key_prefix=metric_key_prefix,
            )
        finally:
            self.compute_metrics = compute_metrics
        total_batch_size = self.args.eval_batch_size * self.args.world_size
        if f"{metric_key_prefix}_jit_compilation_time" in output.metrics:
            start_time += output.metrics[f"{metric_key_prefix}_jit_compilation_time"]
        output.metrics.update(
            speed_metrics(
                metric_key_prefix,
                start_time,
                num_samples=output.num_samples,
                num_steps=math.ceil(output.num_samples / total_batch_size),
            )
        )

        if self.post_process_function is None or self.compute_metrics is None:
            return output

        predictions = self.post_process_function(predict_examples, predict_dataset, output.predictions, "predict")
        metrics = self.compute_metrics(predictions)

        # Prefix all keys with metric_key_prefix + '_'
        for key in list(metrics.keys()):
            if not key.startswith(f"{metric_key_prefix}_"):
                metrics[f"{metric_key_prefix}_{key}"] = metrics.pop(key)
        metrics.update(output.metrics)
        return PredictionOutput(predictions=predictions.predictions, label_ids=predictions.label_ids, metrics=metrics)
```

1. 시작:

   - 우리는 질문-응답 모델을 훈련하고 평가하기 위해 Huggingface의 Trainer 클래스를 확장한 QuestionAnsweringTrainer 클래스를 만듭니다.
   - 이 클래스는 기본적인 훈련 기능 외에도, 평가와 예측 시에 특별한 후처리 과정을 거칠 수 있도록 설계되었습니다.

2. 초기화:

   - QuestionAnsweringTrainer 객체가 생성될 때, 부모 클래스인 Trainer의 초기화가 먼저 이루어집니다.
   - 추가로 평가에 사용할 예제들과 예측 결과를 후처리할 함수를 저장합니다.

3. 평가 과정:

   - 모델의 성능을 평가하기 위해 evaluate 메서드를 호출합니다.
   - 평가할 데이터셋과 예제들을 준비하고, 데이터로더를 생성합니다.
   - 메트릭 계산을 일시적으로 비활성화하여, 예측 수행 시 손실만 계산하도록 설정합니다.
   - prediction_loop을 통해 모델의 예측을 수행하고, 결과를 얻습니다.
   - 예측 결과를 후처리 함수로 가공한 후, 가공된 결과를 바탕으로 메트릭을 계산하고 로그에 기록합니다.
   - 만약 TPU를 사용 중이라면, TPU 관련 디버깅 정보를 출력합니다.
   - 최종적으로 평가 메트릭을 반환합니다.

4. 예측 과정:

   - 새로운 데이터에 대해 모델의 예측을 수행하기 위해 predict 메서드를 호출합니다.
   - 테스트할 데이터셋과 예제들을 준비하고, 데이터로더를 생성합니다.
   - 메트릭 계산을 일시적으로 비활성화하여, 예측 수행 시 손실만 계산하도록 설정합니다.
   - prediction_loop을 통해 모델의 예측을 수행하고, 결과를 얻습니다.
   - 예측 결과를 후처리 함수로 가공한 후, 최종 예측 결과를 반환합니다.
