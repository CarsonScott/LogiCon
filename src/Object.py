import Relation as rel
import Constraint as con 

class Object:

	def __len__(self): 
		return len(self.slots)
		
	def __getitem__(self, index):
		return self.slots[index]

	def __setitem__(self, index, value):
		self.slots[index] = value

	def set_slot(self, index, value):
		self.slots[index] = value

	def set_constraint_weights(self, index, weights):
		self.constraint_weights[index] = weights

	def set_slot_weights(self, weights):
		self.slot_weights = weights

	def set_relation_weights(self, weights):
		self.relations_weights = weights

	def set_criterion(self, slot_criterion, relation_criterion):
		self.slot_criterion = slot_criterion
		self.relation_criterion = relation_criterion
	
	def set_thresholds(self, thresholds):
		self.thresholds = thresholds

	def __init__(self, slots):
		self.relation_state = 0
		self.slots = []
		self.pairs = []
		self.relations = []
		self.slot_state = 0
		self.thresholds = []
		self.constraints = []
		self.slot_outputs = []
		self.slot_weights = []
		self.slot_criterion = 1
		self.relation_thresh = 1
		self.relation_indices = []
		self.relation_weights = []
		self.relation_outputs = []
		self.relation_criterion = 1
		self.constraint_weights = []
		self.constraint_indices = []
		self.constraint_outputs = []
		for i in range(slots):
			self.constraint_outputs.append([])
			self.constraint_indices.append([])
			self.constraint_weights.append([])
			self.slot_weights.append(1)
			self.slot_outputs.append(0)
			self.constraints.append([])
			self.thresholds.append(1)
			self.slots.append(0)
	
	def create_constraint(self, index, element, constraint, weight=1.0):
		self.constraint_indices[index].append(element)
		self.constraints[index].append(constraint)
		self.constraint_weights[index].append(weight)
	
	def create_relation(self, indices, elements, relation, weight=1.0):
		self.relation_indices.append(elements)
		self.relation_weights.append(weight)
		self.relations.append(relation)
		self.pairs.append(indices)	

	def apply_constraint(self, element, constraint, weight=1.0):
		for i in range(len(self.slots)):
			self.create_constraint(i, element, constraint, weight)

	def compute_slot_output(self, i):
		y = 0
		for j in range(len(self.constraints[i])):
			x = self.slots[i][self.constraint_indices[i][j]]
			y += self.constraints[i][j].call(x)*self.constraint_weights[i][j]
		return y

	def compute_slot_state(self):
		y = 0
		for i in range(len(self.slots)):
			x = self.compute_slot_output(i)
			y += int(x/len(self.constraints[i]) >= self.thresholds[i])*self.slot_weights[i]
		return y

	def compute_relation_state(self):
		y = 0
		for i in range(len(self.pairs)):
			a = self.slots[self.pairs[i][0]][self.relation_indices[i][0]]
			b = self.slots[self.pairs[i][1]][self.relation_indices[i][1]]
			y += self.relations[i].call(a, b)*self.relation_weights[i]
		return y

	def update_slot_state(self):
		x = self.compute_slot_state()
		self.slot_state = int(x/len(self.slots) >= self.slot_criterion)
	
	def update_relation_state(self):
		x = self.compute_slot_state()
		self.relation_state = int(x/len(self.relations) >= self.relation_criterion)

	def update(self):
		self.update_slot_state()
		self.update_relation_state()
	
	def validity(self):
		return self.slot_state and self.relation_state
