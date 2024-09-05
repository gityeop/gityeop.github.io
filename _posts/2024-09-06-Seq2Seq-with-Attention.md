---
title: Seq2Seq with Attention
date: 2024-09-06
categories: machine-learning
---

[Seq2Seq with Attention](https://www.boostcourse.org/boostcampaitech7/lecture/1544441?isDesc=false)

## Seq2Seq2 Model

- Take a series of words as input to the Encoder and output a series of converted words to the Decoder
- Latent vector storing information about the input from Encoder
- Can handle variable-length inputs and outputs
<!-- -->

### Problem - Bottleneck problem

- Fixed-size latent vectors can't hold all of the long input information
<!-- -->

### How to solve Bottleneck problem

- Attention
  - At each time step of the Decoder, if focuses on the part of the Hidden-state vector created from the input Sequence that it needs so that if can take that information and write it.
