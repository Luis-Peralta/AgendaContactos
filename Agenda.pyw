'''AGENDA PERSONAL:
-Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre,
el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones.
Añadir contacto // Lista de contactos // Buscar contacto // Editar contacto // Cerrar agenda'''
#-----librerias/BD-------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
#------DataBase----------------------------------------
def conexionBD():
    #Esta función crea la base de datos al presionar el boton 'Ingresar'
    conexion = sqlite3.connect('agenda.db')
    CursorAgenda = conexion.cursor()
    try:
        CursorAgenda.execute("""CREATE TABLE CONTACTOS ("ID" INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        "NOMBRE" VARCHAR(50) NOT NULL,
                                                        "TELEFONO" INTEGER UNIQUE NOT NULL,
                                                        "EMAIL" VARCHAR(50))""")
        messagebox.showinfo("Bienvenido","Creaste una Agenda!.")
    except:
        messagebox.showinfo("Hola","Ya hay una agenda creada.")
#-----Ventana-------------------------------------------
root=Tk()
root.title("Agenda Personal")
root.resizable(0,0)
root.geometry("980x613")
root.iconbitmap("Agenda.ico")
bg=PhotoImage(file="background.png")
bg2=PhotoImage(file="background2.png")
#------Cuadro1--------------------------------------------
cuadro1=Frame(root,bg="yellow")
cuadro1.pack(fill="both",expand="True")
fondo=Label(cuadro1,image=bg).place(x=0,y=0)

