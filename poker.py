import random
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

results = ['Royal Flush', 'Straight Flush', 'Four of a kind', 'Full House',
           'Flush', 'Straight', 'Three of a kind', 'Two Pair', 'Pair', 'High Card']


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

    def __lt__(self, other):
        return ranks.index(self.get_rank()) < ranks.index(other.get_rank())


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def high_card(self):

        self.cards.sort()
        return self.cards[4]

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_two_pair(self):
        pairs = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    pairs += 1
        if pairs == 2:
            return True
        return False

    def is_three_of_a_kind(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    for k in range(j+1, 5):
                        if self.cards[i].get_rank() == self.cards[k].get_rank():
                            return True
        return False

    def is_straight(self):

        self.cards.sort()

        for i in range(4):
            if ranks.index(self.cards[i].get_rank()) + 1 != ranks.index(self.cards[i+1].get_rank()):
                return False

        return True

    def is_flush(self):

        suit = self.cards[0].get_suit()
        for i in range(1, 5):
            if suit != self.cards[i].get_suit():
                return False

        return True

    def is_full_house(self):

        temp = self.cards.copy()
        temp.sort()

        if self.is_three_of_a_kind():
            if temp[0].get_rank() == temp[1].get_rank() and temp[len(temp)-1].get_rank() == temp[len(temp)-2].get_rank():
                return True
        return False

    def is_four_of_a_kind(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    for k in range(j+1, 5):
                        if self.cards[i].get_rank() == self.cards[k].get_rank():
                            for l in range(k+1, 5):
                                if self.cards[i].get_rank() == self.cards[l].get_rank():
                                    return True
        return False

    def is_straight_flush(self):
        if self.is_flush() and self.is_straight():
            return True
        return False

    def is_royal_flush(self):

        if self.high_card().get_rank() == "A"and self.is_straight_flush():
                return True

        return False

    def check_ranking(self):

        if self.is_royal_flush():
            return "Royal Flush"
        elif self.is_straight_flush():
            return "Straight Flush"
        elif self.is_four_of_a_kind():
            return "Four of a kind"
        elif self.is_full_house():
            return "Full House"
        elif self.is_flush():
            return "Flush"
        elif self.is_straight():
            return "Straight"
        elif self.is_three_of_a_kind():
            return "Three of a kind"
        elif self.is_two_pair():
            return "Two Pair"
        elif self.is_pair():
            return "Pair"
        else:
            return "High Card"