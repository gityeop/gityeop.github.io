import numpy as np
import matplotlib.pyplot as plt

# 두 개의 예제 벡터
vector1 = np.array([1, 2])
vector2 = np.array([-1, -1])

# L1 노름 계산
l1_norm_vector1 = np.sum(np.abs(vector1))
l1_norm_vector2 = np.sum(np.abs(vector2))

# L2 노름 계산
l2_norm_vector1 = np.sqrt(np.sum(vector1 ** 2))
l2_norm_vector2 = np.sqrt(np.sum(vector2 ** 2))

print("L1 노름 (vector1):", l1_norm_vector1)
print("L1 노름 (vector2):", l1_norm_vector2)
print("L2 노름 (vector1):", l2_norm_vector1)
print("L2 노름 (vector2):", l2_norm_vector2)

# 단위 원 시각화
theta = np.linspace(0, 2 * np.pi, 100)

# L1 노름 단위 원
l1_unit_circle_x = np.sign(np.cos(theta)) * np.abs(np.cos(theta))
l1_unit_circle_y = np.sign(np.sin(theta)) * np.abs(np.sin(theta))

# L2 노름 단위 원
l2_unit_circle_x = np.cos(theta)
l2_unit_circle_y = np.sin(theta)

plt.figure(figsize=(10, 5))

# L1 노름 단위 원 시각화
plt.subplot(1, 2, 1)
plt.plot(l1_unit_circle_x, l1_unit_circle_y, label="L1 norm unit circle")
plt.scatter(vector1[0], vector1[1], color='red', label='vector1')
plt.scatter(vector2[0], vector2[1], color='blue', label='vector2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("L1 Norm")
plt.legend()
plt.grid(True)
plt.axis('equal')

# L2 노름 단위 원 시각화
plt.subplot(1, 2, 2)
plt.plot(l2_unit_circle_x, l2_unit_circle_y, label="L2 norm unit circle")
plt.scatter(vector1[0], vector1[1], color='red', label='vector1')
plt.scatter(vector2[0], vector2[1], color='blue', label='vector2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("L2 Norm")
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.show()