#------Cuadro2--------------------------------------------
def cuadro2():
    cuadro1.destroy()#<-destruye el cuadro1 del inicio.
    conexionBD()
    cuadro2=Frame(root,bg="blue")
    cuadro2.pack(fill="both",expand="True")
    fondo2=Label(cuadro2,image=bg2).place(x=0,y=0)
    #------Opciones-----------------------------------------
    add = Button(cuadro2,text="AÑADIR CONTACTOS",font=("Arial",16),command=lambda:crearRegistro())
    add.place(x=30,y=250)

    editar = Button(cuadro2,text="EDITAR CONTACTOS",font=("Arial",16),command=lambda:editarRegistro())
    editar.place(x=30,y=300)

    lista = Button(cuadro2,text="LISTA DE CONTACTOS",font=("Arial",16),command=lambda:buscarRegistro())
    lista.place(x=30,y=350)

    cerrar = Button(cuadro2,text="CERRAR",font=("Arial",16),command=quit)
    cerrar.place(x=30,y=400)
    #------Crea un contacto---------------------------------
    def crearRegistro():
        global cuadro3
        cuadro3=Frame(root,bg="blue")
        cuadro3.place(x=350,y=250)
        add.config(state=DISABLED)
        editar.config(state=DISABLED)
        lista.config(state=DISABLED)
        name1 = StringVar()
        tel1 = StringVar()
        email1 = StringVar()
        tituloNewContact = Label(cuadro3,text="NUEVO CONTACTO:",font=("Arial",20),bg="yellow").grid(row=0,column=1,pady=5,columnspan=3)
        name = Entry(cuadro3,justify="center",font=("Consolas",20),width=20,textvariable=name1).grid(row=1,column=1,pady=5,padx=10,columnspan=3)
        nombre = Label(cuadro3,text="Nombre:",font=("Arial",20),bg="blue",fg="white").grid(row=1,column=0,pady=5)
        tel = Entry(cuadro3,justify="center",font=("Consolas",20),width=20,textvariable=tel1).grid(row=2,column=1,pady=5,padx=10,columnspan=3)
        telefono = Label(cuadro3,text="Telefono:",font=("Arial",20),bg="blue",fg="white").grid(row=2,column=0,pady=5)
        email = Entry(cuadro3,justify="center",font=("Consolas",18),width=22,textvariable=email1).grid(row=3,column=1,pady=5,padx=10,columnspan=3)
        correo = Label(cuadro3,text="Email:",font=("Arial",20),bg="blue",fg="white").grid(row=3,column=0,pady=5)
        crear = Button(cuadro3,text="Crear",font=("Arial",16),command=lambda:crear()).grid(row=4,column=1,pady=5)
        borrar = Button(cuadro3,text="Limpiar",font=("Arial",16),command=lambda:clean()).grid(row=4,column=2,pady=5)
        Salir = Button(cuadro3,text="Salir",font=("Arial",16),command=lambda:exit1()).grid(row=4,column=3,pady=5)
        def crear():
            contacto1 = contacto(name1.get(), tel1.get(), email1.get())
            contacto1.add()
            add.config(state=NORMAL)
            editar.config(state=NORMAL)
            lista.config(state=NORMAL)
            cuadro3.destroy()
        def clean():
            name1.set("")
            tel1.set("")
            email1.set("")
            name.focus()
        def exit1():
            add.config(state=NORMAL)
            editar.config(state=NORMAL)
            lista.config(state=NORMAL)
            cuadro3.destroy()

    #------Edita,borra o busca un contacto------------------
    def editarRegistro():
        global cuadro4
        cuadro4=Frame(root,bg="green")
        cuadro4.place(x=300,y=250)
        add.config(state=DISABLED)
        editar.config(state=DISABLED)
        lista.config(state=DISABLED)
        id1 = StringVar()
        name1 = StringVar()
        tel1 = StringVar()
        email1 = StringVar()
        tituloEdit = Label(cuadro4,text="EDITAR/BORRAR O VER CONTACTOS:",font=("Arial",20),bg="yellow").grid(row=0,column=0,pady=5,columnspan=6)
        identificador = Label(cuadro4,text="Ingrese ID:",font=("Arial",20),bg="green",fg="white").grid(row=1,column=0,pady=5)
        idC = Entry(cuadro4,justify="center",font=("Consolas",20),width=20,textvariable=id1)
        idC.grid(row=1,column=1,pady=5,columnspan=5)
        name = Entry(cuadro4,justify="center",font=("Consolas",20),width=20,textvariable=name1).grid(row=2,column=1,pady=5,columnspan=5)
        nombre = Label(cuadro4,text="Nombre:",font=("Arial",20),bg="green",fg="white").grid(row=2,column=0,pady=5)
        tel = Entry(cuadro4,justify="center",font=("Consolas",20),width=20,textvariable=tel1).grid(row=3,column=1,pady=5,columnspan=5)
        telefono = Label(cuadro4,text="Telefono:",font=("Arial",20),bg="green",fg="white").grid(row=3,column=0,pady=5)
        email = Entry(cuadro4,justify="center",font=("Consolas",18),width=24,textvariable=email1).grid(row=4,column=1,pady=5,columnspan=5)
        correo = Label(cuadro4,text="Email:",font=("Arial",20),bg="green",fg="white").grid(row=4,column=0,pady=5)
        Editar = Button(cuadro4,text="Editar",font=("Arial",16),state=DISABLED,command=lambda:update())
        Editar.grid(row=5,column=1,pady=5)
        Borrar = Button(cuadro4,text="Borrar",font=("Arial",16),state=DISABLED,command=lambda:borrar())
        Borrar.grid(row=5,column=2,pady=5)
        Leer = Button(cuadro4,text="Buscar",font=("Arial",16),command=lambda:buscar()).grid(row=5,column=3,pady=5)
        limpiar = Button(cuadro4,text="Limpiar",font=("Arial",16),command=lambda:clean()).grid(row=5,column=4,pady=5)
        Salir = Button(cuadro4,text="Salir",font=("Arial",16),command=lambda:exit1()).grid(row=5,column=5,pady=5)
        #------Actualiza un contacto-----------------------------------------
        def update():
            try:
                conexion = sqlite3.connect('agenda.db')
                CursorAgenda = conexion.cursor()
                CursorAgenda.execute("UPDATE CONTACTOS SET NOMBRE='"+ name1.get()+
                "', TELEFONO='"+ tel1.get()+
                "', EMAIL='"+ email1.get()+
                "'WHERE ID="+  id1.get())
                conexion.commit()
                messagebox.showinfo("Bien!","Contacto actualizado con exito!. ")
                clean()
            except:
                messagebox.showwarning("oops.","Algo salio mal :( ... Vuelve a ingresar los valores!. ")
        #------Borra un contacto----------------------------------------------
        def borrar():
            try:
                conexion = sqlite3.connect('agenda.db')
                CursorAgenda = conexion.cursor()
                pregunta = messagebox.askquestion("ATENCIÓN!","Estas seguro de borrar este contacto?")
                if pregunta=="yes":
                    CursorAgenda.execute("DELETE FROM CONTACTOS WHERE ID="+  id1.get())
                    messagebox.showinfo("Listo!","Contacto borrado con exito!. ")
                    cuadro4.destroy()
                    add.config(state=NORMAL)
                    editar.config(state=NORMAL)
                    lista.config(state=NORMAL)
                conexion.commit()
            except:
                messagebox.showwarning("oops.","Algo salio mal :( ... Vuelve a ingresar los valores!. ")
        #------Busca un contacto----------------------------------------------
        def buscar():
            try:
                conexion = sqlite3.connect('agenda.db')
                CursorAgenda = conexion.cursor()
                CursorAgenda.execute("SELECT * FROM CONTACTOS WHERE ID="+ id1.get())
                for contac in CursorAgenda:
                    name1.set(contac[1])
                    tel1.set(contac[2])
                    email1.set(contac[3])
                conexion.commit()
                Editar.config(state=NORMAL)
                Borrar.config(state=NORMAL)
            except:
                messagebox.showwarning("oops.","Algo salio mal :( ... Vuelve a ingresar los valores!. ")   
        def clean():
            name1.set("")
            tel1.set("")
            email1.set("")
            idC.focus()
            Editar.config(state=DISABLED)
            Borrar.config(state=DISABLED)
        def exit1():
            add.config(state=NORMAL)
            editar.config(state=NORMAL)
            lista.config(state=NORMAL)
            cuadro4.destroy()     

    #------Lista de contactos------------------
    def buscarRegistro():
        global cuadro5
        cuadro5=Frame(root,bg="red")
        cuadro5.place(x=320,y=200)
        add.config(state=DISABLED)
        editar.config(state=DISABLED)
        lista.config(state=DISABLED)

        titleBuscar = Label(cuadro5,text="*N°*  |*NOMBRE*  |*TELEFONO*  |*EMAIL*",font=("Consolas",18),bg="yellow").grid(row=0,column=0,pady=5)

        conexion = sqlite3.connect('agenda.db')
        CursorAgenda = conexion.cursor()
        id_contacto = Listbox(cuadro5, exportselection=0, highlightcolor="yellow", selectbackground="blue", selectmode = SINGLE,font=Font(family="Sans Serif", size=14)
                            ,width="57", height="12")

        CursorAgenda.execute("SELECT * FROM CONTACTOS")
        cont = 1
        for contacto in CursorAgenda:
            try:
                id_contacto.insert(cont, (str(contacto[0])+"                   " + contacto[1]+"              ") + str(contacto[2])+"               " + contacto[3])
                cont+=1
            except:
                messagebox.showwarning("oops.","Algo salio mal :( ... Vuelve a ingresar los valores!. ")

        id_contacto.grid(row=1,column=0,pady=5)

        Salir = Button(cuadro5,text="Salir",font=("Arial",16),command=lambda:exit1()).grid(row=2,column=0,pady=5)
        def exit1():
            add.config(state=NORMAL)
            editar.config(state=NORMAL)
            lista.config(state=NORMAL)
            cuadro5.destroy() 

        conexion.commit()

#------Titulo/Inicio-------------------------------------
ingreso = Button(cuadro1,text="Ingresar",font=("Arial",30),bg="yellow",command=lambda:cuadro2()).place(x=710,y=370)
salir = Button(cuadro1,text="Salir",font=("Arial",30),bg="red",command=quit).place(x=735,y=460)

#------Codigo POO----------------------------------------
class contacto():
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def add(self):
        try:
            conexion = sqlite3.connect('agenda.db')
            CursorAgenda = conexion.cursor()
            registro = [(self.nombre, int(self.telefono), self.email)]
            CursorAgenda.executemany("INSERT INTO CONTACTOS VALUES(NULL,?,?,?)", registro)
            messagebox.showinfo("Listo!","Contacto agregado satisfactoriamente!...\n")
            conexion.commit()
        except:
            messagebox.showwarning("oops.","Algo salio mal :( ... Vuelve a ingresar los valores!. ")

#------END----------------------------------------------
root.mainloop()
