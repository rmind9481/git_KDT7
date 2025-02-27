import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sample_list = [1,2,3,4,5]

print(sample_list)


sample_array = np.array([1,2,3,4,5])
print(sample_array)

# ---------------------------

a = sample_array +2 
print(a)

#----------------------------------

# 행렬
sample_array_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(sample_array_2)


a_choice = np.random.choice([1,2,3],3)

print(a_choice)


df = pd.read_csv('./ch4_scores400.csv')
scores = np.array(df['score'])
print(scores[:10])

# 표본 추출 방법
# 무작위 추출 (임의 추출) : 임의로 표본을 추출하는 방법
np.random.choice([1,2,3],3)
# 비복원 추출 : 동일한 표본은 한번만 선택하는 방법 
print(np.random.choice([1,2,3],3, replace=False))


## 표본추출방법 

#a_seed = np.random.seed(0)
#print(a_seed)
print(np.random.choice([1,2,3],3))
mean_a = []
for i in range(5):
	sample = np.random.choice(scores,20)
	print(f'{i+1}번째 무작위 추출로 얻은 표본평균',sample.mean())
	mean_a.append(sample.mean())

print(f'mean_a.mean() 얻은 평균', (sum(mean_a)/len(mean_a)))


# 확률변수

dice = [1,2,3,4,5,6]
prob = [1/21, 2/21, 3/21, 4/21, 5/21, 6/21]

num_trial = 100
sample = np.random.choice(dice, num_trial, p= prob)
print(sample)


# 추측통계의 확률
# 예제 데이터 생성
# np.random.seed(42)
# scores = np.random.randint(0, 100, 1000)  # 0~100 사이 난수 1000개 생성

# 히스토그램 그리기
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.hist(scores, bins=100, range=(0, 100), density=True)

# x축, y축 범위 설정
ax.set_xlim(20, 100)  # x축 범위를 숫자로 설정
ax.set_ylim(0, 0.042)  # y축 범위를 숫자로 설정

# 축 레이블 추가 (set_xlabel(), set_ylabel() 사용)
ax.set_xlabel('Score')  # 'score' 대신
ax.set_ylabel('Relative Frequency')  # 'relative frequency' 대신

# 그래프 출력
plt.show()

# 무작위추출에 의한 표본평균으로 모평균 추측가능
sample_means = [np.random.choice(scores,20).mean()
				for _ in range(10000)]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hist(sample_means, bins=100, range=(0,100), density=True)
# 모평균을 세로선으로 표시

ax.vlines(np.mean(scores), 0,1, 'gray')
ax.set_xlim(50,90)
ax.set_ylim(0,0.13)
ax.set_xlabel('Score')
ax.set_ylabel('relative frequency')
plt.show()


# --------------------------------------------------
# 1차형 이산형 확률 변수
# --------------------------------------------------

def short_function(x):
	return x*2


equiv_anon = lambda x:x*2

def apply_to_list(some_list,f ):
	return [f(x) for x in some_list]
ints= [4,0,1,5,6]

print(apply_to_list(ints, lambda x: x*2))



# ---------------------------------------------------------
# 2차형 이산형 확률 변수
# ---------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# X와 Y의 가능한 값 설정
x_set = np.arange(2, 13)  # x의 값 범위: 2부터 12까지 (주사위 2개의 합)
y_set = np.arange(1, 7)   # y의 값 범위: 1부터 6까지 (하나의 주사위 값)

# 확률 밀도 함수 정의
def f_xy(x, y):
    if 1 <= y <= 6 and 1 <= x - y <= 6:  # 주어진 조건을 만족하는 경우만 확률값 계산
        return y * (x - y) / 441  # 확률 값 계산
    else:
        return 0  # 조건을 만족하지 않으면 확률은 0

# 2차원 확률 배열 생성
prob = np.array([[f_xy(x_i, y_j) for y_j in y_set] for x_i in x_set])

# 그래프 생성
fig = plt.figure(figsize=(10, 8))  # 그래프 크기 설정
ax = fig.add_subplot(111)  # 서브플롯 추가

# 확률 값을 컬러맵으로 표현
c = ax.pcolor(prob)

