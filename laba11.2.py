class VectorInt:
    __codeError = 0
    __num_vec = 2

    def __init__(self, size=0, number=0):
        self.__IntArray = []
        self.__size = size
        if number == 0 and size == 0:
            self.__IntArray.append(0)

        else:
            for i in range(self.__size):
                self.__IntArray.append(int(number))

    def __del__(self):
        print("Дескруктор включений")

    def Input(self):
        print("Введення нових значень у вектор")
        for i in range(self.__size):
            self.__IntArray[i] = int(input())

    def Output(self):
        print(self.__IntArray)

    def Parametr(self, value):
        for i in range(self.__size):
            self.__IntArray[i] = value

    @staticmethod
    def Count():
        print("Кількість масивів: ", VectorInt.__num_vec)

    @property
    def GetSize(self):
        return self.__size

    @property
    def CodeError(self):
        if self.__codeError == -1:
            return 0

    @CodeError.setter
    def CodeError(self, value):
        self.__codeError = value

    def __getitem__(self, item):
        for i in range(self.__size):
            if item == i:
                return self.__IntArray[i]
        self.__codeError = -1

    def __iadd__(self, other):
        for i in range(self.__size):
            self.__IntArray[i] += 1
        return self

    def __isub__(self, other):
        for i in range(self.__size):
            self.__IntArray[i] -= 1
        return self

    def __neg__(self):
        return self.__size != 0

    def __bool__(self):
        return self.__size == 0

    def __invert__(self):
        for i in range(self.__size):
            self.__IntArray[i] = ~self.__IntArray[i]

    def __add__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] += other
        else:
            for i in range(self.__size):
                self.__IntArray[i] += other.__IntArray[i]
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] -= other
        else:
            for i in range(self.__size):
                self.__IntArray[i] -= other.__IntArray[i]
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] *= other
        else:
            for i in range(self.__size):
                self.__IntArray[i] *= other.__IntArray[i]
        return self

    def __truediv__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] /= other
        else:
            for i in range(self.__size):
                self.__IntArray[i] /= other.__IntArray[i]
        return self

    def __mod__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] %= other
        else:
            for i in range(self.__size):
                self.__IntArray[i] %= other.__IntArray[i]
        return self

    def __or__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) | other
        else:
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) | other.__IntArray[i]
        return self

    def __and__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) & other
        else:
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) & other.__IntArray[i]
        return self

    def __xor__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) ^ other
        else:
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) ^ other.__IntArray[i]
        return self

    def __rshift__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) >> other
        else:
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) >> other.__IntArray[i]
        return self

    def __lshift__(self, other):
        if isinstance(other, int):
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) << other
        else:
            for i in range(self.__size):
                self.__IntArray[i] = int(self.__IntArray[i]) << other.__IntArray[i]
        return self

    def __eq__(self, other):
        for i in range(self.__size):
            if self.__IntArray[i] == other.__IntArray[i]:
                return True
        return False

    def __ne__(self, other):
        for i in range(self.__size):
            if self.__IntArray[i] != other.__IntArray[i]:
                return True
        return False

    def __gt__(self, other):
        for i in range(self.__size):
            if self.__IntArray[i] > other.__IntArray[i]:
                return True
        return False

    def __ge__(self, other):
        for i in range(self.__size):
            if self.__IntArray[i] >= other.__IntArray[i]:
                return True
        return False

    def __lt__(self, other):
        for i in range(self.__size):
            if self.__IntArray[i] < other.__IntArray[i]:
                return True
        return False

    def __le__(self, other):
        for i in range(self.__size):
            if self.__IntArray[i] <= other.__IntArray[i]:
                return True
        return False


vec = VectorInt(3, 2)
vec.Output()
vec.Input()
vec.Output()
# vec.Parametr(3)
vec.Output()
vec.CodeError = "fdfdfd"
# print(vec[3])
print(vec.CodeError)
vec += 1
vec.Output()
var = ~vec
vec.Output()
vec2 = VectorInt(3, 2)
VectorInt.Count()
# vec + vec2
vec + 2
vec.Output()
vec - vec2
vec.Output()
vec / 2
vec.Output()
vec * vec2
vec.Output()
vec % 2
vec.Output()
vec3 = vec | vec2
vec3.Output()
vec & 2
vec.Output()
if vec[2] == vec2[2]:
    print("Є спільна пара елементів")
elif vec[2] != vec2[2]:
    print("Немає спільної пари")
if vec[1] > vec2[1]:
    print(f"{vec[1]} > {vec2[1]}")
elif vec[1] >= vec2[1] or vec[1] <= vec2[1]:
    print(f"{vec[1]} == {vec2[1]}")
elif vec[1] < vec2[1]:
    print(f"{vec[1]} < {vec[1]}")
