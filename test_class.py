import pytest
from bowling_game import BowlingGame

@pytest.fixture
def game():
	return BowlingGame()

class TestClass:

	def roll_same_value_n_times(self, game, value, n):
		for _ in range(n):
			game.roll(value)

	def test_game_w_all_zeros(self, game):
		self.roll_same_value_n_times(game, value=0, n=20)
		assert game.score() == 0

	def test_game_w_all_ones(self, game):
		self.roll_same_value_n_times(game, value=1, n=20)
		assert game.score() == 20

	def test_w_one_spare(self, game):
		game.roll(3)
		game.roll(7)
		game.roll(3)
		game.roll(1)
		self.roll_same_value_n_times(game, value=0, n=16)
		assert game.score() == 17

	def test_w_two_spares(self, game):
		game.roll(3)
		game.roll(7)
		game.roll(5)
		game.roll(5)
		game.roll(1)
		game.roll(3)
		self.roll_same_value_n_times(game, value=0, n=16)
		assert game.score() == 30

	def test_w_two_strikes(self, game):
		game.roll(10)
		game.roll(10)
		game.roll(1)
		game.roll(3)
		self.roll_same_value_n_times(game, value=0, n=14)
		assert game.score() == 39

	def test_w_spare_in_the_end(self, game):
		self.roll_same_value_n_times(game, value=0, n=2*9)
		game.roll(4)
		game.roll(4)
		game.roll(7)
		game.roll(3)
		game.roll(3)
		game.roll(2)
		assert game.score() == 26

	def test_w_strike_in_the_end(self, game):
		self.roll_same_value_n_times(game, value=0, n=2*9)
		game.roll(10)
		game.roll(10)
		game.roll(10)
		assert game.score() == 60
