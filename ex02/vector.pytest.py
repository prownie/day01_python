class Vector:

    def __init__(self, val):
        self.values = []
        if isinstance(val, int):
            if val >= 0:
                i = 0
                while i < val:
                    self.values.append(float(i))
                    i += 1
        if isinstance(val, list):
            for i in val:
                if not isinstance(i, int) and not isinstance(i, float):
                    exit("Only accepts ints and floats")
                self.values.append(float(i))
        if isinstance(values, tuple):
            if (len(val) != 2 or (type(val[0]) != int and type(val[0]) != float)
               or (type(val[1]) != int and type(val[1]) != float)):
                exit("Only accepts range with 2 int or floats, with nb1 < nb2")
            i = val[0]
            while int(i) < int(val[1]):
                self.values.append(float[i])
                i += 1

vec = []
print(type(vec)) 
