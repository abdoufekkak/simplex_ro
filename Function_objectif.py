from tkinter import *


def RETURN_FUNCTION_OBJECIF(N_VARIABLE,root,Z,frame2,cmb):#nombre of var,page ,fct obje,injecté z array,combobox :min/max
 
 l1 = Label(frame2, text =cmb.get(),font=('Times',10,'bold'))#get valeur de combobox max/min et l'injecter dans label
 l1.grid(row =0, column = 0, sticky = W, pady = 20)
       

 for i in range(N_VARIABLE):#creer entry
    E1 = Entry(frame2,width=10)
    Z.append(E1) #append array Z par entry tout entierz de fct objectif 
    E1.grid(row = 0, column = 1+(2*i+1), pady = 2,)
    lolo=Label(frame2,text="x"+str(i+1),font=('Times',10,'bold')) # fait creer x1,x2...

    lolo.grid(row = 0, column = 2*i+1, pady = 2)

    
 frame2.pack()
