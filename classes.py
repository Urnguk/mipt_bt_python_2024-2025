class Student:
    def __init__(self, name="John Doe", age=18):
        self.name = name
        self.age = age
        self.currency = 0
        self.year = 1
        self.have_stipend = True
        self.marks = []

    def get_stipend(self):
        if self.have_stipend:
            self.currency += 5200

    def check_term(self):
        self.have_stipend = min(self.marks) >= 5
        self.marks = []


# a = Student("Vera", 17)
# b = Student()
# print(a.currency)
# a.get_stipend()
# print(a.currency)
# print(b.currency)
# b.name = "Ivan"
# print(a.name)
# print(b.name)


a = Student("Aleksei")
for i in range(5):
    a.get_stipend()

a.marks.append(7)
a.marks.append(9)
a.marks.append(8)
a.marks.append(7)
a.check_term()
for i in range(5):
    a.get_stipend()
print(a.currency)



