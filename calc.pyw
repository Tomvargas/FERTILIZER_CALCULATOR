from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

def ventana_inicio():
    global ventana_principal
    pestas_color="white"
    ventana_principal=Tk()
    ventana_principal.geometry("380x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("CALCULADORA DE PESTICIDA")#TITULO DE LA VENTANA

    #==========================================================================================================================
    #............................................ ICONO DE LAS VENTANAS .......................................................

    ventana_principal.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    #==========================================================================================================================
    #.............................................. FONDE DE LA VENTANA .......................................................
    #==========================================================================================================================
    '''
        1) SE DECLARA UNA VARIABLE CON LA FUNCION PhotoImage() Y PARAMETRO FILE IGUAL A LA DIRECCION Y NOMBRE DE IMAGEN
            RECOMENDABLE QUE LA IMAGEN ESTE EN LA MISMMA CARPETA QUE EL ARCHIVO...
            >>> bg_image=PhotoImage(file= "BG.png")


        2) CON ttk Y UN Label SE DAN PARAMETROS DE LA VENTANA DONDE SE VA A MOSTRAR EL FONDO, image IGUALADO A LA VARIABLE QUE
            SE CREO ANTERIORMENTE Y LA UBICACION , ESTA NO VA A CAMBIAR PARA NADA
            >>> ttk.Label(ventana_principal, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)

        3) LA IMAGEN EN CUESTION DEBE TENER LAS MISMAS DIMENCIONES EN PIXELES QUE LA VENTANA, SI LA VENTANA ES 300X300 LA IMAGEN
            TAMBIEN MEDIRA LO MISMO

    '''
    #==========================================================================================================================

    bg_image=PhotoImage(file= "BG.png")
    ttk.Label(ventana_principal, image=bg_image).place(x=0, y=0, relwidth=1, relheight=1)
    #==========================================================================================================================
    #==========================================================================================================================


    Label(text="TIPO DE CULTIVO", bg="#B5E61D", width="300", height="2", font=("Calibri", 13)).pack()
    #Label(text="").pack()
    Button(text="TOMATE", height="2", width="30", bg=pestas_color, command=tomates).place(x=50+33, y=50+30) 
    #Label(text="").pack()
    Button(text="PIMIENTO", height="2", width="30", bg=pestas_color, command=pimientos).place(x=50+33, y=100+30) 
    #Label(text="").pack()
    ventana_principal.mainloop()
    
def tomates(): #--------------------------------------------- ventana para las plagas del tomate
    ventana_tomate = Toplevel(ventana_principal)
    ventana_tomate.title("PLAGA")
    ventana_tomate.geometry("380x250")
    ventana_tomate.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    
    Label(ventana_tomate, text="TIPO DE PLAGA ", bg="LightGreen").pack()
    Label(ventana_tomate, text="").pack()
    Button(ventana_tomate, text="plaga 1", width=10, height=1,command=opcion1).pack()
    Label(ventana_tomate, text="").pack()
    Button(ventana_tomate, text="plaga 2", width=10, height=1,command=opcion2).pack()
    Label(ventana_tomate, text="").pack()
    Button(ventana_tomate, text="plaga 3", width=10, height=1,command=opcion2).pack()
    Label(ventana_tomate, text="").pack()

def opcion1(): #--------------------------------------------- ventana de pesticida de plaga 1
    ventana_plaga1= Toplevel(ventana_principal)
    ventana_plaga1.title("PESTICIDA")
    ventana_plaga1.geometry("380x250")
    ventana_plaga1.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(ventana_plaga1, text="Seleccione el tipo de pesticida: ", bg="LightGreen").pack()
    Label(ventana_plaga1, text="").pack()
    Button(ventana_plaga1, text="pesticida 1", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga1, text="").pack()
    Button(ventana_plaga1, text="pesticida 2", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga1, text="").pack()
    Button(ventana_plaga1, text="pesticida 3", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga1, text="").pack()

def opcion2(): #--------------------------------------------- ventana de pesticida de plaga 2
    ventana_plaga2= Toplevel(ventana_principal)
    ventana_plaga2.title("PESTICIDA")
    ventana_plaga2.geometry("380x250")
    ventana_plaga2.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(ventana_plaga2, text="Seleccione el tipo de pesticida: ", bg="LightGreen").pack()
    Label(ventana_plaga2, text="").pack()
    Button(ventana_plaga2, text="pesticida 1", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga2, text="").pack()
    Button(ventana_plaga2, text="pesticida 2", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga2, text="").pack()
    Button(ventana_plaga2, text="pesticida 3", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga2, text="").pack()

def opcion3(): #--------------------------------------------- ventana de pesticida de plaga 3
    ventana_plaga3= Toplevel(ventana_principal)
    ventana_plaga3.title("PESTICIDA")
    ventana_plaga3.geometry("380x250")
    ventana_plaga3.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(ventana_plaga3, text="Seleccione el tipo de pesticida: ", bg="LightGreen").pack()
    Label(ventana_plaga3, text="").pack()
    Button(ventana_plaga3, text="pesticida 1", width=10, height=1,command=datos1).pack() #------------------------- llamamos command=datos1 para abir la ventana de la calculadora 
    Label(ventana_plaga3, text="").pack()
    Button(ventana_plaga3, text="pesticida 2", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga3, text="").pack()
    Button(ventana_plaga3, text="pesticida 3", width=10, height=1,command=datos1).pack()
    Label(ventana_plaga3, text="").pack()

def datos1(): #--------------------------------------------ventana de la calculadora de pesticida
    ventana_principal.destroy()
    vent=Tk()
    vent.title('Calculadora Para Pesticida')
    vent.geometry("500x350")
    vent.configure(background='#B5E61D')
    vent.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    vent.resizable(False, False)#-----------------Bloquear redimencion de la ventana
    
    ab=StringVar() #distancia de surcos
    ab.set(0)
    ds=StringVar()#ancho de banda
    ds.set(0)
        
    
    texto=("@Tomvargas")
    Label(vent,text=texto,bg='#B5E61D',fg='white').place(x=300,y=10)
    Label(vent,text="Medidor De Pesticida",bg='#B5E61D', fg='white', font = 'bold').place(x=20,y=9)
    n=80

    Label(vent, text='Ingresar los valores actuales',bg='#B5E61D').place(x=20,y=70)

    Label(vent,text="Distancia de surco (ab)",bg='#B5E61D').place(x=20 , y=20+n )
    Entry(vent,textvariable=ab).place(x=20 , y=20*2+n )
    
    Label(vent,text="Ancho de banda  (bs)",bg='#B5E61D').place(x=20 , y=20*3+n )
    Entry(vent,textvariable=ds).place(x=20 , y=20*4+n )
    

    def comp(): #--------------------------------------------- ventana del proceso de los datos ingresados

        r.set(float(ab.get())/float(ds.get()))

    r=StringVar()#resultado(pesticida)
    r.set(0)

    Label(vent,text="").pack()
    Button(vent,text="Calcular",command=comp).place(x=20, y=20*11+n)
    Label(vent,text="Resultado").place(x=230, y=180)
    Entry(vent,justify="center",textvariable=r,state="disabled").place(x=200, y=200)
    
    
    vent.mainloop()
  
                
def pimientos(): #--------------------------------------------- venatana para las plagas del pimiento
    global ventana_pimiento
    ventana_pimiento = Toplevel(ventana_principal)
    ventana_pimiento.title("Selececciones el tipo de plaga")
    ventana_pimiento.geometry("380x250")
    ventana_pimiento.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    
    Label(ventana_pimiento, text="Seleccione el tipo de plaga: ", bg="LightGreen").pack()
    Label(ventana_pimiento, text="").pack()
    Button(ventana_pimiento, text="plaga 1", width=10, height=1,command=opcion4).pack()
    Label(ventana_pimiento, text="").pack()
    Button(ventana_pimiento, text="plaga 2", width=10, height=1,command=opcion5).pack()
    Label(ventana_pimiento, text="").pack()
    Button(ventana_pimiento, text="plaga 3", width=10, height=1,command=opcion6).pack()

def opcion4(): #--------------------------------------------- ventana de pesticida de plaga 1
    ventana_plaga4= Toplevel(ventana_principal)
    ventana_plaga4.title("Selececciones el tipo de plaga")
    ventana_plaga4.geometry("380x250")
    ventana_plaga4.iconbitmap(r'images/descarga_gMJ_icon.ico ')


    Label(ventana_plaga4, text="Seleccione el tipo de pesticida: ", bg="LightGreen").pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 1", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 2", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 3", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()

def opcion5(): #--------------------------------------------- ventana de pesticida de plaga 2
    ventana_plaga4= Toplevel(ventana_principal)
    ventana_plaga4.title("Selececciones el tipo de plaga")
    ventana_plaga4.geometry("380x250")
    ventana_plaga4.iconbitmap(r'images/descarga_gMJ_icon.ico ')


    Label(ventana_plaga4, text="Seleccione el tipo de pesticida: ", bg="LightGreen").pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 1", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 2", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 3", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()

def opcion6(): #--------------------------------------------- ventana de pesticida de plaga 3
    ventana_plaga4= Toplevel(ventana_principal)
    ventana_plaga4.title("Selececciones el tipo de plaga")
    ventana_plaga4.geometry("380x250")
    ventana_plaga4.iconbitmap(r'images/descarga_gMJ_icon.ico ')

    Label(ventana_plaga4, text="Seleccione el tipo de pesticida: ", bg="LightGreen").pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 1", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 2", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()
    Button(ventana_plaga4, text="pesticida 3", width=10, height=1,command=datos2).pack()
    Label(ventana_plaga4, text="").pack()

def datos2(): #--------------------------------------------ventana de la calculadora de pesticida
    ventana_principal.destroy()
    vent=Tk()
    vent.title('Calculadora Para Pesticida')
    vent.geometry("500x350")
    vent.iconbitmap(r'images/descarga_gMJ_icon.ico ')
    vent.resizable(False, False)#-----------------Bloquear redimencion de la ventana
    
    ab=StringVar() #distancia de surcos
    ab.set(0)
    ds=StringVar()#ancho de banda
    ds.set(0)
        
    
    texto=("Universidad Agraria del ecuador ")
    Label(vent,text=texto,bg='#B5E61D',fg='white').place(x=300,y=10)
    Label(vent,text="Medidor De Pesticida",bg='#B5E61D', fg='white', font = 'bold').place(x=20,y=9)
    n=80

    Label(vent, text='Ingresar los valores actuales',bg='white').place(x=20,y=70)

    Label(vent,text="Distancia de surco (ab)",bg='white').place(x=20 , y=20+n )
    Entry(vent,textvariable=ab).place(x=20 , y=20*2+n )
    
    Label(vent,text="Ancho de banda  (bs)",bg='white').place(x=20 , y=20*3+n )
    Entry(vent,textvariable=ds).place(x=20 , y=20*4+n )
    

    def comp(): #--------------------------------------------- ventana del proceso de los datos ingresados

        r.set(float(ab.get())/float(ds.get()))

    r=StringVar()#resultado(pesticida)
    r.set(0)

    Label(vent,text="").pack()
    Button(vent,text="Calcular",command=comp).place(x=20, y=20*11+n)
    Label(vent,text="Resultado").place(x=230, y=180)
    Entry(vent,justify="center",textvariable=r,state="disabled").place(x=200, y=200)
    
    
    vent.mainloop()


ventana_inicio()
 
