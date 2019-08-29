class Coursename:
	def __init__(self,course):
		self.course = course
	def setCourse(self,course):
		self.course = course.upper()
	def getCourse(self):
		return(self.course)

ob = Coursename("Python")
print(ob.getCourse())

ob.setCourse("Machine Learning")
print(ob.getCourse())


# ob = Coursename()
# ob.setCourse("Python")
# print(ob.getCourse())
# ob.setCourse("Machine Learning")
# print(ob.getCourse())