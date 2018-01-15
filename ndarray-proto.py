from typing import *
N = IntVar('N')
M = IntVar('M')
N0 = IntVar('N0')
M0 = IntVar('M0')
N1 = IntVar('N1')
M1 = IntVar('M1')

T = TypeVar('T')
S = TypeVar('S', bound=Shape)
S0 = TypeVar('S0', bound=Shape)
S1 = TypeVar('S1', bound=Shape)
S2 = TypeVar('S2', bound=Shape)

class ndarray(Generic[T,S]):
    def __init__(self):
        pass

def add(a: ndarray[T,S],b: ndarray[T,S]) -> ndarray[T,S]:
    pass

def matmul(a: ndarray[T,Shape[N0,M0]],b: ndarray[T,Shape[N1,M1]]) -> ndarray[T,Shape[N0,M1]]:
    pass

def flatten(a: ndarray[T,Shape[N0,M0]]) -> ndarray[T,Shape[N0*M0]]:
    pass

def reshape(a: ndarray[T,Shape[N0*M0]]) -> ndarray[T,Shape[N0,M0]]:
    pass

a: ndarray  # just an array, shape and type are arbitrary
b: ndarray[float, Any]  # array of floats with an unknown (dynamic) shape
c: ndarray[Any, Shape[100, 100]]  # array of dynamic types with fixed shape (100, 100)
c: ndarray[float, Shape[100, 100]]
d: ndarray[float, Shape[N, M]]

s0: ndarray[float, Shape[3, 2]] = ndarray()
s1: ndarray[float, Shape[2, 3]] = ndarray()
s2: ndarray[float, Shape[3, 3]] = matmul(s0,s1)
