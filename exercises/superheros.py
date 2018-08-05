# Write your solutions for 1.5 here!
class superhero():
	"""docstring forgsuperheo"""
	def __init__(self,name,nickname,superpower,strength):
		self.name = name
		self.nickname=nickname
		self.superpower=superpower
		self.strength=strength
	def safe_civillian(self,x):
		if self.strength> x:
			print("civillian saved")
			self.strength-=x
		elif self.strength<=x:
			print("the hero isn't strong enough")
	def workout(self,time):
		self.strength*=time
		print("hero is now stronger")
		print(self.strength)
goku=superhero("goku","goku","tons of stuff",9100)
goku.safe_civillian(800)
goku.workout(8)