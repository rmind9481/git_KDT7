from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 명의 player 객체 생성
    player1 = Player("흥부")
    player2 = Player("놀부")

    dealer = GameDealer()

    # GameDealer가 한 벌의 카드 생성
    dealer.make_deck()

    # 초기 10장의 카드를 나누어 주고, 각 player들은 자신이 가지고 있는 카드 목록을 출력
    card_list1, card_list2 = dealer.distribute_card(10)
    player1.add_card_list(card_list1)
    player1.display_two_card_lists()

    player2.add_card_list(card_list2)
    player2.display_two_card_lists()

    
if __name__ == '__main__':
    play_game()
    #play_game_test() # 특수한 경우 기능 검증을 위해 추가함
