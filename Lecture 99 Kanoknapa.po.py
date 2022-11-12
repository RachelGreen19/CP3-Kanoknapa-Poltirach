from tkinter import *
import math
def leftClickButton(event):
    result = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    print(result)
    lebelResult.configure(text=result)
    if result > 30.0:
        lebelResult2.configure(text="อ้วนมาก")
    elif result > 25.0 and result < 29.9:
        lebelResult2.configure(text="อ้วน")
    elif result > 23.0 and result < 24.9:
        lebelResult2.configure(text="น้ำหนักเกิน")
    elif result > 18.6 and result < 22.9:
        lebelResult2.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        lebelResult2.configure(text="ผอมเกินไป")

MainWindow = Tk()
lebelHeight = Label(MainWindow,text="ส่วนสูง (cm.)").grid(row=0,column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0,column=1)

lebelWeight = Label(MainWindow,text="น้ำหนัก (kg.)").grid(row=1,column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

lebelResult = Label(MainWindow,text="ผลลัพท์")
lebelResult.grid(row=2,column=1)
lebelResult2 = Label(MainWindow)
lebelResult2.grid(row=3,column=1)

MainWindow.mainloop()