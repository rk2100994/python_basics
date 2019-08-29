class Edureka:
	domain = ("Data science")
	def setCourse(self, name):
		self.name = name
# instances declaration
ob1 = Edureka()
ob2 = Edureka()

ob1.setCourse("Python")
ob2.setCourse("Machine Learning")

print(ob1.domain)
print(ob1.name)
print(ob2.name)
ob1.domain = "GOD"
print(ob1.domain)
print(ob2.domain)

