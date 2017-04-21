# an AnyList is either:
# - Pair(first, rest), or
# - None
class Pair:
    def __init__(self, first, rest):
        self.first = first # any value
        self.rest = rest # an AnyList
    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)
