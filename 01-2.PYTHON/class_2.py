class BankAccount:
	def __init__(self):
		self.balance = 0

	
	def withdraw(self, amount):
		
		# 10000 단위 출금 및 잔액이 출금 금액보다 많은 경우에 정상ㅊ ㅜㄹ금
		# 아니면 에러 메세지 출력
		print(f"잔액: {self.balance}, {amount} 원 출금되었음")
		self.balance -= amount


	def deposit(self, amount):
		self.balance += amount
		print('통장에',amount,'원 입금되었음')



a = BankAccount()
