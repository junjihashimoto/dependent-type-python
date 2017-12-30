from mytyping import TypeVar,TypeNumVar,List,Tuple,NewType,Matrix

S = TypeVar('S')
T = TypeVar('T')
L = List[int]
L2 = List[1]
T2 = Tuple[True,int]

Z = NewType('Z',int)
S1 = Tuple[int,Z]
S2 = Tuple[int,Tuple[int,Z]]
M1 = Tuple[int,2,2]


def vec2(x: T, y: T) -> List[T]:
    return [x, y]

def vec3(x: List[T]) -> List[T]:
    return x

def vec4(x: T, y: T) -> List[1]:
    return vec3(vec2(x,y))

v:Tuple[int,2,2] = [[1,2],[1,2]]

def val(x:Tuple[int,2,2]) -> Tuple[int,2,2]:
    return [[1,2],[1,2]]

N = TypeNumVar('N')
M = TypeNumVar('M')
L = TypeVar('L')


def matmul(x: Tuple[int,N,M], y: Tuple[int,M,L]) -> Tuple[int,N,L]:
    return [[1,2],[1,2]]

def flatten(x: Tuple[int,N,M]) -> Tuple[int,1,N*M]:
    return [[1,2,1,2]]

print(L)
print(L2)
print(T2)
print(M1)
print(Tuple[int,1,N*M])
print(matmul(v,v))
print(type(flatten(v)))
