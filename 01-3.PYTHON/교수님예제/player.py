class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()

    def add_card_list(self, card_list):
        for card in card_list:
            self.holding_card_list.append(card)

    def add_card(self, card):
        self.holding_card_list.append(card)

    def display_two_card_lists(self):
        print('=' * 60)

        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        for card in self.open_card_list:
            print(card, end=' ')
        print()
        print()

        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        for card in self.holding_card_list:
            print(card, end=' ')
        print()
        print()

    def check_one_pair_card(self):
       pass 

    