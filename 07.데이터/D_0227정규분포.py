import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, integrate
from scipy.optimize import minimize_scalar
import koreanize_matplotlib  # 한글 폰트 설정

linestyles = ['-', '--', ':']  # 선 스타일 리스트

def E(X, g=lambda x: x):  # 기대값 계산 함수
    x_range, f = X  # X는 (x_range, f) 형태의 튜플
    def integrand(x):
        return g(x) * f(x)  # 적분 함수 정의: g(x) * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]  # 적분 수행 후 결과 반환

def V(X, g=lambda x: x):  # 분산 계산 함수
    x_range, f = X  # X는 (x_range, f) 형태의 튜플
    mean = E(X, g)  # 기대값 계산
    def integrand(x):
        return (g(x) - mean) ** 2 * f(x)  # 적분 함수 정의: (g(x) - mean) ** 2 * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]  # 적분 수행 후 결과 반환

def check_prob(X):  # 확률밀도함수 검증 함수
    x_range, f = X  # X는 (x_range, f) 형태의 튜플
    f_min = minimize_scalar(f, bounds=(-10, 10), method='bounded').fun  # f(x)의 최솟값 계산
    assert f_min >= 0, 'Density function is negative'  # PDF가 음수가 아니어야 함
    
    prob_sum = np.round(integrate.quad(f, -np.inf, np.inf)[0], 6)  # 적분 값을 1로 검증
    assert prob_sum == 1, f'Sum of probability is {prob_sum}'  # 적분 값이 1인지 확인
    
    print(f'Expected value: {E(X):.3f}')  # 기대값 출력
    print(f'Variance: {V(X):.3f}')  # 분산 출력

def plot_prob(X, x_min, x_max):  # 확률밀도함수 및 누적분포함수 시각화 함수
    x_range, f = X  # X는 (x_range, f) 형태의 튜플
    def F(x):
        return integrate.quad(f, -np.inf, x)[0]  # 누적분포함수(CDF) 계산
    
    xs = np.linspace(x_min, x_max, 100)  # x축 범위 설정
    
    fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 설정
    ax.plot(xs, [f(x) for x in xs], label='f(x)', color='gray')  # PDF 그래프
    ax.plot(xs, [F(x) for x in xs], label='F(x)', ls='--', color='gray')  # CDF 그래프
    
    ax.legend()  # 범례 추가
    plt.show()  # 그래프 표시

def N(mu, sigma):  # 정규분포 정의 함수
    x_range = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)  # x축 범위 설정
    def f(x):
        return 1 / np.sqrt(2*np.pi * sigma**2) * np.exp(-(x-mu)**2 / (2 * sigma**2))  # 정규분포 PDF
    return x_range, f  # x_range와 f 반환

mu, sigma = 2, 0.5  # 평균과 표준편차 설정
X = N(mu, sigma)  # 정규분포 객체 생성

check_prob(X)  # 확률밀도함수 검증
plot_prob(X, 0, 4)  # PDF 및 CDF 시각화

rv = stats.norm(2,0.5)  # 정규분포 객체 생성

rv.pdf(2)  # 특정 값에 대한 PDF 계산
rv.isf(0.3)  # 특정 누적 확률에 대한 역함수 값 계산

# 정규 분포 설정
mu, sigma = 2, 0.5  # 평균과 표준편차 설정
rv = stats.norm(mu, sigma)  # 정규분포 객체 생성

# x 값 범위 설정
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)  # x축 범위 설정

# 확률 밀도 함수 (PDF) 계산
pdf = rv.pdf(x)  # PDF 계산

# 누적 분포 함수 (CDF) 계산
cdf = rv.cdf(x)  # CDF 계산

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))  # 그래프 설정

# 확률 밀도 함수 (PDF) 그래프
ax.plot(x, pdf, label='pdf', color='black')  # PDF 그래프

