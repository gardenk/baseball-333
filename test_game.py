from unittest import TestCase

from game import Game
from game_result import GameResult


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_matched_number(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_ball())

    def assert_invalid_argument(self, guessNum):
        try:
            self.game.guess(guessNum)
            self.fail()
        except TypeError:
            pass

    def test_exception_invalid_input(self):
        self.assert_invalid_argument(None)
        self.assert_invalid_argument("12")
        self.assert_invalid_argument("1234")
        self.assert_invalid_argument("12s")
        self.assert_invalid_argument("121")

    def generate_question(self, question_num):
        self.game.question = "123"

    def test_solve_result_if_matched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("123"), True, 3, 0)

    def test_solve_result_if_unmatched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("456"), False, 0, 0)
