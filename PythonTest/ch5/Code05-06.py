from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
# def myFunc() :
#     messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")
def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("다이얼로그 제목창입니다.", "체크버튼 해제")
    else :
        messagebox.showinfo("다이얼로그 제목창입니다.", "체크버튼 선택")

def myFunc2() :
    if var.get() == 1 :
        resultLabel.configure(text="라디오 버튼1 var 값 : %d" %(var.get()))
    elif var.get() == 2 :
        resultLabel.configure(text="라디오 버튼2 var 값 : %d" %(var.get()))
    else :
        resultLabel.configure(text="라디오 버튼3 var 값 : %d" %(var.get()))

## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file = "PythonTest/gif1/dog10.gif")
button = Button(window, image = photo, command = myFunc)
button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)
button2 = Button(window, text = "파이썬 종료", fg = "red", command = quit)

button.pack()
button1.pack(side=TOP, fill=X, padx = 10, pady = 10)
button2.pack(side=TOP, fill=X, ipadx = 10, ipady = 10)

chk = IntVar()
ch1 = Checkbutton(window, text = "체크해주세요", variable=chk, command=myFunc)
ch1.pack()

var = IntVar()
rb1 = Radiobutton(window, text="라디오 버튼1", variable=var,value=1, command=myFunc2)
rb2 = Radiobutton(window, text="라디오 버튼2", variable=var,value=2, command=myFunc2)
rb3 = Radiobutton(window, text="라디오 버튼3", variable=var,value=3, command=myFunc2)

resultLabel = Label(window, text="선택한 라디오 버튼 : ",fg="red")

rb1.pack(side=TOP, fill=X, padx = 10, pady = 10)
rb2.pack(side=TOP, fill=X, padx = 10, pady = 10)
rb3.pack(side=TOP, fill=X, padx = 10, pady = 10)
resultLabel.pack()

window.mainloop()
