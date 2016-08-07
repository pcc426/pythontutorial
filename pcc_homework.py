some_var =5
if some_var > 10:
	print "some_var is totally bigger than 10"
elif some_var < 10:
	print "some_var is smaller than 10"
else:
	print "some_var is indded 10"

for animal in ["dog", "cat", "mouse"]:
	print "%s is a animal" % animal

for i in range(4):
	print i

x = 0 
while x < 4:
	print x 
	x += 1

try:
	raise IndexError("This is an index error")
except IndexError, e:
	pass

def add(x,y):
	print "x is %s and y is %s" % (x, y)
	return x + y

print add(y=6, x=5)

def varargs(*args):
	return args

print varargs(1,3,4)

def keyword_args(**kwargs):
	return kwargs

print keyword_args(big="foot", loch="ness")

def all_the_args(*args, **kwargs):
	print args
	print kwargs

print all_the_args(1, 2, a=3, b=4)

args = (1,2,3,4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)
all_the_args(**kwargs)

def create_adder(x):
	def adder(y):
		return x + y
	return adder
add_10 = create_adder(10)
print add_10(3)

(lambda x:x > 2)(3)

print map(add_10, [1,2,3])
print filter(lambda x: x > 5, [3,4,5,6,7])

class Human(object):
	"""docstring for Human"""
	species = "H. sapiens"
	def __init__(self, name):
		super(Human, self).__init__()
		self.name = name

	def say(self, msg):
		return "%s: %s" % (self.name, msg)

	@classmethod	
	def get_species(cls):
		return cls.species

	@staticmethod
	def grunt():
		return "*grunt*"


i = Human(name="Ian")
print i.say("hi there")

j = Human(name="James")
print j.say("Hello world")

print i.get_species()

Human.species = "H. neverthelessiss"
print i.get_species()
print j.get_species()

print Human.grunt()

import math
print math.sqrt(16)

from math import ceil, floor
print ceil(3.7)
print floor(3.7)

import math as m
print math.sqrt(16) == m.sqrt(16)

import math 
print dir(math)