# X, Y 축 눈금 설정 (중앙 정렬을 위해 0.5를 더함)
ax.set_xticks(np.arange(prob.shape[1]) + 0.5, minor=False)  # x축 눈금
ax.set_yticks(np.arange(prob.shape[0]) + 0.5, minor=False)  # y축 눈금

# 올바른 눈금 레이블 설정
ax.set_xticklabels(np.arange(1, 7))  # x축 레이블을 주사위 값 (1~6)으로 설정
ax.set_yticklabels(np.arange(2, 13))  # y축 레이블을 두 주사위의 합 (2~12)로 설정

ax.invert_yaxis()  # y축을 뒤집어 위에서 아래로 값이 증가하도록 설정
ax.xaxis.tick_top()  # x축 눈금을 상단으로 이동

fig.colorbar(c, ax=ax)  # 컬러바 추가하여 확률 값 시각적으로 표시

# 그래프 출력
plt.show()

# ====================================================================
# 결합 확률 질량 함수 f_xy(x, y)를 기반으로 X와 Y의 주변 확률을 계산하는 함수

# X의 주변 확률을 계산하는 함수: y_set의 모든 y 값에 대해 f_xy(x, y)를 합산
def f_x(x):
    return np.sum([f_xy(x, y_k) for y_k in y_set])

# Y의 주변 확률을 계산하는 함수: x_set의 모든 x 값에 대해 f_xy(x, y)를 합산
def f_y(y):
    return np.sum([f_xy(x_k, y) for x_k in x_set])

# X와 Y에 대한 값과 확률을 저장하는 리스트
x = [x_set, f_x]  # X의 값과 f_x 함수
y = [y_set, f_y]  # Y의 값과 f_y 함수

# X의 주변 확률 분포 계산
prob_x = np.array([f_x(x_k) for x_k in x_set])

# Y의 주변 확률 분포 계산
prob_y = np.array([f_y(y_k) for y_k in y_set])

# 그래프 설정 (12x4 크기의 figure 생성)
fig = plt.figure(figsize=(12, 4))

# 첫 번째 서브플롯 (X의 주변 확률 분포)
ax1 = fig.add_subplot(121)
ax1.bar(x_set, prob_x)  # X값에 대한 막대 그래프
ax1.set_title('X_marginal probability')  # 제목 설정
ax1.set_xlabel('X_value')  # X축 라벨
ax1.set_ylabel('probability')  # Y축 라벨
ax1.set_xticks(x_set)  # X축 눈금 설정

# 두 번째 서브플롯 (Y의 주변 확률 분포)
ax2 = fig.add_subplot(122)
ax2.bar(y_set, prob_y)  # Y값에 대한 막대 그래프
ax2.set_title('Y_marginal probability')  # 제목 설정
ax2.set_xlabel('Y_value')  # X축 라벨
ax2.set_ylabel('probability')  # Y축 라벨

# 그래프 표시
plt.show()


# ----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy import integrate

# 특정 경고 메시지(IntegrationWarning)를 무시
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

# 1차원 연속형 확률 변수 정의

# X의 범위를 [0,1]로 설정
x_range = np.array([0, 1])

# 확률 밀도 함수(PDF) f(x) 정의
def f(x):
    if x_range[0] <= x <= x_range[1]:  # X가 [0,1] 구간 내에 있을 때
        return 2 * x  # f(x) = 2x
    else:  # 그 외의 경우
        return 0  # 확률 밀도는 0

# X의 값과 확률 밀도 함수를 저장
x = [x_range, f]

# X의 범위에서 100개의 균등한 점 생성 (그래프 그리기 위해)
xs = np.linspace(x_range[0], x_range[1], 100)

# 그래프 설정 (10x6 크기의 figure 생성)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# 확률 밀도 함수 f(x) 그래프
ax.plot(xs, [f(x) for x in xs], label='f(x)', color='gray')

# 보조선 추가 (x축과 y축 기준선)
ax.hlines(0, -0.2, 1.2, alpha=0.3)  # x축 기준선
ax.vlines(0, -0.2, 2.2, alpha=0.3)  # y축 기준선 (x=0)
ax.vlines(xs.max(), 0, 2.2, linestyles=':', colors='gray')  # x=1에서 점선 추가

