class Game:
    def guess(self, num):
        if num is None or len(num) != 3:
            raise TypeError