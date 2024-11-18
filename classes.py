from matplotlib import pyplot as plt

# class Student:
#     def __init__(self, name="John Doe", age=18):
#         self.name = name
#         self.age = age
#         self.currency = 0
#         self.year = 1
#         self.have_stipend = True
#         self.marks = []
#
#     def get_stipend(self):
#         if self.have_stipend:
#             self.currency += 5200
#
#     def check_term(self):
#         self.have_stipend = min(self.marks) >= 5
#         self.marks = []


# a = Student("Vera", 17)
# b = Student()
# print(a.currency)
# a.get_stipend()
# print(a.currency)
# print(b.currency)
# b.name = "Ivan"
# print(a.name)
# print(b.name)


# a = Student("Aleksei")
# for i in range(5):
#     a.get_stipend()
#
# a.marks.append(7)
# a.marks.append(9)
# a.marks.append(8)
# a.marks.append(7)
# a.check_term()
# for i in range(5):
#     a.get_stipend()
# print(a.currency)

class Ball:
    def __init__(self, m=1, x=10, y=10, v_x=0, v_y=0):
        self.m = m
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a_x = 0
        self.a_y = -10

    def move(self, dt, l=50):
        self.x += self.v_x * dt + self.a_x * dt ** 2 / 2
        self.y += self.v_y * dt + self.a_y * dt ** 2 / 2

        self.v_x += self.a_x * dt
        self.v_y += self.a_y * dt

        if self.x < 0:
            self.x = -self.x
            self.v_x = - self.v_x
        if self.x > l:
            self.x = 2 * l - self.x
            self.v_x = -self.v_x
        if self.y < 0:
            self.y = -self.y
            self.v_y = - self.v_y
        if self.y > l:
            self.y = 2 * l - self.y
            self.v_y = -self.v_y


X = []
Y = []
dt = 0.01

a = Ball(2, 10, 10, 5)

for i in range(2000):
    a.move(dt)
    X.append(a.x)
    Y.append(a.y)

plt.scatter(X, Y)
plt.show()
