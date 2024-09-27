---
title: 에러 수리 기록
date: 2024-09-25
categories: machine_learning
---

## 모델은 업데이트 되고 있지만 모델의 토크나이저는 업데이트 되고 있지 않아서 생기는 문제

```
tokenizing: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9324/9324 [00:02<00:00, 3735.37it/s]
tokenizing: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 550/550 [00:00<00:00, 3722.12it/s]
tokenizing: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 550/550 [00:00<00:00, 3696.16it/s]
tokenizing: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 550/550 [00:00<00:00, 3703.56it/s]
/opt/conda/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:472: FutureWarning: The use_auth_token argument is deprecated and will be removed in v5 of Transformers. Please use
token instead.                                                                                                                                                                                         warnings.warn(
Some weights of ElectraForSequenceClassification were not initialized from the model checkpoint at monologg/koelectra-base-v3-discriminator and are newly initialized: ['classifier.out_proj.bias', 'cl
assifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.weight']                                                                                                                         You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
epoch 0 training:   0%|                                                                                                                                                        | 0/583 [00:00<?, ?it/s]
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [96,0,0] Assertion srcIndex < srcSelectDimSize failed.  /opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [97,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [98,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [99,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [100,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [101,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [102,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [103,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [104,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [105,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [106,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [107,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [108,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [109,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [110,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [111,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [112,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [113,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [114,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [115,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [116,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [117,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [118,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [119,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [120,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [121,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [122,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [123,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [124,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [125,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [126,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [597,0,0], thread: [127,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [0,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [1,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [2,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [3,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [4,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [5,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [6,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [7,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [8,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [9,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [10,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [11,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [12,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [13,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [14,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [15,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [16,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [17,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [18,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [19,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [20,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [21,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [22,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [23,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [24,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [25,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [26,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [27,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [28,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [29,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [30,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [31,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [32,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [33,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [34,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [35,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [36,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [37,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [38,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [39,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [40,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [41,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [42,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [43,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [44,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [45,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [46,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [47,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [48,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [49,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [50,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [51,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [52,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [53,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [54,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [55,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [56,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [57,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [58,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [59,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [60,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [61,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [62,0,0] Assertion srcIndex < srcSelectDimSize failed.
/opt/conda/conda-bld/pytorch_1695392020201/work/aten/src/ATen/native/cuda/Indexing.cu:1292: indexSelectLargeIndex: block: [604,0,0], thread: [63,0,0] Assertion srcIndex < srcSelectDimSize failed.
epoch 0 training:   0%|                                                                                                                                                        | 0/583 [00:00<?, ?it/s]
Error executing job with overrides: []
Traceback (most recent call last):
  File "/data/ephemeral/home/STS/train.py", line 99, in main
    trainer.train()
  File "/data/ephemeral/home/STS/base/base_trainer.py", line 53, in train
    self._train_epoch(epoch)
  File "/data/ephemeral/home/STS/module/trainer.py", line 146, in _train_epoch
    output = self.model(input_ids=input_ids,attention_mask=attention_mask)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1568, in _call_impl
    result = forward_call(*args, **kwargs)
  File "/data/ephemeral/home/STS/module/model.py", line 28, in forward
    outputs = self.plm(
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/transformers/models/electra/modeling_electra.py", line 996, in forward
    discriminator_hidden_states = self.electra(
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/transformers/models/electra/modeling_electra.py", line 900, in forward
    hidden_states = self.embeddings(
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/transformers/models/electra/modeling_electra.py", line 203, in forward
    inputs_embeds = self.word_embeddings(input_ids)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/sparse.py", line 162, in forward
    return F.embedding(
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/functional.py", line 2233, in embedding
    return torch.embedding(weight, input, padding_idx, scale_grad_by_freq, sparse)
RuntimeError: CUDA error: device-side assert triggered
Compile with TORCH_USE_CUDA_DSA to enable device-side assertions.


Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
wandb: 🚀 View run rare-sweep-2 at: https://wandb.ai/freiheit517-boostcamp/sangyeop/runs/bu7s6f5x
wandb: Find logs at: wandb/run-20240925_021415-bu7s6f5x/logs
wandb: Agent Starting Run: q6m2wgj7 with config:
wandb:  plm_name: snunlp/KR-ELECTRA-discriminator
wandb: WARNING Ignored wandb.init() arg project when running a sweep.
Error executing job with overrides: []
Traceback (most recent call last):
  File "/data/ephemeral/home/STS/train.py", line 34, in main
    wandb.init(project=config["wandb"]["project_name"])
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/wandb_init.py", line 1248, in init
    wandb._sentry.reraise(e)
  File "/opt/conda/lib/python3.10/site-packages/wandb/analytics/sentry.py", line 155, in reraise
    raise exc.with_traceback(sys.exc_info()[2])
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/wandb_init.py", line 1234, in init
    return wi.init()
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/wandb_init.py", line 655, in init
    with telemetry.context() as tel:
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/lib/telemetry.py", line 42, in __exit__
    self._run._telemetry_callback(self._obj)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/wandb_run.py", line 806, in _telemetry_callback
    self._telemetry_flush()
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/wandb_run.py", line 819, in _telemetry_flush
    self._backend.interface._publish_telemetry(self._telemetry_obj)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/interface/interface_shared.py", line 101, in _publish_telemetry
    self._publish(rec)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/interface/interface_sock.py", line 51, in _publish
    self._sock_client.send_record_publish(record)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 221, in send_record_publish
    self.send_server_request(server_req)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 155, in send_server_request
    self._send_message(msg)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 152, in _send_message
    self._sendall_with_error_handle(header + data)
  File "/opt/conda/lib/python3.10/site-packages/wandb/sdk/lib/sock_client.py", line 130, in _sendall_with_error_handle
    sent = self._sock.send(data)
BrokenPipeError: [Errno 32] Broken pipe

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.
```

### 해결책

```
    config['arch']['args']['plm_name'] = wandb.config['plm_name']
    config['data_module']['args']['plm_name'] = wandb.config['plm_name']
```

- 각자의 코드에 맞게 모델의 토크나이저도 동시에 업데이트 해준다.
