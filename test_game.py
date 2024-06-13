from unittest import TestCase

from game import Game
from game_result import GameResult


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

    def test_solve_result_if_matched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strikes())
        self.assertEqual(0, result.get_ball())

    def test_solve_result_if_unmatched_number(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("456")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(0, result.get_strikes())
        self.assertEqual(0, result.get_ball())
