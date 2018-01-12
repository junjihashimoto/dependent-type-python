from typing import *
N = IntVar('N')
M = IntVar('M')

T = TypeVar('T')
S = TypeVar('S', bound=Shape)
S0 = TypeVar('S0', bound=Shape)
S1 = TypeVar('S1', bound=Shape)

class ndarray(Generic[T,S]):
    def __init__(self):
        pass

class MatMul(Generic[S0,S1]): # This is type level function. It returns fixed shape(a,d) of a result of mutrix multiply(S0(a,b) x S1(c,d)).
    pass

def add(a: ndarray[T,S],b: ndarray[T,S]) -> ndarray[T,S]:
    pass

def matmul(a: ndarray[T,S0],b: ndarray[T,S1]) -> ndarray[T,MatMul[S0,S1]]:
    pass
    
a: ndarray  # just an array, shape and type are arbitrary
b: ndarray[float, Any]  # array of floats with an unknown (dynamic) shape
c: ndarray[Any, Shape[100, 100]]  # array of dynamic types with fixed shape (100, 100)
c: ndarray[float, Shape[100, 100]]
d: ndarray[float, Shape[N, M]]

s0: ndarray[float, Shape[3, 2]] = ndarray()
s1: ndarray[float, Shape[2, 3]] = ndarray()
s2: ndarray[float, Shape[3, 3]] = matmul(s0,s1)
