x = 1
y = -1
z = 1


if x > 0:
    if y > 0:
        print("1번문장")
elif z > 0:
    print("2번문장")

number = 1
even = number % 2 == 0
print(even)

if number % 2 == 0:
    even2 = True
else:
    even2 = False
print(even2)
import random
for i in range(1,20):
    a=random.randint(0,2)
    print(a)


x = 0

if  x<4 :

    x = x+1

print("x는",x,"입니다")

print("smith\\exam1\\test.txt")

number2 = 4
print(format(number2,"2d"))
print(format(number2**1.5,"4.2f"))

print(eval("1+3*2"))

test = input()

j,k = 1, 2
j,k = k,j
j,k = k,j

print(j,k)