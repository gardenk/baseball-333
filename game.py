class Game:
    def guess(self, num):
        self.assert_invalid_value(num)

    def assert_invalid_value(self, num):
        if num is None or len(num) != 3:
            raise TypeError
        for N in num:
            if not ord('0') <= ord(N) <= ord('9'):
                raise TypeError
        if len(set(list(num))) < 3:
            raise TypeError