import numpy as np 
import matplotlib.pyplot as plt
# 데이터
X = np.array([2]) # 공부시간
y = np.array([80]) # 실제성적

# 파라미터 초기화
W = 30.0
b = 10.0
learning_rate = 0.01
loss_history= []

for Epoch in range(50):
    # 순전파

    y_pred = X*W+b
    loss = np.mean((y-y_pred)**2)
    loss_history.append(loss)
    # 미분
    dL_dy_pred = -2*(y-y_pred)
    dL_dw = dL_dy_pred*X
    dL_db = dL_dy_pred*1

    # 가중치 없데이트
    W -= learning_rate*dL_dw
    b -= learning_rate*dL_db

    # 중간 결과 출력

    print(f'Epoch {Epoch+1}, Loss: {float(loss):.4f}, W: {W.tolist()}, b: {b.tolist()}')

# 최종결과

print(f'\n최종 W: {W.tolist()}, 최종 b: {b.tolist()}')


# Loss 변화 그래프

plt.figure(figsize=(8,4))
plt.plot(loss_history, marker='o')
plt.title('MES Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid()
plt.show()

    # print(f'{i} 번째')
    # print("="*50)
    # print(f'W:{W}, b:{b}')
    # print(f"y = {y}, y_pred : {y_pred}")
    # print()
