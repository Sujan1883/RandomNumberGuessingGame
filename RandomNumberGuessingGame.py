from tkinter import *
import random
root=Tk()
root.title("Number Guessing Game")
root.geometry("600x400")
root.config(bg="white")
lower_bound=random.randint(0,50)
print("The Lower Bound Is",lower_bound)
upper_bound=random.randint(51,100)
print("The Upper Bound Is",upper_bound)
Num=random.randint(lower_bound,upper_bound)
chance=round(((upper_bound-lower_bound)/10))
print("Number Of Chances Are",chance)
var=IntVar()
disp=StringVar()
def check_guess():
 global Num
 global chance
 guess=var.get()
 if chance>0:
  if guess==Num:
   msg=f"You Won!{Num} Is The Right Answer"
  elif guess>Num:
   chance-=1
   msg=f"{guess} is greater.You Have {chance} attempts left after this."
  elif guess<Num:
   chance-=1
   msg=f"{guess} is smaller.You Have {chance} attempts left after this."
  else:
   msg="Something Went Wrong!"
 else:
  msg=f"You Lost!The Number Is {Num}."
 disp.set(msg)
Label(root,text="Number Guessing Game",font=("Arial",20),relief=SOLID,padx=10,pady=10,bg="Lightgreen").pack(pady=(10,0))
Label(root,text=("The Lower Bound Is",lower_bound),font=("Arial",18),bg="Lightblue").pack()
Label(root,text=("The Upper Bound Is",upper_bound),font=("Arial",18),bg="Lightblue").pack()
Label(root,text=("The Number Of Chances You Have Are",chance),font=("Arial",18),bg="Lightgreen").pack()
Entry(root,textvariable=var,font=("Arial",18)).pack(pady=(50,10))