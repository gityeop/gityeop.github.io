## Transformer

1. 아직 해결되지 않은 질문
   - 출력은 여전히 입력 토큰들의 sequence -> 여전히 seq2seq만 가능한 것이 아니냐? classification 또는 regression이 가능할까?
   - 어떻게 Transformer model을 학습시킬 수 있을까?
     - model의 prediction을 Ground Truth와 어디에서 비교해야할까?
     - Loss는 어디에서 발생하나?
   - RNN과 다르게 token의 순서는 무시되는 것 같음. 어떻게 모델링할 수 있을까?
2. Token Aggregation(Average Pooling)
   - 생각할 수 있는 가장 간단한 집계 방법: MEAN
     - 평균을 취하게 되면 전체 input에 대한 single embedding z를 얻게 됨
     - classifier나 regressor를 훈련시킬 수 있음
   - 시퀀스가 매우 길지 않고 비교적 homogeneous한 경우 평균이 효과적
   - 그러나 평균 embedding z는 전체 입력의 meaning을 반영하지 않을 수 있음
   - attention mechanism을 사용할 수 있음
   - 더미 토큰(classification token; [CLS])은 입력 시퀀스에 추가되어 집계된 embedding으로 사용됨
     - 더미 토큰은 어떤 의미도 전달하지 않기 때문에 어떤 토큰에도 치우치지 않음

---

Step 1. Input embeddings
Step 2. Contextualizing the word embedding

- Multi-head Self-attention - 모델이 서로 다른 subspace에 있는 representation을 추출할 수 있어 성능 향상 측면에서 매우 유리함 - 예를 들어 하나의 대명사가 두 개의 값(street, animal) 중 어떤 걸 선택해야할 때 이 두 subspace의 representation을 고려할 수 있어서 성능이 좋음
  ![Image](https://i.imgur.com/La6bt6V.png)

Step 3. Feed-forward Layer

- 각 문맥화된(contextualized)된 embedding은 추가적인 FC layer를 통과함
  $$
  \mathbf{FFN}(x) = max(0, xW_1+b_1)W_2 +b_2
  $$
- Multi-head self-attention 그리고 FC layer 끝에 Residual Connection 그리고 Layer Normalization이 추가됨
  Stacked Self-attention Blocks
- 여러 개(N)의 self-attention bloack이 쌓여 있음

Positional Encoding

- RNN과 달리 토큰에 순서 개념이 없음
- Order infromation을 넣기 위해, Transformer느 Positional encoding을 추가함
- sinusoidal encoding을 사용함으로써, 테스트 시에 임의로 긴 sequence를 처리할 수 있음
  $$
  \begin{align*}
  PE_{(pos, 2i)} &= \sin\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right) \\
  PE_{(pos, 2i+1)} &= \cos\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)
  \end{align*}
  $$
- 이렇게하면 서로 다른 두 인덱스가 같은 인코딩을 가지는 일이 없음
  - Adjacent pos는 유사한 positional encoding을 가짐

Step 4. Decoder Input

- 인코더의 출력 Z = {z1, ..., zn}이 주어지고, output sequence를 auto-regressively하게 생성함
  - 다음 심볼을 생성할 때 이전에 생성된 심볼을 추가 입력으로 사용함
- Positional encoding은 Encoder와 동일한 방식으로 적용됨

Step 5. Masked Multi-head Self-attention

- Transformer의 디코더는 일반적으로 전체 입력 시퀀스를 한 번에 처리할 수 있는데, 테스트 시에는 실제로 다음 단어가 무엇인지 모르기 때문에 훈련 중에도 모델이 현재 시점에서의 입력된 단어들만 참고하도록 만드는 것
  Step 6. Encoder-Decoder Attention

Step 7. Feed-forward Layer

- Encoder와 동일
- Residual, layer normalization: Encoder와 동일
- N Stacked bloack: Encoder와 동일
  - 마지막 레이어의 출력은 next time step에서 입력으로 사용됨

Step 8. Linear Layer

- Output embedding을 class scores로 매핑함

Step 9. Softmax Layer

- Class scores에 softmax를 취해서 확률로 변환함
- 이 점수들은 1-hot-encoded ground truth와 비교됨
  - 그 다음 loss를 가지고 backprop함
- Decoding 단계는 다음 단어가 [EOS]로 예측될 때까지 반복
- 출력된 문장은 탐욕적으로 선택되거나(greedy search), 또는 상위 k-선택이 될 수 있음(beam search)

---

1. Bert: Bidirectional Encoder Representaions from Transformers
   - Transformer encoder를 사용한 대규모 word embedding pre-training
   - Self-supervised: human rating 불필요

- Input sequence는 세 가지를 합한 두 문장으로 구성됨