# 특정 구간 (0.4 ~ 0.6)에서 확률 밀도 함수 아래 영역 채우기
xs = np.linspace(0.4, 0.6, 100)
ax.fill_between(xs, [f(x) for x in xs], label='prob')

# x축과 y축 눈금 설정
ax.set_xticks(np.arange(-0.2, 1.3, 0.1))  # x축 눈금 (-0.2 ~ 1.2, 0.1 간격)
ax.set_xlim(-0.1, 1.1)  # x축 범위 설정
ax.set_ylim(-0.2, 2.2)  # y축 범위 설정

# 범례 추가
ax.legend()

# 그래프 표시
plt.show()


# 특정 경고 메시지(IntegrationWarning)를 무시
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

# 1차원 연속형 확률 변수의 범위 설정
x_range = np.array([0, 1])

# 확률 밀도 함수(PDF) f(x) 정의
def f(x):
    if x_range[0] <= x <= x_range[1]:  # X가 [0,1] 범위 내에 있을 때
        return 2 * x  # f(x) = 2x
    else:  # 그 외의 경우
        return 0  # 확률 밀도는 0

# 누적 분포 함수(CDF) F(x) 정의: f(x)를 적분하여 계산
def F(x):
    return integrate.quad(f, -np.inf, x)[0]  # 적분 범위: (-∞, x]

# 확률 계산: P(0.4 ≤ X ≤ 0.6) = F(0.6) - F(0.4)
print(F(0.6) - F(0.4))

# X의 범위에서 100개의 균등한 점 생성 (그래프 그리기 위해)
xs = np.linspace(x_range[0], x_range[1], 100)

# 그래프 설정 (10x6 크기의 figure 생성)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# 누적 분포 함수 F(x) 그래프
ax.plot(xs, [F(x) for x in xs], label='F(x)', color='gray')

# 보조선 추가 (x축과 y축 기준선)
ax.hlines(0, -0.1, 1.1, alpha=0.3)  # x축 기준선
ax.vlines(0, -0.1, 1.1, alpha=0.3)  # y축 기준선 (x=0)
ax.vlines(xs.max(), 0, 1, linestyles=':', color='gray')  # x=1에서 점선 추가

# x축과 y축 눈금 설정
ax.set_xticks(np.arange(-0.1, 1.2, 0.1))  # x축 눈금 (-0.1 ~ 1.1, 0.1 간격)
ax.set_xlim(-0.1, 1.1)  # x축 범위 설정
ax.set_ylim(-0.1, 1.1)  # y축 범위 설정

# 범례 추가
ax.legend()

# 그래프 표시
plt.show()

#----------------------------------------------------------------
# 2차형 연속확률 변수
# ---------------------------------------------------------------

x_range = [0,2]
y_range = [0,1]

def f_xy(x,y):
	if 0 <= y <=1 and 0 <= x -y <=1:
		return 4 * y * (x-y)
    
	else:
		return 0

xy = [x_range, y_range, f_xy]

xs = np.linspace(x_range[0], x_range[1], 200)
ys = np.linspace(x_range[0], x_range[1], 200)

pd = np.array([[f_xy(x,y) for y in ys] for x in xs])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

c = ax.pcolor(pd)
ax.set_xticks(np.linspace(0,200,3), minor=False)
ax.set_yticks(np.linspace(0,200,3), minor=False)

ax.set_xticklabels(np.linspace(0,2,3))
ax.set_yticklabels(np.linspace(0,1,3))

ax.invert_yaxis()
ax.xaxis.tick_top()
fig.colorbar(c, ax=ax)
plt.show()                                

# --------------------------------------------------


from functools import partial

def f_x(x):
    return integrate.quad(partial(f_xy,x), -np.inf, np.inf)[0]

def f_y(y):
    return integrate.quad(partial(f_xy, y=y), -np.inf, np.inf)[0]

xs = np.linspace(*x_range, 100)
ys = np.linspace(*y_range, 100)

fig = plt.figure(figsize=(12,4))
ax1 = fig.add_subplot(121)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
ax2 = fig.add_subplot(122)

ax1.plot(xs, [f_x(x) for x in xs], color  = 'gray')
ax2.plot(ys, [f_y(y) for y in ys], color  = 'gray')

ax1.set_title('X_marginal density function')
ax2.set_title('Y_marginal density function')

plt.show()



