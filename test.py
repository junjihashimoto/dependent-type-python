from mytyping import *

S = TypeVar('S')
T = TypeVar('T')
L = List[int]
L2 = List[1]
T2 = Tuple[True,int]

Z = NewType('Z',int)
MS1 = Matrix[int,2,2]
S1 = Tuple[int,Z]
S2 = Tuple[int,Tuple[int,Z]]
M1 = Tuple[int,2,2]


def vec2(x: T, y: T) -> List[T]:
    return [x, y]

def vec3(x: List[T]) -> List[T]:
    return x

def vec4(x: T, y: T) -> List[T]:
    return vec3(vec2(x,y))

v: Tuple[int,2,2] = [[1,2],[1,2]]

def val(x:Tuple[int,2,2]) -> Tuple[int,2,2]:
    return [[1,2],[1,2]]

N = TypeNumVar('N')
M = TypeNumVar('M')
P = TypeNumVar('P')
L = TypeVar('L')


def matmul(x: Tuple[int,N,M], y: Tuple[int,M,L]) -> Tuple[int,N,L]:
    return [[1,2],[1,2]]

def flatten(x: Matrix[int,N,M]) -> Matrix[int,1,N*M]:
    return [[1,2,1,2]]

def flatten(x: Tensor[int,N,M,P]) -> Tensor[int,1,N*M*P]:
    return [[[1,2,1,2]]]

print(L)
print(L2)
print(T2)
print(M1)
print(Tuple[int,1,N*M])
print(matmul(v,v))
print(type(flatten(v)))
#print(reveal_type(flatten(v)))
