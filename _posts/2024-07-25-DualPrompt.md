---
title: 역할을 나눠서 해보자고 DualPrompt (ECCV 2022)
date: 2024-07-25
categories: machine-learning
---

<div class="email-container">
    
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="font-size: 20px;">역할을 나눠서 해보자고 DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning (ECCV 2022)</h2>
        <br>
        <a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150">
            <img style="max-width: 100%; height: auto;" alt="Thumbnail" src="https://i.ytimg.com/vi/slXjRG_t150/hqdefault.jpg">
        </a>
        <br>
    </div>
    <div style="text-align: left;"><p><a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150&amp;t=0s">00:00</a> 📖 <strong style="font-weight:bold;">논문 소개 및 배경</strong></p>
<p>영상의 시작에서는 진행자가 이번 주에 다룰 논문 “듀얼 프롬프트 컴플리멘터리 프롬프트 학습”에 대해 소개하고 있습니다. 이 논문은 2022년 ECCV에서 발표되었으며, 작성자는 노스이스턴 대학교에서 연구 중인 박사과정 학생으로 구글 클라우드 AI에서 인턴 경험이 있는 분입니다. 이 연구는 최근 인공지능 분야에서 활발히 연구되고 있는 연속 학습(Continual Learning)과 관련된 주제로, 매우 주목받고 있는 내용을 포함하고 있습니다. 논문의 목적은 효과적인 프롬프트 학습 방법을 제안하는 것으로, 진행자는 이를 통해 어떻게 기존의 연속 학습 문제를 해결할 수 있는지를 논의할 것이라고 설명합니다.</p>
<p><a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150&amp;t=90s">01:30</a> 🌐 <strong style="font-weight:bold;">컨티뉴얼 러닝의 필요성 및 문제</strong></p>
<p>이 섹션에서는 연속 학습(컨티뉴얼 러닝)의 기본 개념과 그 이론적 배경에 대해 설명합니다. 컨티뉴얼 러닝이란 여러 개의 태스크를 순차적으로 학습하면서 이전 태스크의 정보를 잃지 않고 지속적으로 학습하는 과제를 뜻합니다. 하지만 이러한 학습 과정에서 발생하는 '재앙적 망각(Catastrophic Forgetting)' 문제는 심각한 어려움 중 하나입니다. 진행자는 이전에 학습한 내용을 잊지 않고 새로운 정보를 효율적으로 학습하기 위해 어떻게 접근해야 하는지를 설명하며, 기존의 방식들이 리허설 버퍼 혹은 메모리 저장 방식에 의존하고 있음을 지적합니다.</p>
<p><a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150&amp;t=180s">03:00</a> 🧠 <strong style="font-weight:bold;">듀얼 프롬프트 접근 방식</strong></p>
<p>진행자는 본 논문에서 제안하는 듀얼 프롬프트 기술에 대해 구체적으로 설명합니다. 듀얼 프롬프트 모델은 일반적인 지식을 학습하는 'g 프롬프트'와 태스크 특정 지식을 학습하는 'e 프롬프트'로 나뉘어져 있습니다. 이러한 이원적인 구조는 뇌 과학에서 영감을 받아 개발되었으며, 뇌의 정보 저장 방식과 연관이 있습니다. 진행자는 이 절차가 어떻게 이루어지는지를 소개하며, 각 모델이 어떻게 협력하여 학습을 진행하는지를 설명합니다. 이러한 방식은 메모리 사용의 비효율성을 줄이고, 다양한 태스크를 효율적으로 처리하는 데 큰 도움이 됩니다.</p>
<p><a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150&amp;t=270s">04:30</a> 📊 <strong style="font-weight:bold;">비전 트랜스포머와 프롬프트 튜닝</strong></p>
<p>이 섹션에서는 비전 트랜스포머와 프롬프트 튜닝 기술에 대해 보다 심도 깊은 설명이 이어집니다. 비전 트랜스포머(ViT)는 이미지를 패치로 나누고 이를 임베딩하여 트랜스포머 인코더에 처리하는 방식입니다. 진행자는 기존의 파인 튜닝이 모델 전반에 큰 오버헤드를 초래하는 반면, 프롬프트 튜닝은 필요에 따라 특정 노드나 레이어만 조정하면서도 효과적인 성능을 달성할 수 있다는 점을 강조합니다. 이는 다양한 태스크를 수행하는 데 있어 효율성을 극대화할 수 있는 방법론입니다.</p>
<p><a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150&amp;t=360s">06:00</a> 🧪 <strong style="font-weight:bold;">실험 설계 및 데이터셋</strong></p>
<p>영상에서는 실험 설계와 사용된 데이터셋에 대해 설명합니다. 진행자는 연구에 사용된 두 가지 벤치마크 데이터셋인 이미지넷과 사이파이 데이터셋에 대해 소개하며, 실험의 조건과 목표에 대한 명확한 설명을 제공합니다. 특히, 실험에서 다양한 스타일의 이미지를 포함한 데이터셋이 어떠한 도전 과제를 제시하는지를 강조합니다. 이어서, '리허설 버퍼'를 사용하지 않고도 높은 성능을 유지할 수 있는 방법론에 대해 논의하며, 기존의 요구되는 메모리 사이즈를 고려했을 때의 장점을 설명합니다.</p>
<p><a rel="noopener noreferrer" href="https://www.youtube.com/watch?v=slXjRG_t150&amp;t=450s">07:30</a> 🎯 <strong style="font-weight:bold;">결과 및 분석</strong></p>
<p>마지막으로, 진행자는 실험 결과를 정리하며 듀얼 프롬프트 접근 방식이 어떤 성과를 이루었는지를 설명합니다. 결과적으로 듀얼 프롬프트는 기존 리허설 기반 방법 없이도 이전 태스크에 대한 정보를 잘 유지하면서도 높은 정확도를 달성했다고 평가합니다. further examination of the tasks evaluated, as well as the optimal positioning of prompts within the model, will be shared. 이러한 성과는 특히 메모리 효율성과 관련하여 이론적 토대와 실용적 적용 모두에서 중요한 의미를 갖습니다. 진행자는 이 연구가 향후 인공지능 연구에 어떻게 기여할 수 있을지를 전망하며 발표를 마칩니다.</p></div>
        </div>
