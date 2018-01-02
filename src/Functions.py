def more(a, b):
	return a > b

def less(a, b):
	return a < b

def equal(a, b):
	return a == b

def equal_or_more(a, b):
	return more(a, b) or equal(a, b)

def equal_or_less(a, b):
	return less(a, b) or equal(a, b)

def difference(a, b):
	return a-b
	
def distance(a, b):
	return abs(a-b)

def within(x, d):
	return x in d

def inbound(x, r):
	if r[0] != None:
		if not equal_or_more(x, r[0]):
			return False
	if r[1] != None:
		 if not equal_or_less(x, r[1]):
		 	return False
	return True

def inbound_positive_offset(a, b, r):
	return more(a, b) and inbound(difference(a, b), r)

def inbound_negative_offset(a, b, r):
	return less(a, b) and inbound(difference(a, b), r)

def inbound_absolute_offset(a, b, r):
	return inbound(distance(a, b), r)

def inclusion_state(x, S):
	if x in S:return 1
	return -1
def exclusion_state(x, S):
	if x not in S:return 1
	return -1