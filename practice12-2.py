# 실행에러
def main():
    mycount = Count()
    times = 0

    for i in range(0,100):
        increment(mycount,times)

    print("mycount.count=",mycount.count, ",times=",times)


def increment(c,times):

    c.count += 1
    times += 1


class Count:
    def __init__(self):
        self.count = 0

main()


