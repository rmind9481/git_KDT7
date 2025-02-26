class BankAccount:
	def __init__(self):
		self.name  = 'KDT7은행'
		self.__balance = 0

	def withdraw(self, amount):
		# 10000단위 출금 및 잔액이 출금 금액보다 많은 경우에 정상 출금 
		# 아니면 에러 메시지 출력

		if int(amount) > self.__balance and int(amount)%10000 : 
				self.__balance -= amount
				print(f"잔액: {self.__balance}, {amount}원 출금되었음")
		else:  
			print(f'잔액: {self.__balance}, \n출금액이 너무 작습니다.')



	def deposit(self, amount):
		# 10000원 단위 입금 
		# 아닌 경우, 에러 메시지 출력

		if not int(amount)%10000  : 
			self.__balance += amount
			print(f"{amount}원 입금 되었음, \n잔액: {self.__balance},")
		else:  
			print(f'{amount} 입금 금액이 너무 작습니다. 10000 이상 입금 \n현재 잔액: {self.__balance}')
		

	def print_balance(self):
		print(f'{self.name }현재 잔액: {self.__balance}')


def main():
	bank = BankAccount()
	option = 0
	money = 0
	while True:
		print('1. 입금')
		print('2. 출금')
		print('3. 조회')
		print('4. 종료')
		option = int(input('메뉴 선택: '))

		if option == 4:
			print('프로그램 종료 ')
			break
		elif option == 1:
			money = int(input('입금할 금액을 10000원 단위로 입력하세요: '))
			bank.deposit(money)
		elif option == 2:
			money = int(input('출금할 금액을 10000원 단위로 입력하세요: '))
			bank.withdraw(money)
		elif option == 3:
			bank.print_balance()


main()