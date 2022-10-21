def funcion(x,y):
    return x + 1/5 * y

import matplotlib.pyplot as math
def MetodoEuler(abs, y, func, h):
    ord = list()
    ord.append(y)
    MetodoEuler2(abs[0], y, func, h, abs[0], abs[len(abs) - 1], ord)
    return ord

def MetodoEuler2(x,y, func,h, menor, mayor, ord):
    if x < menor or x >= mayor: return y
    b = y + h*func(x,y)
    ord.append(b)
    return MetodoEuler2(x+1,b,func,h, menor, mayor, ord)


def EulerMethod( x, y, f, h, menor, mayor):
    if x < menor or x >= mayor: return y
    b = y + h*f(x ,y)
    return EulerMethod(x+h, b, f, h, menor, mayor)

abs = list()
ord = list()
for i in range(6):
    abs.append(i)
ord = MetodoEuler(abs, -3, funcion, 1)
math.plot(abs, ord)
math.show()

abs = list()
ord = list()
for i in range(5):
    abs.append(i)
    ord.append(funcion())




    