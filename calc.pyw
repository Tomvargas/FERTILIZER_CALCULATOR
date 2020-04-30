from tkinter import *
from tkinter import ttk
from tkhtmlview import HTMLLabel
import os

def tomates(): #--------------------------------------------- ventana para las plagas del tomate
    vtom = Toplevel(root)
    vtom.title("TOMATE")
    bg="white"
    btn="#ee374e"
    vtom.geometry("130x200+480+200")
    vtom.resizable(False, False)
    vtom.configure(bg=bg)
    vtom.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(vtom, text="TIPO DE PLAGA",bg=bg).pack()
    Label(vtom, text="",bg=bg).pack()
    Button(vtom, text="plaga 1", width=10, height=1,command=op,bg=btn,fg=bg).pack()
    Label(vtom, text="",bg=bg).pack()
    Button(vtom, text="plaga 2", width=10, height=1,command=op,bg=btn,fg=bg).pack()
    Label(vtom, text="",bg=bg).pack()
    Button(vtom, text="plaga 3", width=10, height=1,command=op,bg=btn,fg=bg).pack()
    Label(vtom, text="",bg=bg).pack()
    vtom.mainloop()

def pimientos(): #--------------------------------------------- venatana para las plagas del pimiento
    vpim = Toplevel(root)
    bg="white"
    btn="#93cc2e"
    vpim.title("PIMIENTO")
    vpim.geometry("130x200+480+200")
    vpim.configure(bg=bg)
    vpim.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    
    Label(vpim, text="TIPO DE PLAGA",bg=bg).pack()
    Label(vpim, text="",bg=bg).pack()
    Button(vpim, text="plaga 1", width=10, height=1,command=op,bg=btn,fg=bg).pack()
    Label(vpim, text="",bg=bg).pack()
    Button(vpim, text="plaga 2", width=10, height=1,command=op,bg=btn,fg=bg).pack()
    Label(vpim, text="",bg=bg).pack()
    Button(vpim, text="plaga 3", width=10, height=1,command=op,bg=btn,fg=bg).pack()
    vpim.mainloop()

def op(): #--------------------------------------------- ventana de pesticida
    plaga= Toplevel(root)
    bg="white"
    plaga.title("PESTICIDA")
    plaga.geometry("180x250+480+200")
    plaga.configure(bg=bg)
    plaga.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(plaga, text="TIPO DE PESTICIDA",bg=bg).pack()
    Label(plaga, text="",bg=bg).pack()
    Button(plaga, text="pesticida 1", width=10, height=1,command=data).pack()
    Label(plaga, text="",bg=bg).pack()
    Button(plaga, text="pesticida 2", width=10, height=1,command=data).pack()
    Label(plaga, text="",bg=bg).pack()
    Button(plaga, text="pesticida 3", width=10, height=1,command=data).pack()
    Label(plaga, text="",bg=bg).pack()

#==================================== VENTANA CALCULAR ================================================

def data(): #--------------------------------------------ventana de la calculadora de pesticida

    def comp(): #--------------------------------------------- ventana del proceso de los datos ingresados
        r.set(float(ab.get())/float(ds.get()))

    vent=Toplevel(root)
    bg_img=PhotoImage(file= "images/BG2.png")
    Label(vent, image=bg_img).place(x=0, y=0, relwidth=1, relheight=1)
    vent.title('CALCULAR CANTIDAD DE PESTICIDA')
    vent.geometry("500x350+480+200")
    bgcolor="white"
    vent.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    vent.resizable(False, False)#-----------------Bloquear redimencion de la ventana


    ab=StringVar() #distancia de surcos
    ab.set(0)
    ds=StringVar()#ancho de banda
    ds.set(0)
        

    texto=("CANTIDAD A USAR")
    Label(vent,text=texto,bg='#b5e61d',fg=bgcolor,font = 'bold,35').place(x=330,y=30)
    Label(vent,text="Medidor De Pesticida",bg='#b5e61d', fg=bgcolor, font = 'bold,30').place(x=20,y=9)
    n=80

    Label(vent, text='Ingresar los valores actuales',bg='#739112',fg=bgcolor, font = 'bold').place(x=19,y=70)

    Label(vent,text="Distancia de surco (ab)",bg=bgcolor,fg='#34404b').place(x=20 , y=35+n )
    Entry(vent,textvariable=ab).place(x=20 , y=35*2+n )

    Label(vent,text="Ancho de banda  (bs)",bg=bgcolor,fg='#34404b').place(x=20 , y=35*3+n )
    Entry(vent,textvariable=ds).place(x=20 , y=35*4+n )

    r=StringVar()#resultado(pesticida)
    r.set(0)
    

    Label(vent,text="",bg='#b5e61d').pack()
    Button(vent,text="Calcular",bg=bgcolor,command=comp).place(x=20, y=20*11+n)
    Label(vent,text="Resultado",bg=bgcolor).place(x=230, y=155)
    Entry(vent,justify="center",textvariable=r,state="disabled").place(x=230, y=180)


    vent.mainloop()

#==================================== VENTANA INFORMACIÓN ================================================
def info():
    inf=Toplevel(root)
    inf.geometry("220x110+480+200")
    inf.resizable(False, False)
    inf.title("Información")
    inf.configure(bg="white")
    inf.iconbitmap(r'images/descarga_gMJ_icon.ico')
    Label(inf,bg="white",text=" ").pack()

    Label(inf,bg="white",justify="left",text="Este software sigue en desarrollo y estará\ndisponible con un interfaz completa.\nCódigo en mi página de github: ").pack()
    HTMLLabel(inf,bg="white", html='<a style="color:#34404b" href="https://github.com/Tomvargas">@Tomvargas</a>').pack()


#==================================== VENTANA PRINCIPAL ================================================
color="white"
root=Tk()# iniciar ventana
root.geometry("380x250+480+200")# DIMENSIONES DE LA VENTANA
root.resizable(False, False)
root.title("CALCULADORA DE PESTICIDA")# TITULO DE LA VENTANA
root.iconbitmap(r'images/descarga_gMJ_icon.ico')# ATRIBUIR ICONO
bg_image=PhotoImage(file= "images/BG.png")
ttk.Label(root, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)


Label(text="TIPO DE CULTIVO", bg="#B5E61D",fg="white",width="380", font=("Calibri", 15)).pack()
Button(text="ⓘ",bg="#B5E61D",fg="white",font=(13),command=info).place(x=10, y=5)
Button(text="TOMATE", height="2", width="30", bg=color, command=tomates).place(x=50+33, y=50+30) 
#Label(text="").pack()
Button(text="PIMIENTO", height="2", width="30", bg=color, command=pimientos).place(x=50+33, y=100+30) 
#Label(text="").pack()
root.mainloop()


