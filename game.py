from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, num) -> GameResult:
        self.assert_invalid_value(num)
        if num == self.question:
            return GameResult(True, 3, 0)
        else:
            strikes = 0
            for i in range(len(self.question)):
                if self.question.find(num[i]) == i:
                    strikes += 1

            return GameResult(False, strikes, 0)

    def assert_invalid_value(self, num):
        if num is None or len(num) != 3:
            raise TypeError
        for N in num:
            if not ord('0') <= ord(N) <= ord('9'):
                raise TypeError
        if len(set(list(num))) < 3:
            raise TypeError