- Token embedding: pre-trained embedding (WordPiece)
  - [CLS]: 분류 토큰, 항상 시작 부분에 위치합니다. 이 토큰의 최종 hidden state는 분류 작업을 위한 aggregate sequence representation으로 사용됩니다.
  - [SEP]: 구분 토큰, 문장의 끝을 표시하는 데 사용됩니다.
- Segment embedding: 각 토큰이 속한 문장을 나타내는 학습된 embedding
- Position embedding: 시퀀스의 각 위치를 위한 학습된 embedding

과제 1: Masked Language Modeling (MLM)

- 어학시험에서 문장 완성과 유사하게, 문맥을 사용하여 숨겨진 단어를 추측합니다.
- 임의로 15%의 토큰을 마스킹합니다 (특수한 [MASK] 토큰으로 대체).
- 이 위치들에 대한 출력 embedding을 어휘 전체에 걸쳐 분류합니다.

과제 2: Next Sentence Prediction (NSP)

- 입력된 두 문장이 연속적인지 아닌지를 예측하는 이진 분류 문제입니다.
- 학습 데이터의 절반은 두 개의 연속된 문장을 포함합니다 (B는 A의 실제 다음 문장입니다).
- 나머지 절반은 corpus에서 무작위로 선택된 두 문장을 포함합니다.
- 저자들에 따르면, BERT 모델은 이 과제에서 약 ~98%의 정확도를 달성했으며, 여러 작업에 매우
  유익한 성과를 보여주었습니다
  - 추후에는 MLM보다는 덜 중요하다는 것이 밝혀졌습니다.
- 요즘 사전 훈련된 BERT는 word embedding을 위한 기본 선택입니다.

---

3. Vision Transformer

- 표준 트랜스포머 모델이 이미지에 직접 적용됩니다:

  - 이미지는 16x16 패치로 분할됩니다. (각 token은 단어 대신 16x16 image patch입니다.)
  - 이 패치들의 linear embedding sequence가 Transformer에 입력됩니다.
  - 이미지 패치들은 tokens(단어)과 동일한 방식으로 처리됩니다.
  - 최종적으로, 입력 이미지를 분류하기 위해 [CIS] 토큰 위에 MLP가 추가됩니다.

- ViT는 극단적으로 큰 Dataset (예: JFT-300M)에서만 잘
  작동합니다. 왜 그럴까요?
  - ViT는 CNN의 inductive bias (공간적 근접성 및 위치
    불변성)을 가정하지 않습니다.
  - 순전히 데이터에서 특성을 학습해야 합니다. -> 많은
    양의 데이터가 필요합니다.
  - 그러나 충분한 학습 데이터가 제공되면, Spatial
    locality를 넘어서는 복잡한 사례를 모델링할 수 있기
    때문에 CNN 기반 모델보다 뛰어난 성능을 발휘할 수
    있습니다.

Position Embeddings

- ViT는 이미지 내의 거리를 position embeddings의
  유사성을 통해 Encoding하는 방법을 학습합니다.
  - 더 가까운 패치들은 더 유사한 위치
    embedding을 갖는 경향이 나타납니다.
- 행-열 구조가 나타납니다.
  - 동일한 행이나 열에 있는 패치들은 유사한
    embedding을 갖도록 학습됩니다.
- 이런 이유로, 손으로 제작된 2D 인식 embedding
  variants는 개선되지 않습니다.

---

4. ML LifeCycle 총정리

- 1강: 머신 러닝 라이프 사이클 (Machine Learning Life Cycle)
- 2강: Linear Regression, NN Classifier
- 3강: Linear Classifier, Softmax Classifier, Loss Function (손실 함수), Optimization (최적화)
- 4강, 5강: Linear Model, Neural Network, Backpropagation
- 6강: Activation Functions, Weight Initialization, Learning Rate Scheduling
- 7강: Data Processing, Augmentation, Optimization (Gradient Descent, Stochastic
  Gradient Descent)
- 8강: Exploding/Vanishing Gradient Problem, Towards Modeling Longer Dependence,
- 9강: Attention Mechanism, Transformers
- 10강: Attention Mechanism, BERT, Image Data에서의 Transformer

Attention Head : $Z_i = \text{softmax}\left(\frac{Q_i \cdot K_i^\top}{\sqrt{d / N}}\right) \cdot V_i$

Output : $Z = \text{concat}(Z_0, \cdots, Z_{N-1}) \cdot W$

이때 $\textbf{Q}_{i}$, $\textbf{K}_{i}$, $\textbf{V}_{i}$ 는 i번째 head의 Query, Key, Value이고, $d$ 는 Transformer output의 projection dimension, $N$ 은 attention head의 개수입니다.
