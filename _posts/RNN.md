## RNN이란

시계열 데이터를 처리하기 위해 만들어진 모델

- 장점
  - 가변적인 길이의 input sequence를 처리할 수 있음
  - 입력이 많아져도 모델의 크기는 증가하지 않음
  - (이론적으로) t 시점에서 수행된 계산은 여러 단계 이전의 정보를 사용할 수 있음
  - 모든 단계에서 동일한 가중치가 적용됨
- 단점
  - Recurrent computation이 느림
  - 병렬화(parallelization)가 어려움
  - 바닐라 RNN은 훈련 중 **기울기 소실** 문제를 겪음
  - 바닐라 RNN은 종종 시퀀스 내 장거리 의존성(long-range dependence)를 모델링하는데 실패함
  - 실제로는 여러 단계 이전의 정보에 접근하기 어려움

Issue 1
RNN은 Vanishing/Exploding Gradient 문제가 있어서 long-range dependence를 모델링하기 어려움 -> LSTM/GRU

Issue 2
Many-to-Many RNN은 입력/출력 시퀀스의 길이가 다를 때 유연하게 대응하기 어려움 -> Seq2seq model

Issue 3
LSTM/GRU마저도 매우 긴 시퀀슬ㄹ 처리할 때 문제가 발생함 -> Attention model

## Exploding / Vanishing Gradient Problem in RNN

$$
h_t = \tanh(\mathbf{W}_{hh}\mathbf{H}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t)
$$

똑같은 $\mathbf{W}_{hh}$와 $\mathbf{W}_{xh}$를 사용함

$$
\frac{\partial \mathbf{h}_t}{\partial \mathbf{h}_{t-1}} = \tanh'\left(\mathbf{W}_{hh}\mathbf{h}_{t-1} + \mathbf{W}_{xh}\mathbf{x}_t\right) \mathbf{W}_{hh}
$$

$\mathbf{W}_{hh}$가 곱해지는게 문제

$$
\frac{\partial \mathcal{L}_t}{\partial \mathbf{W}_{hh}} = \frac{\partial \mathcal{L}_t}{\partial \mathbf{h}_t} \frac{\partial \mathbf{h}_t}{\partial \mathbf{h}_{t-1}} \cdots \frac{\partial \mathbf{h}_2}{\partial \mathbf{h}_1} \frac{\partial \mathbf{h}_1}{\partial \mathbf{W}_{hh}}
$$

