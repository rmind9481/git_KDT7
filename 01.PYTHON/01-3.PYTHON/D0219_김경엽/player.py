class	Player:
	def	__init__(self,	name):
		self.name =	name
		self.holding_card_list = list()
		self.open_card_list = list()

	# 카드 받아오기
	def	add_card_list(self,	card_list):

		self.holding_card_list.append(card_list)
		

	# 자신의 받은 카드 출력
	def	display_two_card_lists(self):
		print(f'\n[{self.name}] open_card_list : {len(self.open_card_list)}')
		
		print(f"\n\n[{self.name}] holding_card_list :{len(self.holding_card_list)} ")
		
		for i in self.holding_card_list:
			
			print(i, end=' ')
			
		print()
		print(f'='*50)
		
	def	check_one_pair_card(self):
	
		for i in self.holding_card_list:
				print(i.number) 
			
		
	

		