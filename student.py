class student:
    name
    def __(self,age, grade):
        self.age = age
        self.grade = grade
    def put(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
object = student()
object.get(18, "A")
object.name = "Rudra"
object.put()