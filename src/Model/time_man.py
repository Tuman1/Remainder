import time

class Time_man:
    '''This class is needed for raising cards according to users needs.'''
    def __init__(self, Manager_card):
        self.Work_state = True
        self.Manager_card = Manager_card
    def Each(self, dtime):
        # Randam return of the card each dtime
        dtime_sec = dtime * 60
        while True:
            if Work_state:
                time.sleep(dtime_sec)
                self.Manager_card.return_random(3)
            else:
                break
        return True

    # def

if __name__=='__main__':
    import Card_class
    import Model_card
    Manager = Model_card.Model_Card()
    card_1 = Card_class.Card('Apple', "fdsafdsagfagfagfdagf")
    card_2 = Card_class.Card('Juice', "fagfdagfda")
    card_3 = Card_class.Card('Cake', "AAAAAAAAAAAAAAAAAAAAa")
    card_4 = Card_class.Card('Cola', "BBBBBBBBBBBBBBBBBBBBBBB")
    card_5 = Card_class.Card('OKA', "MMMMMMMMMMMMMMMMMMMMMMMM")

    Manager.add_to_list(card_1, card_2, card_3,card_4,card_5)

    obj = Time_man(Manager)
    print(obj.Work_state)
