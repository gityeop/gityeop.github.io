---
title: "Data Visualization Examples"
excerpt: "데이터 시각화 예시들"
tags: ["data-analysis", "visualization", "matplotlib"]
---

```python
import numpy as np
import matplotlib.pyplot as plt
```

### Polar Plot Example

#### 1. **폴라 차트 개요**

- **극좌표계**: 폴라 차트는 극좌표계를 사용하는 차트입니다.
- **서브플롯 및 프로젝션**: `subplot`에서 `projection='polar'`를 사용하면 극좌표 차트를 생성할 수 있습니다.
- **`Figure.add_subplot(polar=True)`**: 극좌표계를 추가 가능.
- **RTX**: 기본적으로 0, 1, 2로 설정된 RTX 값을 원하는 구간에 맞게 조정할 수 있습니다.
- **R 레이블**: `set_rlabel_position`으로 R 레이블의 각도를 조정 가능.

#### 2. **폴라 차트 활용**

- **시작 각도 및 종료 각도**: `set_theta_offset`, `set_theta_max`를 사용해 시작 및 종료 각도를 설정.
- **디자인 및 색상**: `cmap='hsv'`로 색상 맵을 설정해, 각도에 따라 빨주노초파남보 색상이 적용.
- **차트 스타일**: 부채꼴 모양, 소라 모양 등 다양한 스타일로 시각화 가능.

#### 3. **폴라 차트에서 사용되는 주요 함수와 메서드**

- **`plt.subplot(projection='polar')`**: 극좌표를 사용하여 폴라 차트를 생성하는 메서드.
- **`ax.set_rlabel_position(angle)`**: R 레이블의 위치를 특정 각도로 조정하는 메서드.
- **`ax.set_theta_offset(offset)`**: 시작 각도를 조정하는 메서드.
- **`ax.set_theta_max(max_angle)`**: 종료 각도를 설정하는 메서드.
- **`plt.scatter()`**: 폴라 차트에 산점도를 추가하는 함수.
- **`ax.plot()`**: 폴라 차트에 선을 추가하는 함수.

```python
theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(theta) * np.cos(theta))
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rlabel_position(-22.5)  # Move the label position
ax.set_theta_offset(np.pi / 4)  # Offset the start angle
ax.set_theta_direction(-1)  # Set theta direction
plt.show()
```

