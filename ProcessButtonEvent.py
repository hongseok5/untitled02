from tkinter import * #

def processOK():
    print("OK 버튼이 클릭되었습니다.")
def processCancel():
    print("캔슬버튼이 클릭되었습니다.")

window = Tk()
btOK = Button(window, text="OK", fg="red", command = processOK)
btCancel = Button(window, text="Cancel", bg ="Yellow", command=processCancel)

btOK.pack()
btCancel.pack()

window.mainloop()