# CDF 영역 색칠 (X <= 특정 값, 예: x=1.7)
x_fill = np.linspace(mu - 4*sigma, 1.7, 50)  # x값 범위 설정
xs = np.linspace(0, 1.5, 100)  # x축 값 설정
print(xs)
ax.fill_between(xs, [rv.pdf(x) for x in xs], color='g', alpha=0.3)  # PDF 영역 색칠

# 그래프 스타일링
ax.legend()  # 범례 추가
ax.set_xlabel('x')  # x축 라벨 설정
ax.set_ylabel('Density')  # y축 라벨 설정
ax.set_title('정규분포')  # 그래프 제목 설정

plt.show()  # 그래프 표시


# =========================================================

fig = plt.figure(figsize=(10,6))  # 그래프 설정
ax = fig.add_subplot(111)  # 서브플롯 추가

xs = np.linspace(-5,5, 100)  # x축 값 설정
parmas = [(0,1),(0,2),(1,1)]  # 정규분포 파라미터 리스트
for param, ls in zip(parmas, linestyles):  # 파라미터와 선 스타일을 함께 반복
    mu, sigma = param  # 평균과 표준편차 설정
    rv = stats.norm(mu, sigma)  # 정규분포 객체 생성
    ax.plot(xs, rv.pdf(xs), label=f'N({mu},{sigma**2})', ls=ls, color='gray')  # PDF 그래프

ax.legend()  # 범례 추가
plt.show()  # 그래프 표시


# ------------------------------------------------------------------------------

def Ex(lam):
	x_range = [0, np.inf]
	def f(x):
		if x >= 0:
			return lam * np.exp(-lam*x)
		else:
			return 0

	return x_range, f

lam = 3
X = Ex(lam)

check_prob(X)

plot_prob(X,0,2)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

xs = np.linspace(0,3,100)
for lam, ls in zip([1,2,3], linestyles):
    rv = stats.expon(scale=1/lam)
    ax.plot(xs, rv.pdf(xs),
            label=f'lambda: {lam}', ls=ls , color='gray')

ax.legend()

plt.show()

# -----------------------------------------------------
# 카이제곱 분포

# 첫 번째 그래프: 자유도가 10인 카이제곱 분포의 샘플링된 데이터와 이론적인 밀도함수 비교
n = 10  # 자유도
rv=stats.norm()
sample_size=int(1e6)

Zs_sample= rv.rvs((n, sample_size))
chi2_sample = np.sum(Zs_sample**2, axis=0)  # 자유도가 10인 카이제곱 샘플 생성

fig, ax = plt.subplots(figsize=(10, 6))

# 이론적인 카이제곱 밀도 함수
rv_true = stats.chi2(n)
xs = np.linspace(0, 30, 100)
ax.plot(xs, rv_true.pdf(xs), label=f'chi2({n})', color='gray')

# 샘플 데이터의 히스토그램 (밀도 정규화)
ax.hist(chi2_sample, bins=100, density=True, alpha=0.5, label='chi2_sample')

# 범례 및 설정
ax.legend()
ax.set_xlim(0, 30)
plt.show()


# 두 번째 그래프: 자유도 3, 5, 10에 따른 카이제곱 분포 변화
fig, ax = plt.subplots(figsize=(10, 6))

xs = np.linspace(0, 20, 500)
degrees_of_freedom = [3, 5, 10]
linestyles = ['-', '--', ':']

for n, ls in zip(degrees_of_freedom, linestyles):
    rv = stats.chi2(n)
    ax.plot(xs, rv.pdf(xs), label=f'chi2({n})', linestyle=ls, color='gray')

ax.legend()
plt.show()


# ---------------------------------------------------------------

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)


xs = np.linspace(0,20,500)
for n, ls in zip([3,5,10], linestyles):
    rv = stats.chi2(n)
    ax.plot(xs, rv.pdf(xs),
            label = f'ch2({n})', ls=ls, color = 'gray')
    
ax.legend()
plt.show()