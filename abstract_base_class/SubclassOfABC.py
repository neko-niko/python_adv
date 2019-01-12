import collections

Card = collections.namedtuple("Card", ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(x) for x in range(2, 11)] + list('JQKA')
    suits = {"spands", "diamonds", "clubs", "hearts"}

    def __init__(self):
        self._cards = [Card(rank, siut) for rank in self.ranks
                                        for siut in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, index, object):
        self._cards.insert(index, object)


