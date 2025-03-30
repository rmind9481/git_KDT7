
# 필요한 라이브러리 가져오기

import math 	# 수학패키지
import torch 	# 파이토치 모듈 임포트
import matplotlib.pyplot as plt # 시각화 라이브러리



# 학습률 정의
learning_rate = 0.000001 



# 학습 2000번 진행
# -pi 부터 pi 사이에서 점을 1000개 추출

x = torch.linspace(-math.pi, math.pi, 1000)
#print(x)

# 실제 사인곡선에서 추찰한 값으로 y 만들기
y = torch.sin(x)
#print(y)

# 예측 사인곡선에 사용할 임의 가중치(계수)를 뽑아 y 만들기
a = torch.randn(())
b = torch.randn(())
c = torch.randn(())
d = torch.randn(())


y_random = a*x**3 + b* x**2 + c* x+d	

# 사인 함수를 근사할 3차 다항식 정의
for epoch in range(2000):

	y_pred = a*x**3 + b* x**2 + c* x+d	

	# 손실정의
	loss = (y_pred - y ).pow(2).sum().item()
	
	if epoch % 100 == 0:
		print(f' epoch : {epoch+1}, loss: {loss}')

	# 기울기의 미분값
	grad_y_pred = 2.0 * (y_pred - y) 
	# 가중치의 합
	grad_a = (grad_y_pred * x **3).sum()
	grad_b = (grad_y_pred * x **2).sum()
	grad_c = (grad_y_pred * x).sum()
	grad_d = grad_y_pred.sum()

	# 가중치 업데이트
	a -= learning_rate * grad_a
	b -= learning_rate * grad_b
	c -= learning_rate * grad_c
	d -= learning_rate * grad_d


# 실제 사인곡선을 그리기
plt.subplot(3,1,1)
plt.title('True Y')
plt.plot(x,y)

# 예측한 사인곡선을 그리기
plt.subplot(3,1,2)
plt.title('y_pred')
plt.plot(x, y_pred)

#랜덤한 가중치의 사인 곡선 그리기
plt.subplot(3,1,3)
plt.title('y_random')
plt.plot(x, y_random)

# 서브플롯 간 여백 조정
plt.tight_layout()
plt.show()


