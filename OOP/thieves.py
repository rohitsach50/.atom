# import numpy as np
# import matplotlib.pylab as plt
# from numpy import random
#
# list1 = [1, 2, 3, 4, 5, 6]
# np_arr_1 = np.array(list1, dtype=np.int8)
#
# # print(np.linspace(1, 10, 2))
# # print(np_arr_1.size)
# print(np?)

######################################################################

# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#
#
# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first+second
# print(result.x)
# print(result.y)
######################################################################
# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __xor__(self, other):
#         line = "="*len(other.cont)
#         return "\n".join([self.cont, line, other.cont])
#
#
# spam = SpecialString("spam")
# hello = SpecialString("hello wolrd!")
# print(spam ^ hello)
import random
from characters import Character
from attributes import Agile, Sneaky


class Thief(Character, Agile, Sneaky):

    def pickpocketO(self):
        return self.sneaky and bool(random.randint(0, 1))


rock = Thief("rock", scar=None, weapon="wit")
jack = Thief("jack")
rock.sneaky = False
print(rock.sneaky)
print(jack.name)
