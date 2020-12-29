import sys


class A:
    friend = None


a1 = A()
a2 = A()
a3 = A()
a4 = A()
print("1:", sys.getrefcount(a2))
a1.friend = a2
print("2:", sys.getrefcount(a2))

print(a2)
print("3:", sys.getrefcount(a2))
print(a1.friend)
del a2

# print(a1.friend, sys.getrefcount(a1.friend))

# print(a1.friend)

# printf() -> sys.getrefcount() 내에서 a2 가 가리키던 객체의 레퍼런스 카운트 증가
print("4:", sys.getrefcount(a1.friend))

del a1.friend

print(a1.friend) # NOT deleted
