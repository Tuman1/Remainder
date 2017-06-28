# Card class

class Card:
    '''Базовый класс карточек'''
    def __init__(self, Teor_name,Teor_Subs=None):
        self.Teor_name = Teor_name
        self.Teor_Subs = Teor_Subs

    def strcard(self):
        return '\n\tCard name : {} \n\tSubs: {}'.format(self.Teor_name, self.Teor_Subs[:30])

if __name__=='__main__':
    card_1 = Card('Apple', "fdsafdsagfagfagfdagf")
    print(card_1.strcard())
