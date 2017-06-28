import Card_class
import random

class Model_Card:
    '''Класс позволяющий оперировать карточками'''
    def __init__(self):
        # dict() initialization
        self.card_dic = {}

    def add_to_list(self, *args):
        # This method adding all Card objects
        for obj in args:
            if isinstance(obj, Card_class.Card):
                if obj.Teor_name not in self.card_dic.keys():
                    self.card_dic[obj.Teor_name] = obj
                else:
                    print("\nCard already added\n")
                    return False
            else:
                return False
        return True

    def view_list(self):
        cards=[]
        for item in self.card_dic:
            cards.append(self.card_dic[item].strcard())
        return 'List of Cards:\n'+'\n'.join(cards)

    def del_card(self, *args):
        for name in args:
            if name in self.card_dic.keys():
                del self.card_dic[name]
            else:
                print('Card {} is not in list'.format(name))
        return True

    def return_random(self, Num_Cards=1):
        result = []
        for i in range(0, Num_Cards,1):
            random_key = list(self.card_dic.keys())[random.randrange(len(self.card_dic.keys()))]
            result.append(self.card_dic[random_key])
        return result


if __name__=='__main__':
    Manager = Model_Card()
    card_1 = Card_class.Card('Apple', "fdsafdsagfagfagfdagf")
    card_2 = Card_class.Card('Juice', "fagfdagfda")
    card_3 = Card_class.Card('Cake', "AAAAAAAAAAAAAAAAAAAAa")
    card_4 = Card_class.Card('Cola', "BBBBBBBBBBBBBBBBBBBBBBB")
    card_5 = Card_class.Card('OKA', "MMMMMMMMMMMMMMMMMMMMMMMM")

    Manager.add_to_list(card_1, card_2, card_3, card_4, card_5)
    print(Manager.view_list())

    print(Manager.return_random())
    # Manager.del_card('Apple', 'cake')
    # print(Manager.view_list())
