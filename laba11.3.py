class Matrix:
    __CodeError = 0
    __num_matrix = 3

    def __init__(self, n=0, m=0, number=0):
        self.__IntArray = []
        self.__n = n
        self.__m = m
        if number == 0 and n == 0 and m == 0:
            self.__IntArray.append(0)
        else:
            for i in range(self.__n):
                self.__IntArray.append([])
                for j in range(self.__m):
                    self.__IntArray[i].append(number)

    def __del__(self):
        print("Дескруктор включений")

    def Input(self):
        print("Введення нових значень у матрицю")
        for i in range(self.__n):
            for j in range(self.__m):
                self.__IntArray[i][j] = int(input())

    def Output(self):
        print("Матриця")
        for i in range(self.__n):
            for j in range(self.__m):
                print(self.__IntArray[i][j], end=" ")
            print()
        print("----------------")

    def Parametr(self, par):
        for i in range(self.__n):
            for j in range(self.__m):
                self.__IntArray[i][j] = par

    @staticmethod
    def Count():
        print(Matrix.__num_matrix)

    @property
    def GetSize(self):
        return self.__n, self.__m

    @property
    def CodeError(self):
        if self.__CodeError == -1:
            return 0

    @CodeError.setter
    def CodeError(self, value):
        self.__CodeError = value

    def __getitem__(self, tup):
        if len(str(tup)) == 1:
            for i in range(self.__n):
                for j in range(self.__m):
                    if tup == i * self.__m + j:
                        return self.__IntArray[i][j] - 1
        elif len(tup) == 2:
            x, y = tup
            for i in range(self.__n):
                for j in range(self.__m):
                    if x == i and y == j:
                        return self.__IntArray[i][j]
        self.__CodeError = -1
        return self.__CodeError

    def __iadd__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                self.__IntArray[i][j] += 1
        return self

    def __isub__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                self.__IntArray[i][j] -= 1
        return self

    def __bool__(self):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] == 0:
                    return False
        if self.__m != 0 and self.__n != 0:
            return True
        return False

    def __neg__(self):
        return self.__n != 0 and self.__m != 0

    def __invert__(self):
        for i in range(self.__n):
            for j in range(self.__m):
                self.__IntArray[i][j] = ~self.__IntArray[i][j]

    def __add__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] += other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] += other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] -= other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] -= other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] *= other
        elif self.__m == other.__n:
            s = 0
            t = []
            m = []
            for k in range(self.__n):
                for i in range(other.__m):
                    for j in range(self.__m):
                        s += self.__IntArray[k][j] * other.__IntArray[j][i]
                    t.append(s)
                    s = 0
                m.append(t)
                t = []
            return m
        else:
            return "Масиви різні за розміром"

    def __truediv__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] /= other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] /= other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __mod__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] %= other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] %= other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __or__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] | other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = int(self.__IntArray[i][j]) | other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __and__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] & other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = int(self.__IntArray[i][j]) & other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __xor__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] ^ other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = int(self.__IntArray[i][j]) ^ other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __rshift__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] >> other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] >> other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __lshift__(self, other):
        if isinstance(other, int):
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] << other
        elif self.__n == other.__n and self.__m == other.__m:
            for i in range(self.__n):
                for j in range(self.__m):
                    self.__IntArray[i][j] = self.__IntArray[i][j] << other.__IntArray[i][j]
        else:
            print("Масиви різні за розміром")
        return self

    def __eq__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] == other.__IntArray[i][j]:
                    return True
        return False

    def __ne__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] != other.__IntArray[i][j]:
                    return True
        return False

    def __gt__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] > other.__IntArray[i][j]:
                    return True
        return False

    def __ge__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] >= other.__IntArray[i][j]:
                    return True
        return False

    def __lt__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] < other.__IntArray[i][j]:
                    return True
        return False

    def __le__(self, other):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__IntArray[i][j] <= other.__IntArray[i][j]:
                    return True
        return False


A = Matrix(3, 3, 4)
A.Parametr(1)
A.Output()
A.Input()
A.Output()
print("Розмірність матриці: ", A.GetSize)
print("Елемент масиву ", A[1, 2])
A += 1
A.Output()
A -= 1
A.Output()
if A:
    print("Розміри матриці не дорівнюють 0 і немає елементів з нулями")
else:
    print("Є елементи з нулями або розміри матриці рівні 0")
if -A:
    print("Розміри матриці не дорівнюють 0")
else:
    print("Розміри матриці рівні 0")
~A
print("Інвертована матриця")
A.Output()
B = Matrix(3, 3, 3)
print("Друга матриця")
B.Output()
print("Додавання матриць")
A + B
A.Output()
print("Віднімання матриць")
A - B
A.Output()
x = A * B
print("Множення матриць")
for i in x:
    print(i)
print("Ділення матриць")
A / 2
A.Output()
A % 2
print("Ділення з остачею")
A.Output()
A | B
print("Побітове додавання")
A.Output()
A & 2
print("Побітове множення")
A.Output()
A ^ B
print("Додавання за модулем 2")
A.Output()
A << 5
print("Побітове зміщення вправо")
A.Output()
B.Output()
if A[1,2] == B[1,2]:
    print("Рівні")
else:
    print("Не рівні")
if A[1,1] > B[1,1]:
    print("Перший елемент більший за другий")
elif A[1,1] < B[1,1]:
    print("Перший елемент менший за другий")
else:
    print("Елементи рівні")