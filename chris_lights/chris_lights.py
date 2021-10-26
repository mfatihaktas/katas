
"""
Because your neighbors keep defeating you in the holiday house decorating contest year after year,
you’ve decided to deploy one million lights in a 1000x1000 grid. Furthermore, because you’ve been
especially nice this year, Santa has mailed you instructions on how to display the ideal lighting
configuration.Lights in your grid are numbered from 0 to 999 in each direction; the lights at each
corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off,
or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite
corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights
in a 3x3 square. The lights all start turned off. To defeat your neighbors this year, all you have to
do is set up your lights by doing the instructions Santa sent you in order.

Examples
turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on,
and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

Note: Let's first do the first dimensional version of this problem.
Goal is to find the number of lights turned on at the end.
"""

from debug_utils import *

class LightSequence:
	def __init__(self, num_lights):
		self.num_lights = num_lights
		check(num_lights > 0)

		## All lights are off at the beginning
		self.light_list = [0] * num_lights

	def toggle(self, begin_index, end_index):
		check(begin_index > 0 and end_index < self.num_lights)
		for i in range(begin_index, end_index + 1):
			self.light_list[i] = (self.light_list[i] + 1) % 2

	def num_on(self):
		return sum(self.light_list)
