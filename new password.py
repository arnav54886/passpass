
from tkinter import *
import random

root =Tk()
root.title("Password Generator")
root.geometry("400x400")

array_3d = [[["1","2","3","4","5","6","7","8","9","0"],["Head","Tails"],["A","B","C","D","E","F","G","H","I","J"]]]
label = Label(root)
def new_password() :
    random_no1 = random.randint(0,9)
    random_no2 = random.randint(0,1)
    random_no3 = random.randint(0,9)
    
    letter1 = str(array_3d[0][0][random_no1])
    letter2 = (array_3d[0][1][random_no2])
    letter3 = (array_3d[0][2][random_no3])
    label["text"] = letter1  + letter2 + letter3 
    
btn1 = Button(root,text ="New Password",command = new_password)
btn1.place(relx = 0.5 , rely = 0.5 ,anchor = CENTER)

label.place(relx = 0.5 , rely = 0.6 ,anchor = CENTER)





root.mainloop()