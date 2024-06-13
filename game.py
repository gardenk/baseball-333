class Game:
    def guess(self, num):
        if num is None or len(num) != 3:
            raise TypeError

        for N in num:
            if not ord('0') <= ord(N) <= ord('9'):
                raise TypeError