from Functions import *

class EqualTo:
	def call(self, a, b):
		return a == b

class MoreThan:
	def call(self, a, b):
		return a > b

class LessThan:
	def call(self, a, b):
		return a < b