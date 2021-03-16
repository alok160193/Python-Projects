# *********************PROJECT-3 VECTOR OPERATIONS************************
# To find addition,substraction,dot & cross product of any no. of vectors.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str = " "
        index = 0
        for i in self.vec:
            str += f"{i}a{index}+"
            index += 1
        return str[:-1]

    # Addition
    
    def __add__(self, vec2):
        list = []
        for i in range(len(self.vec)):
            list.append(self.vec[i]+vec2.vec[i])
        return Vector(list)

    # Substraction

    def __sub__(self, vec2):
        list = []
        for i in range(len(self.vec)):
            list.append(self.vec[i]-vec2.vec[i])
        return Vector(list)

    # Dot Product

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i]*vec2.vec[i]
        return
    # Cross Product


v1 = Vector([2, 3])
v2 = Vector([3, 2])
print(v1+v2)
print(v1-v2)
print(v1*v2)
