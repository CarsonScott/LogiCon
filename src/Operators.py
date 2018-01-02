class Operator:
	def call(self, x):
		return True
		
class VariableOperator(Operator):
	def __init__(self, data=None):
		self.data = data


class equalto(VariableOperator):
	def __call__(self, x):
		return x == self.data

class lessthan(VariableOperator):
	def __call__(self, x):
		return x < self.data

class morethan(VariableOperator):
	def __call__(self, x):
		return x > self.data

class SetOperator(VariableOperator):
	def __init__(self, data=[]):
		self.data = data
		
class within(SetOperator):
	def __call__(self, x):
		return x in self.data