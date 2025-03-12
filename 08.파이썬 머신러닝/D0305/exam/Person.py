class Person : 

	def __init__(self,name,age,gender,height,weight ):
		self.name = name
		self.age = age
		self.gender = gender
		self.height = height
		self.weight = weight
		self.life_energe = int(height*weight)
		self.vitality = (self.life_energe*50/age)
	
	def introduction(self):
		print(f'저의 이름은 {self.name} 입니다.')
		print(f'저의 나이는 {self.age} 입니다.')
		print(f'저의 성별은 {self.gender} 입니다.')
		print(f'저의 키는 {self.height} 입니다.')
		print(f'저의 몸무게는 {self.weight} 입니다.')
		print(f'에너지 {self.life_energe}')
		print(f'활력 {self.vitality}')

	def dead(self):

		print(f'{self.name} 사망하셨습니다.')

	def demege(self,demege):
		
		print(f'아?? 왜 때려요?')
		self.life_energe = self.life_energe - demege
		
		if self.life_energe <0:
			self.dead()
		
		print(f'{self.life_energe}') 

	
	def sleep(self):
		print(f'잠에 듭니다.')
	
	def eating(self):
		print(f'밥을 먹습니다.')

