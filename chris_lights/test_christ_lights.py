import pytest

from chris_lights import LightSequence

class TestLightSequence:
	@pytest.mark.parametrize("num_lights,begin_index,end_index,num_on",
													 [(10, 3, 5, 3),
														(20, 7, 15, 9),
														(12, 3, 7, 5)])
	def test_toggle_single_range_parametrized(self, num_lights, begin_index, end_index, num_on):
		ls = LightSequence(num_lights)
		ls.toggle(begin_index, end_index)
		assert ls.num_on() == num_on
