class A:
    def __init__(self):
        self.x=1
        self.__y=1

        def getY(self):
            return self.__y

a = A()
print(a.x)
# 정상적으로 1을 출력한다. private이 아니기 때문
