from Functions import *
from Operators import *

class Constraint:
	def __init__(self, operator):
		self.operator = operator
	def call(self,  x):
		return self.operator(x)

class MoreThan(Constraint):
	def __init__(self, value):
		super().__init__(morethan(value))

class LessThan(Constraint):
	def __init__(self, value):
		super().__init__(lessthan(value))

class EqualTo(Constraint):
	def __init__(self, value):
		super().__init__(equalto(value))

class Within(Constraint):
	def __init__(self, domain):
		super().__init__(within(domain))

class DomainConstraint:
	def __init__(self, inclusive_domain=[], exclusive_domain=[]):
		self.positive = inclusive_domain
		self.negative = exclusive_domain
	def call(self, x):
		y = inclusion_state(x, self.positive)
		y += exclusion_state(x, self.negative)
		return y / 2

class RangeConstraint:
	def __init__(self, l, u):
		self.bounds = [l, u]
	def call(self, x):
		return inbound(x, self.bounds)
