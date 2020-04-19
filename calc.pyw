from tkinter import *
from tkinter import ttk
from tkhtmlview import HTMLLabel
import os

def tomates(): #--------------------------------------------- ventana para las plagas del tomate
    vtom = Toplevel(root)
    vtom.title("TOMATE")
    vtom.geometry("130x200+480+200")
    vtom.resizable(False, False)
    vtom.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(vtom, text="TIPO DE PLAGA ", bg="LightGreen").pack()
    Label(vtom, text="").pack()
    Button(vtom, text="plaga 1", width=10, height=1,command=op).pack()
    Label(vtom, text="").pack()
    Button(vtom, text="plaga 2", width=10, height=1,command=op).pack()
    Label(vtom, text="").pack()
    Button(vtom, text="plaga 3", width=10, height=1,command=op).pack()
    Label(vtom, text="").pack()
    vtom.mainloop()

def pimientos(): #--------------------------------------------- venatana para las plagas del pimiento
    global ventana_pimiento
    ventana_pimiento = Toplevel(root)
    ventana_pimiento.title("PIMIENTO")
    ventana_pimiento.geometry("130x200+480+200")
    ventana_pimiento.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(ventana_pimiento, text="TIPO DE PLAGA").pack()
    Label(ventana_pimiento, text="").pack()
    Button(ventana_pimiento, text="plaga 1", width=10, height=1,command=op).pack()
    Label(ventana_pimiento, text="").pack()
    Button(ventana_pimiento, text="plaga 2", width=10, height=1,command=op).pack()
    Label(ventana_pimiento, text="").pack()
    Button(ventana_pimiento, text="plaga 3", width=10, height=1,command=op).pack()

def op(): #--------------------------------------------- ventana de pesticida de plaga 1
    plaga= Toplevel(root)
    plaga.title("PESTICIDA")
    plaga.geometry("380x250+480+200")
    plaga.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(plaga, text="TIPO DE PESTICIDA").pack()
    Label(plaga, text="").pack()
    Button(plaga, text="pesticida 1", width=10, height=1,command=data).pack()
    Label(plaga, text="").pack()
    Button(plaga, text="pesticida 2", width=10, height=1,command=data).pack()
    Label(plaga, text="").pack()
    Button(plaga, text="pesticida 3", width=10, height=1,command=data).pack()
    Label(plaga, text="").pack()

#==================================== VENTANA CALCULAR ================================================

def data(): #--------------------------------------------ventana de la calculadora de pesticida

    def comp(): #--------------------------------------------- ventana del proceso de los datos ingresados
        r.set(float(ab.get())/float(ds.get()))

    root.destroy()
    vent=Tk()
    vent.title('CALCULAR CANTIDAD DE PESTICIDA')
    vent.geometry("500x350+480+200")
    bgcolor="white"
    vent.configure(background=bgcolor)
    vent.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    vent.resizable(False, False)#-----------------Bloquear redimencion de la ventana

    ab=StringVar() #distancia de surcos
    ab.set(0)
    ds=StringVar()#ancho de banda
    ds.set(0)
        

    texto=("@Tomvargas")
    Label(vent,text=texto,bg=bgcolor,fg='#B5E61D').place(x=300,y=10)
    Label(vent,text="Medidor De Pesticida",bg=bgcolor, fg='#B5E61D', font = 'bold').place(x=20,y=9)
    n=80

    Label(vent, text='Ingresar los valores actuales',bg=bgcolor,fg='#B5E61D').place(x=20,y=70)

    Label(vent,text="Distancia de surco (ab)",bg=bgcolor).place(x=20 , y=20+n )
    Entry(vent,textvariable=ab).place(x=20 , y=20*2+n )

    Label(vent,text="Ancho de banda  (bs)",bg=bgcolor).place(x=20 , y=20*3+n )
    Entry(vent,textvariable=ds).place(x=20 , y=20*4+n )

    r=StringVar()#resultado(pesticida)
    r.set(0)
    

    Label(vent,text="",bg=bgcolor).pack()
    Button(vent,text="Calcular",bg=bgcolor,command=comp).place(x=20, y=20*11+n)
    Label(vent,text="Resultado",bg=bgcolor).place(x=230, y=180)
    Entry(vent,justify="center",textvariable=r,state="disabled").place(x=200, y=200)


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


