from card import Card
import	random


class  GameDealer:
	def	__init__(self):
		self.deck =	list()
		self.suit_number =	13
	#	self.selected_plyear = []

	def	make_deck(self):
		card_suits =	["♠",	"♥",	"♣",	"◆"]
		card_numbers =	["A",	"2",	"3",	"4",	"5",	"6",	"7",	"8",	"9",	"10",	"J",	"Q",	"K"]
		


		for i in card_suits:
			for j in card_numbers:
				self.deck.append(Card(i,j)) #Card('♠', 10)
			
		 
		
	# 카드 10장 리턴/ 남은 deck 에서 저장
	def	distribute_card(self,num):
		
		plyer_card = self.deck[:num]
		self.deck = self.deck[num:]
		
		return plyer_card #, print(plyer_card), print(len(self.deck))
		
		#return  self.plyer_card

	
	def print_start(self):
		if len(self.deck) == 52:
			print(f'[GameDealer] : 초기생성 카드')
		print(f'-'*50)
	
		print(f'[GameDealer] : 딜러가 가진 카드수 : {len(self.deck)}')

		for i in range(len(self.deck)):
			i+=1
			print(self.deck[i-1],end='')
			if not i%13:
				print()
		print()
		if len(self.deck) == 52:
			print()
			print(f'[GameDealer] : 랜덤하게 섞기')
			print(f'-'*50)
			random.shuffle(self.deck)

			for i in range(len(self.deck)):
				i+=1
				print(self.deck[i-1],end='')
				if not i%13:
					print()

		print(f'='*50)
		
		

		
if __name__ == '__main__':
	game = GameDealer()

	game.make_deck()
	game.print_start()
	game.distribute_card(10)