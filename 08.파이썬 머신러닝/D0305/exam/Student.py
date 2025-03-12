from Person import Person


class Student(Person):
	def __init__(self,name,age,gender,height,weight,school):

		super().__init__(name,age,gender,height,weight)
		self.school = school
	
	def introduction(self):
		super().introduction()
		print(f'{self.school} 입니다.')
		
	def studing(self):
		print(f'학교에 끌려갑니다.')



if __name__ == '__main__':

	a_sudent = Student('철수',10,'남',180, 80,'대구고')


	a_sudent.introduction()
	a_sudent.demege(1000)
	a_sudent.demege(100000)