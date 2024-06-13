from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def test_exception_invalid_input(self):
        self.assert_invalid_argument(None)
        self.assert_invalid_argument("12")
        self.assert_invalid_argument("1234")
        self.assert_invalid_argument("12s")
        self.assert_invalid_argument("121")

    def assert_invalid_argument(self, guessNum):
        try:
            self.game.guess(guessNum)
            self.fail()
        except TypeError:
            pass
