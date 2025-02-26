class Counter:	
	def __init__(self, name, value):
		self.count = value
		self.count_name = name
	
	def increment(self):
		self.total_sum = 0   # increment() 내부의 지역 변수
		self.count +=1
		self.total_sum += self.count
	def reset(self):
		self.count = 0
	#	print(f'{total_sum}')

	def get(self):
		return self.count 

a = Counter('KDT7', 0) # 객체생성
a.increment()

print('카운터 a 의 값', a.get())
print(f"'카운터 a의 값은?', {a.count} , count_name : {a.count_name}")


b = Counter('KDT7', 10)
print(f'b의 객체 count 값은: {b.count}, count_name')


class Car :
	def __init__(self, speed, color, model):
		self.speed  = speed
		self.color = color
		self.model = model
	
	def drive(self):
		self.speed = 60

myCar = Car(0,' blue', 'E-class')

print('자동차 객체를 생성하였습니다.')
print('차동차의 속도는', myCar.speed)
print('차동차의 색상는', myCar.color)
print('차동차의 속도는', myCar.model)

