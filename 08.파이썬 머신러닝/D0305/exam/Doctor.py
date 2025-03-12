from Person import Person


class Docter(Person):
	def __init__(self,name,age,gender,height,weight,id_card,hospital):

		super().__init__(name,age,gender,height,weight)
		self.id_card = id_card
		self.hospital = hospital

	def introduction(self):
		super().introduction()
		print(f'저의 의사 면허증 은 {self.id_card} 입니다.')
		print(f'저의 근무 병원은 {self.hospital} 입니다.')
	def working(self):
		print(f'병원에 끌려갑니다.')

	def demege(self, demege):
		super().demege(demege)
		self.life_energe = self.life_energe+(demege/2)
		print(f'{demege/2}을 회복했습니다.')
		print(f'현재 생명력 {self.life_energe}')

if __name__ == '__main__':
	a_sudent = Docter('철수',40,'남',180, 80,'id8300278dmm_938','대구병원')


	a_sudent.introduction()
	a_sudent.demege(1000)
	a_sudent.demege(100000)