![Image](https://i.imgur.com/An8IED0.png)

### Radar Chart Example

#### 4. **레이더 차트**

- **세타 및 R**: 세타와 R 값을 분리하여 차트를 그리며, 선 그래프와 내부 채우기 가능.
- **세타 그리드, 세타 오프셋**: 시작 각도와 그리드를 조정해 차트를 좀 더 명확하게 표현.

#### 5. **레이더 차트에서 사용되는 주요 함수와 메서드**

- **`plt.subplot(projection='polar')`**: 레이더 차트 역시 극좌표를 사용하며, 폴라 차트와 동일한 메서드를 사용.
- **`ax.fill()`**: 선 그래프 내부를 채우는 메서드.
- **`ax.plot()`**: 데이터 포인트를 연결하는 선 그래프를 그리는 메서드.
- **`ax.set_theta_offset(offset)`**: 시작 각도를 조정하여 차트를 회전하는 메서드.
- **`ax.set_theta_direction(-1)`**: 각도의 방향을 시계 반대방향으로 설정하는 메서드.

```python
labels=np.array(['A', 'B', 'C', 'D'])
stats=np.array([80, 70, 90, 85])

angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
stats=np.concatenate((stats,[stats[0]]))
angles+=angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='green', alpha=0.25)
ax.plot(angles, stats, color='green', linewidth=2)
plt.show()
```

![Image](https://i.imgur.com/atQDuQd.png)

### Pie Chart Example

#### 6. **파이 차트**

- **기본 개념**: 원형 안에 비율을 구분하여 표시하는 차트로, `plt.pie()` 메소드를 사용.
- **막대 그래프와의 비교**: 막대 그래프는 파이 차트보다 값의 비교에 적합. 각에 대한 인지가 길이에 대한 인지보다 떨억지기 때문.
- **스타일링 옵션**:
  - `startangle`: 시작 각도 설정.
  - `explode`: 특정 조각을 강조하기 위해 밖으로 튀어나오게 설정.
  - `shadow`: 그림자를 추가하여 시각적 효과.
  - `autopct`: 각 조각의 비율을 퍼센트로 표시.
  - `labeldistance`: 레이블을 원으로부터 떨어뜨려 표시.

#### 7. **파이 차트에서 사용되는 주요 함수와 메서드**

- **`plt.pie(data, labels, startangle)`**: 파이 차트를 그리는 기본 함수.
- **`explode`**: 파이 차트에서 특정 조각을 강조하기 위해 밖으로 튀어나오게 하는 옵션.
- **`shadow`**: 파이 차트에 그림자를 추가하는 옵션.
- **`autopct`**: 파이 차트의 각 조각에 비율을 퍼센트로 표시하는 옵션.
- **`labeldistance`**: 레이블을 원으로부터 떨어뜨려 표시하는 거리 조정 옵션.

```python
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
explode = (0, 0.1, 0, 0)  # explode 2nd slice
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.show()
```

![Image](https://i.imgur.com/yAtZEbw.png)

### Donut Chart Example

#### 8. **도넛 차트**

- **파이 차트의 변형**: 파이 차트 중심에 원을 그려 도넛 모양을 만듦.
- **중심 원 그리기**: `plt.Circle`을 사용해 도넛 형태로 변형 가능.
- **퍼센트 표시 조정**: 퍼센트 텍스트를 테두리에 맞게 조정하여 시각적 효과를 극대화.

#### 9. **도넛 차트에서 사용되는 주요 함수와 메서드**

- **`plt.pie()`**: 파이 차트를 그린 후, 도넛 차트로 변형하기 위해 원을 그릴 때 사용하는 함수.
- **`plt.Circle((x, y), radius, color)`**: 도넛 차트의 중심에 위치한 원을 그리는 함수.
- **`ax.add_artist()`**: 도넛 차트의 중심 원을 추가하는 메서드.

```python
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
circle = plt.Circle((0, 0), 0.7, color='white')
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.add_artist(circle)
plt.show()
```

![Image](https://i.imgur.com/N5ZUCaf.png)

### Missingno Example

#### 10. **Missingno**

- **결측치를 시각화**: 결측치를 시각화할 때 사용하는 라이브러리.
  - **`msno.matrix(data)`**: 결측치를 시각화하는 메서드.
  - **`msno.heatmap(data)`**: 결측치 간의 상관관계를 시각화하는 메서드.
  - **`msno.dendrogram(data)`**: 결측치의 계층적 클러스터링을 시각화하는 메서드.

```python
import pandas as pd
import seaborn as sns
df = pd.DataFrame({
    'A': [1, np.nan, 3, 4, np.nan],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, np.nan, 4, 5]
})
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.show()
```

![Image](https://i.imgur.com/qxyEmJp.png)

```python
%pip install missingno
```

```python
# 필요한 라이브러리 설치 (만약 설치되어 있지 않은 경우)
# pip install missingno

import missingno as msno
import pandas as pd
import numpy as np

# 샘플 데이터 생성
df = pd.DataFrame({
    'A': [1, np.nan, 3, 4, np.nan],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, np.nan, 4, 5],
    'D': [np.nan, 2, np.nan, 4, np.nan],
    'E': [1, np.nan, 3, 4, 5]
})

# 결측치 매트릭스 시각화
msno.matrix(df)
plt.show()

# 결측치 히트맵 시각화
msno.heatmap(df)
plt.show()

# 결측치 덴드로그램 시각화
msno.dendrogram(df)
plt.show()

```

![Image](https://i.imgur.com/fENIIKq.png)

![uploading...](http://i.imgur.com/uploading.png)

![Image](https://i.imgur.com/DfxUilD.png)

### Treemap Example

#### 11. **Treemap**

- **트리맵 시각화**: 아직 널리 사용되지 않는 트리맵 시각화 라이브러리 `squarify`.
  - **`squarify.plot(sizes, label, color)`**: 트리맵을 그리는 함수.
  - **`plt.axis('off')`**: 트리맵의 축을 숨기기 위한 함수.

```python
%pip install squarify
```

```python
import squarify
sizes = [500, 300, 200, 100]
labels = ['A', 'B', 'C', 'D']
colors = sns.color_palette('viridis', len(sizes))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.axis('off')
plt.show()
```

![Image](https://i.imgur.com/VJFKKXY.png)

### Waffle Chart Example

#### 12. **Waffle Chart**

- **와플 차트 시각화**: `pywaffle` 라이브러리를 사용하여 와플 형태의 차트를 생성.
  - **`Waffle(rows, values, colors, legend)`**: 와플 차트를 생성하는 기본 함수.
  - **`FontAwesome`**: 와플 차트의 아이콘을 추가할 때 사용하는 폰트 라이브러리.

```python
%pip install pywaffle
```

```python
from pywaffle import Waffle
data = {'Category A': 30, 'Category B': 20, 'Category C': 50}
fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data,
    colors=["#232066", "#983D3D", "#DCB732"],
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
    icons='star', icon_size=18, icon_legend=True
)
plt.show()
```

![Image](https://i.imgur.com/RztdGGT.png)

### Venn Diagram Example

#### 13. **Venn Diagram**

- **벤 다이어그램 시각화**: 집합의 교집합을 시각화하는 벤 다이어그램 생성 가능.
  - **`plt.venn2(subsets)`**: 두 개의 집합을 나타내는 벤 다이어그램을 생성하는 함수.
  - **`plt.venn3(subsets)`**: 세 개의 집합을 나타내는 벤 다이어그램을 생성하는 함수.

```python
%pip install matplotlib_venn
```

```python
from matplotlib_venn import venn2
venn2(subsets = (10, 5, 2), set_labels = ('A', 'B'))
plt.show()
```

![Image](https://i.imgur.com/rJ8EeoJ.png)

### Facet Example

#### 14. **Facet**

- **여러 개의 플롯 배치**: `subplot`으로 여러 플롯을 n x n 형태로 배치 가능.
- **dpi 설정**: 해상도 조정으로 차트의 품질을 향상.
- **grid_spec**: 특정 영역을 잘라 플롯 배치.
- **Aspect Ratio**: 플롯의 가로 세로 비율을 일정하게 유지.

#### 15. **Facet에서 사용되는 주요 함수와 메서드**

- **`plt.subplots(nrows, ncols)`**: 여러 플롯을 배치하기 위한 기본 함수.
- **`plt.set_facecolor(color)`**: 플롯의 배경색을 설정하는 메서드.
- **`fig.add_subplot()`**: 추가적인 서브플롯을 생성하는 메서드.
- **`plt.grid(True)`**: 그리드를 표시하는 함수.
- **`plt.tight_layout()`**: 플롯 간의 간격을 자동으로 조정하는 함수.

```python
import seaborn as sns
sns.set_theme(style="ticks")
df = sns.load_dataset("penguins")
g = sns.pairplot(df, hue="species")
plt.show()
```

![Image](https://i.imgur.com/7a3FKMs.png)

#### 16. **스파인, 보조선, 보조면**

- **스파인(Spine) 조정**: 테두리 설정, 라인 두께, 색상 조정 가능.
- **보조선/보조면 추가**: 중요한 데이터 포인트 강조를 위해 가로선, 세로선 및 보조면 추가 가능.

#### 17. **스파인, 보조선, 보조면에서 사용되는 주요 함수와 메서드**

- **`ax.spines['left'].set_position('center')`**: 스파인의 위치를 중앙으로 설정하는 메서드.
- **`ax.axhline(y=0, color='k')`**: 가로 보조선을 그리는 함수.
- **`ax.axvline(x=0, color='k')`**: 세로 보조선을 그리는 함수.
- **`ax.axhspan(ymin, ymax, facecolor='0.5', alpha=0.5)`**: 보조면을 추가하는 함수.
- **`ax.axvspan(xmin, xmax, facecolor='0.5', alpha=0.5)`**: 보조면을 추가하는 함수.

#### 18. **커스텀 세팅**

- **커스텀 스타일**: 시각화 스타일을 파일로 저장하고 불러올 수 있음.
- **스타일 사용**: `plt.style.use()`로 스타일 지정 가능.

#### 19. **커스텀 세팅에서 사용되는 주요 함수와 메서드**

- **`plt.style.use('style_name')`**: 스타일을 설정하는 함수.
- **`plt.rcParams['key'] = value`**: 전역 설정을 변경하는 함수.
- **`with plt.style.context('style_name')`**: 특정 스타일을 일시적으로 적용하는 문맥 관리 메서드.

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(-10, 10, 100)
y = np.sin(x)

# 플롯 생성
fig, ax = plt.subplots()

# 데이터 플롯팅
ax.plot(x, y)

# 스파인 조정 - 왼쪽 스파인을 중앙으로 이동
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# 위, 오른쪽 스파인 제거
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 보조선 추가 - 가로선과 세로선을 중앙에 추가
ax.axhline(y=0, color='k', linestyle='--')
ax.axvline(x=0, color='k', linestyle='--')

# 보조면 추가 - 특정 영역 강조
ax.axhspan(ymin=-0.5, ymax=0.5, facecolor='lightgrey', alpha=0.5)
ax.axvspan(xmin=-5, xmax=5, facecolor='lightgrey', alpha=0.5)

plt.show()

```

![Image](https://i.imgur.com/HJs2ltM.png)

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.cos(x)

# 커스텀 스타일 적용
plt.style.use('ggplot')  # 예시: 'ggplot' 스타일 사용

# 커스텀 전역 설정
plt.rcParams['figure.figsize'] = (10, 6)  # 그림 크기 설정
plt.rcParams['lines.linewidth'] = 2  # 라인 두께 설정
plt.rcParams['lines.color'] = 'r'  # 라인 색상 설정

# 플롯 생성
fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
```

![Image](https://i.imgur.com/3h4vhdG.png)
