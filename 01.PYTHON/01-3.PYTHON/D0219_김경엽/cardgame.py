from	card	import	Card
from	player	import	Player
from	gamedealer import	GameDealer
def	play_game():
#	두 명의 player	객체 생성
	player1	=	Player("흥부")
	player2	=	Player("놀부")
	dealer	=	GameDealer()

	# 딜러 카드만들기
	dealer.make_deck()
	# 카드 출력
	dealer.print_start()
	# 플레이어에게 카드 10장 배부
	player1_card = dealer.distribute_card(10)
	player2_card = dealer.distribute_card(10)
	
	# 리스트 언팩킹
	for i in range(10):
		#print(type(player1_card[i]))
		player1.add_card_list(player1_card[i])
		player2.add_card_list(player2_card[i])

	dealer.print_start()

	player1.display_two_card_lists()
	player2.display_two_card_lists()

	player2.check_one_pair_card()

if	__name__=='__main__':

	play_game()
	
	