$$
= \frac{\partial \mathcal{L}_t}{\partial \mathbf{h}_t} \left( \prod_{k=2}^{t} \frac{\partial \mathbf{h}_k}{\partial \mathbf{h}_{k-1}} \right) \frac{\partial \mathbf{h}_1}{\partial \mathbf{W}_{hh}}
= \frac{\partial \mathcal{L}_t}{\partial \mathbf{h}_t} \left( \prod_{k=2}^{t} \tanh'(\mathbf{W}_{hh}\mathbf{h}_{k-1} + \mathbf{W}_{xh}\mathbf{x}_k)\mathbf{W}_{hh} \right)
\frac{\partial \mathbf{h}_1}{\partial \mathbf{W}_{hh}}
$$

$$
= \frac{\partial \mathcal{L}_t}{\partial \mathbf{h}_t} \left( \prod_{k=2}^{t} \tanh'(\mathbf{W}_{hh}\mathbf{h}_{k-1} + \mathbf{W}_{xh}\mathbf{x}_k)\right) \mathbf{W}_{hh}^{t-1} \frac{\partial \mathbf{h}_1}{\partial \mathbf{W}_{hh}}
$$

$\tanh$에 들어간 값이 크거나 작은 값이면 vanishing gradient

$\mathbf{W}^{t-1}_{hh}$ 동일한 행렬의 반복적인 multiplication

- 1 이상이면 Exploding gradients
- 1 이하면 Vanishing gradients

Weight Initailization을 해도 모델이 deep하면 분산이 0으로 수렴

X가 정확히 1이 아닌 한 $x^k$가 발산하거나 large k 와 함께 0으로 수렴할 것

- k는 neural network의 depth

RNN은 Input sequence length가 depth처럼 작용

해결책 Clipping: 값이 커? 그럼 쳐내

- gradient가 특정 threshold값을 최대값으로 Gradient Clipping됨
- 각 dimension은 기울기 방향을 유지하기 위해 비례적으로 축소되어야 함

Vanishing Gradients
다음 inputs에서의 loss는 초기 stage로 잘 전달되지 않음

## LSTM: Toward Modeling Longer Dependence

바닐라 RNN이 **Fully Connected**를 통과하는 backward 과정에서 기울기 소실이 일어남

이를 방지하기 위해 cell state($c_t$)라 불리는 새로운 hidden state 세트와 FC layer를 우회하는 highway를 도입

![Image](https://i.imgur.com/s1GG7ld.png)

![Image](https://i.imgur.com/EsfkTNI.png)

![Image](https://i.imgur.com/HK83YIA.png)

![Image](https://i.imgur.com/f6aNWAw.png)

![Image](https://i.imgur.com/ql1rcNn.png)

![Image](https://i.imgur.com/8gdVEvb.png)

![Image](https://i.imgur.com/H1j3kso.png)

전반적으로, 입력 $x_t$와 이전 hidden state인 $h_{t-1}$이 다음 hidden state 그리고 cell state $h_t$, $c_t$를 결정할 뿐만 아니라 이전 값을 유지하거나 새로운 값으로 업데이트할지도 결정함

- long-range information을 더 잘 보존할 수 있음
- long-distance dependencies를 완전히 해결하지는 못함

## GRU(Gated Recurrent Unit)

![Image](https://i.imgur.com/S66IyK2.png)

$$
\begin{align*}
r_t &= \sigma(\mathbf{W}_r \mathbf{x}_t + \mathbf{U}_r \mathbf{h}_{t-1} + \mathbf{b}_r) \\
z_t &= \sigma(\mathbf{W}_z \mathbf{x}_t + \mathbf{U}_z \mathbf{h}_{t-1} + \mathbf{b}_z) \\
\mathbf{h}_t &= (1 - z_t) \circ \mathbf{h}_{t-1} + z_t \circ \tanh(\mathbf{W}_h \mathbf{x}_t + \mathbf{U}_h (r_t \circ \mathbf{h}_{t-1}) + \mathbf{b}_h)
\end{align*}
$$

- LSTM과 같이 추가적인 cell states가 필요하지 않음
- LSTM보다 적은 파라미터를 사용함
- LTSM과 유사한 gradient highway를 제공하며, 이전 hidden state와 input에서 계산된 새로운 convex combination을 사용함

PyTorch API: LSTM
![Image](https://i.imgur.com/8IfFKbU.png)

```python
rnn = nn.LSTM(10, 20, 2)
input - torch.randn(5, 64, 10)
h0 = torch.randn(2, 64, 20)
c0 = torch.randn(2, 64, 20)
output, (hn, cn) = rnn(input, (h0, c0))
```

### Practical Guides

- LSTM은 RNN에 대한 좋은 기본 선택
- 더 빠른 계산과 적은 파라미터를 원하면 GRU
- 무거운 자연어 처리(NLP) 문제는 **Transformer**

## Seq2seq Models

### Machine Translation Problem

Many-to-many RNN

- 1:1 관계를 가정함
  - input length = output length
- 1:1 매칭은 불가능함
- 1:1대응이 안된다는 특성 때문에 입력에 기반해서 출력하는 것이 불가능

1. Encoder-Decoder Structure
   ![Image](https://i.imgur.com/BUUnfe6.png)

- 각 단계에서 outputting하지 않음
- 다 문장을 읽어들이면 전체 입력 시퀀스의 의미를 포함하는 Embedding을 가지고 있고 이는 마지막의 hidden state에 저장이 되어있음
- Embedding에서 시작하여 하나씩 출력을 생성하는 Decoder를 구축

Encoder: 문장을 읽어서 저장
Decoder: 저장된 문장을 받아들여서 한 단어씩 해석

loss가 Decoder에서 부터 Encoder까지 쭉 지나감

2. Decoder: Auto-Regressice Generation

- Auto-Regressive: output으로 예측된 단어가 그 다음 단계의 input으로 들어감(Auto-regressice input)

3. Teacher Forcing
   ![Image](https://i.imgur.com/NTLoj9X.png)

- 학습 단계에서, 모델이 올바른 입력에서 나오는 출력을 학습할 필요가 있기 때문에 ground truth data인 $y_{t_1}$을 input으로 사용
- Inference(test) 단계에서는, ground truth 데이터인 $y_{t_1}$ 접근이 불가하기에 실제로 이전 출력인 $\hat y_{t_1}$을 auto-regressively하게 제공함(예측한 값 그대로를 넣어줌)

### Overall seq2seq model

- Encoder는 many-to-one, Decoder는 one-to-many 특성을 가지고 있음
- Input Sequence는 Encoder 끝에서 Single Vector로 인코딩됨
- 이 Single Vector는 Decoder가 출력 시퀀스를 생성함

```python
class EncoderLSTM(nn.Module):
  def __init__(self, input_size, embedding_size, hidden_size, num_layers, p):
    self.input_size = input_size
    self.embedding_size = embedding_size
    self.hidden_size = hidden_size
    self.num_layers = nunm_layers
    slef.dropout = nn.Dropout(p)
    self.embedding = nn.Embedding(self.input_size, self.embedding_size)
    self.LSTM = nn.LSTM(self.embedding_size, hidden_size, num_layers, dropout = p)

  def forward(self, x);
    embedding = self.dropout(self.embedding(x))

    outputs, (hidden_state, cell_state) = self.LSTM(embedding)

    return hidden_state, cell_state

import torch
import torch.nn as nn

class DecoderLSTM(nn.Module):
    def __init__(self, input_size, embedding_size, hidden_size, num_layers, p, output_size):
        super(DecoderLSTM, self).__init__()
        self.input_size = input_size  # one-hot input의 길이
        self.embedding_size = embedding_size  # input token (word embedding) 차원
        self.hidden_size = hidden_size  # hidden representation 차원
        self.num_layers = num_layers  # LSTM 내 레이어 개수
        self.output_size = output_size  # one-hot output 길이 (output language vocab size)
        self.dropout = nn.Dropout(p)

        self.embedding = nn.Embedding(self.input_size, self.embedding_size)
        self.LSTM = nn.LSTM(self.embedding_size, self.hidden_size, num_layers, dropout=p)
        self.fc = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, x, hidden_state, cell_state):
        x = x.unsqueeze(0)  # shape of x: [1, batch_size]
        embedding = self.dropout(self.embedding(x))  # shape: [1, batch_size, embedding_dims]

        # outputs shape: [1, batch size, hidden_size]
        # hs, cs shape: [num_layers, batch_size, hidden_size] → hs, cs from Encoder
        outputs, (hidden_state, cell_state) = self.LSTM(embedding, (hidden_state, cell_state))

        predictions = self.fc(outputs)  # shape: [1, batch size, output_size]
        predictions = predictions.squeeze(0)  # shape: [batch_size, output_size]

        return predictions, hidden_state, cell_state

class Seq2Seq(nn.Module):
    def __init__(self, Encoder_LSTM, Decoder_LSTM):
        super(Seq2Seq, self).__init__()
        self.Encoder_LSTM = Encoder_LSTM
        self.Decoder_LSTM = Decoder_LSTM

    def forward(self, source, target):
        batch_size = source.shape[1]  # source shape: [input language seq len, num_sentences]
        target_len = target.shape[0]  # target shape: [output language seq len, num_sentences]
        target_vocab_size = len(english.vocab)

        outputs = torch.zeros(target_len, batch_size, target_vocab_size)
        hs, cs = self.Encoder_LSTM(source)

        x = target[0]  # Trigger token <SOS>; shape: [batch_size]

        for i in range(1, target_len):
            output, hs, cs = self.Decoder_LSTM(x, hs, cs)
            outputs[i] = output
            x = output.argmax(1)

        return outputs  # shape: [output language seq len, batch_size, target_vocab_size]
```
