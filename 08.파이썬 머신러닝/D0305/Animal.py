# ------------------------------------------------------------------------------
#	동물 데이터를 표현/하는 클래스 정의/설계
#  -----------------------------------------------------------------------------


# ------------------------------------------------------------------------------
#	* 특징/속성/성질/외형 : 품종, 털색상, 눈색상, 무게, 나이, 성별, 이름
#	* 행동/기능/동작	 : 짖는다, 문다, 꼬리친다, 죽는척하기(x - 특별한 강아지)
# ------------------------------------------------------------------------------


class Animal:

	def __init__(self, kind, coat_color, eye_color,weight,age,gender, name):
		print('Animal___init__()', self)
		self.kind = kind
		self.coat_color = coat_color
		self.eye_color = eye_color
		self.weight = weight
		self.age = age
		self.gender = gender
		self.name = name
	
	# 메소드이름 : tailing

	def tailing(self):
		print(f'{self.name}가 꼬리친다.')