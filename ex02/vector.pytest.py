class Vector:

    def __init__(self, val):
        self.values = []
        if isinstance(val, int):
            if val < 0:
                exit("Error : Number is negative")
            else:
                i = 0
                while i < val:
                    self.values.append(float(i))
                    i += 1
        elif isinstance(val, list):
            for i in val:
                if not isinstance(i, int) and not isinstance(i, float):
                    exit("Only accepts ints and floats")
                self.values.append(float(i))
        elif isinstance(val, tuple):
            if (len(val) != 2 or (type(val[0]) != float)
               or (type(val[1]) != float)):
                exit("Only accepts range with 2 floats, with nb1 < nb2")
            i = val[0]
            while int(i) < int(val[1]):
                self.values.append(i)
                i += 1
        else:
            exit("Accepted format : Vector(float), Vector((float,float)),\
                 Vector(float_list)")

    def __add__(self, val):
        rep = []
        if isinstance(val, int) or isinstance(val, float):
            for i in self.values:
                rep.append(i + val)
            return(rep)
        elif (isinstance(val, Vector) and len(val.values) == len(self.values)):
            i = 0
            while i < len(val.values):
                rep.append(val.values[i] + self.values[i])
                i += 1
            return(rep)
        else:
            print("Can't add, different vector sizes")

    def __radd__(self, val):
        rep = []
        if isinstance(val, int) or isinstance(val, float):
            for i in self.values:
                rep.append(i + val)
            return(rep)
        elif (isinstance(val, Vector) and len(val.values) == len(self.values)):
            i = 0
            while i < len(val.values):
                rep.append(val.values[i] + self.values[i])
                i += 1
            return(rep)
        else:
            print("Can't add, different vector sizes")

    def __sub__(self, val):
        rep = []
        if isinstance(val, int) or isinstance(val, float):
            for i in self.values:
                rep.append(i - val)
            return(rep)
        elif (isinstance(val, Vector) and len(val.values) == len(self.values)):
            i = 0
            while i < len(val.values):
                rep.append(self.values[i] - val.values[i])
                i += 1
            return(rep)
        else:
            print("Can't substract, different vector sizes")

    def __rsub__(self, val):
        rep = []
        if isinstance(val, int) or isinstance(val, float):
            for i in self.values:
                rep.append(val - i)
            return(rep)
        elif (isinstance(val, Vector) and len(val.values) == len(self.values)):
            i = 0
            while i < len(val.values):
                rep.append(val.values[i] - self.values[i])
                i += 1
            return(rep)
        else:
            print("Can't substract, different vector sizes")

    def __truediv__(self, val):
        rep = []
        if (isinstance(val, int) or isinstance(val, float)) and int(val) != 0:
            for i in self.values:
                rep.append(i / val)
            return(rep)
        else:
            print("Can only divid vector by a scalar not null (int/float)")

    def __rtruediv__(self, val):
        rep = []
        if (isinstance(val, int) or isinstance(val, float)):
            for i in self.values:
                if i == 0:
                    print("Can't divide by 0")
                    return(0)
                rep.append(val / i)
            return(rep)
        else:
            print("Can only divid vector by a scalar not null (int/float)")

    def __mul__(self, val):
        rep = []
        if isinstance(val, int) or isinstance(val, float):
            for i in self.values:
                rep.append(i * val)
            return(rep)
        elif (isinstance(val, Vector) and len(val.values) == len(self.values)):
            i = 0
            rep = 0
            while i < len(self.values):
                rep += val.values[i] * self.values[i]
                i += 1
            return rep
        else:
            print("Can only multiply vector of the same size, or by a scalar")

    def __rmul__(self, val):
        rep = []
        if isinstance(val, int) or isinstance(val, float):
            for i in self.values:
                rep.append(i * val)
            return(rep)
        elif (isinstance(val, Vector) and len(val.values) == len(self.values)):
            i = 0
            rep = 0
            while i < len(self.values):
                rep += val.values[i] * self.values[i]
                i += 1
            return rep
        else:
            print("Can only multiply vector of the same size, or by a scalar")


vec1 = Vector([2.0, 1.0, 0.0, 5.0, 10])
vec2 = Vector((2.0, 7.0))
print(vec1.values)
print(5 * vec)
