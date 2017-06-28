import datetime

class Time_man:
    '''This class is needed for raising cards according to users needs.'''
    def __init__(self):
        self.Work_state = False

    def SetTime(self, hours=0, minutes=0, seconds=0):
        Alram_Time=datetime.time(hours, minutes, seconds)
        self.Work_state=True
        return Alram_Time

    def RaiseCards(self, command):
        command
        return None
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

    obj = Time_man()
    print(obj.SetTime(hours=1, minutes=1, seconds=1))
    print(obj.Work_state)
    print(obj.RaiseCards(print("Hello")))
