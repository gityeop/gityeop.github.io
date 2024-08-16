## Attention Mechanism

## Transformers

리뷰: MLP 그리고 CNN

- MLP와 CNN이 배우는 내용:
  - Training dataset의 입력 x에서 label y로 가장 잘 매핑되는 가중치 집합
  - 출력 $\hat y$는 input x의 weighted sum

RNN

$$
h_t = f_w(h_{t-1}, x_t) = \tanh(W_{hh}h_{t-1} W_{xh}x_t)
$$

- RNN도 마찬가지로 W는 Loss function 측면에서 Training set의 input과 output을 가장 잘 매핑하도록 설계되었음

Transformer의 Main Idea

- 기본 가정: input x는 서로 유기적으로 관련(organically related)된 여러 요소(multiple elements)로 분할될 수 있다.
  - 문장 속의 단어
  - 비디오의 프레임
- Self-attention: 각 element는 해당 context(input의 다른 요소)에 참여하여 own representation을 개선하는 방법을 학습
- 시퀀스에 있는 다른 element들의 weighted sum

Attention (Q, K, V) = Attention 값
query(context)와 key의 dot-produt = similarity
similarity \* value 값의 weighted sum

transformer가 attention과 다른 이유는 Q, K, V를 만들 때 weighted parameter를 사용한다는 것

input token $(x_1, x_2, ..., x_n)$ -> token $x_i$는 linear transformation에 의해 Q, K, V 벡터로 매핑

Linear weights는 learned parameter로 모든 input에서 공유됨

embedding $z_1$은 원래 embedding($x_1$)과 유사한 경향이 있음

- cos($Q_1, K_1$)이 다른 cos($Q_1, K_i$)보다 훨씬 높을 가능성이 높기 때문
- 결과 $z_1$은 여전히 원본과 동일하지는 않음, context($x_2, x_3)의 영향을 약간 받음
- further contextualize를 위해 이 단계를 여러번 반복
