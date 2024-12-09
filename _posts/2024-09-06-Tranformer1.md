---
title: "Transformer Part 1"
excerpt: "트랜스포머 모델 이해하기"
tags: ["nlp", "deep-learning", "transformer"]
date: 2024-09-06
categories: machine-learning
---

[Tranformer 1](https://www.boostcourse.org/boostcampaitech7/lecture/1544442?isDesc=false)

## Attention is all you need

- No longer using RNN, CNN modules
- For RNNs, the farther apart the time steps are when computing the hidden state vector, the more likely it is that the hidden state will only contain that information after going through the RNN module by the difference of those time steps.
<!-- -->

### Hash Table T

| Key(동물) | Value(다리 개수) |
| --------- | ---------------- |
| 강아지    | 4                |
| 닭        | 2                |
| 문어      | 8                |
| 오징어    | 10               |
| 고양이    | 4                |

T(“강아지”) = 4
T(“사자”) = “Error: Key is not found”

### Attention is a Hash table with Soft matching

- Find and utilize similar keys even if they don’t exactly match the query
<!-- -->

## Self-Attention(Dot-Product Attention)

Input : One Query q and Multiple Key-Value(k, v) pair
Output : Weighted average of Value vector
weighted = Inner product of its corresponding Key and Query

## Scaled Dot-Product Attention

### Problem

- As d_k gets larger, the variance of Dot-product q, k increase
  - Increased likelihood of certain values within Softmax being unusually large
  - Softmax output has a distribution that is skewed toward one value
  - Gradient becomes very small.
