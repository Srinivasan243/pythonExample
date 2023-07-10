import numpy as np
class Numpy_Ex:
    def ex_method(self, data):
        grades = np.array(data)
        print('grade\n')
        print(grades)
        print(type(grades),'x2\n',grades*2)
        print('data\n')
        print(data)
        print(type(data),'x2\n',data*2)


data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
obj = Numpy_Ex()
obj.ex_method(data)
