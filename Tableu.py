
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import numpy as np

def  tableau(N_VARIABLE,N_CONTRINT,root,A,B,frame1,Ord):#nbr col,ligne,matr prin,secong membre,ordre(<,>,=): genere entry tableau 
    
   
     
     for i in range(N_CONTRINT):#creation par ligne
        a1=[]#tabeau pour append les entrys par lignes dans a1 ,lors de recomm va etre null
       
        for j in range(N_VARIABLE):
                eee=Entry(frame1,width=10)#creation des entry pour A
                eee.grid(row=2*i,column=2*j,pady=20)
                a1.append(eee)
                l1 = Label(frame1, text = "X"+str(j+1),font=('Times',10,'bold'))
                l1.grid(row =2*i, column =2*j+1, sticky = W, pady = 20)
        A.append(a1) # append ligne par ligne ,apres chaque ligne se vide , ala fin obtenir A contient tous entry de matrice princi
        cmb=ttk.Combobox(frame1,values=["<=",">=","="],width=10) #creation combobox <,>,=
        cmb.grid( row=2*i,column=2*N_VARIABLE)
        cmb.current(0)# par default <=
        Ord.append(cmb)# get combobox <,>,= dans tab ord 
        Label(frame1,text=" ").grid(row=2*i,column=2*N_VARIABLE+1,pady=20)
        f=Entry(frame1,width=10) # entry de second membre
        B.append(f) # append dans matrice B
        f.grid(row=2*i,column=2*N_VARIABLE+2,pady=20)
     
    
     frame1.pack()


