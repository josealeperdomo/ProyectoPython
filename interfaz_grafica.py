import os
import re
from email.message import EmailMessage
import smtplib
import ssl
import time
import json
import pyautogui, webbrowser
import tkinter
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.geometry('800x450')

etiqueta = tkinter.Label(ventana, text='REGISTRO')
etiqueta.pack()

nombreUI = tkinter.Label(ventana, text='Nombre')
input_nombre = tkinter.Entry(ventana)
nombreUI.pack()
input_nombre.pack()

apellidoUI = tkinter.Label(ventana, text='Apellido')
input_apellido = tkinter.Entry(ventana)
apellidoUI.pack()
input_apellido.pack()

nacimientoUI = tkinter.Label(ventana, text='Fecha de Nacimiento')
input_nacimiento = tkinter.Entry(ventana)
nacimientoUI.pack()
input_nacimiento.pack()

paisUI = tkinter.Label(ventana, text='Pais')
input_pais = tkinter.Entry(ventana)
paisUI.pack()
input_pais.pack()

correoUI = tkinter.Label(ventana, text='Correo')
input_correo = tkinter.Entry(ventana)
correoUI.pack()
input_correo.pack()

numeroUI = tkinter.Label(ventana, text='Numero')
input_numero = tkinter.Entry(ventana)
numeroUI.pack()
input_numero.pack()

def registro():
    datosValidos = 0
    nombre = input_nombre.get()
    ex = re.search(r'^[A-Z][a-z]*$',nombre)
    if ex == None:
        messagebox.showerror(title="Nombre invalido", message="Su nombre debe tener una mayúscula y minusculas")
    else:
        datosValidos += 1

    apellido = input_apellido.get()
    ex = re.search(r'^[A-Z][a-z]*$',apellido)
    if ex == None:
        messagebox.showerror(title="Apellido invalido", message="Su apellido debe tener una mayúscula y minusculas")
    else:
        datosValidos += 1

    nacimiento = input_nacimiento.get()
    ex = re.search(r'^([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\2(\d{4})$',nacimiento)
    if ex == None:
        messagebox.showerror(title="Fecha de nacimiento invalida", message="Su fecha de nacimiento debe tener el siguiente formato DD/MM/AAAA")
    else:
        datosValidos += 1
    
    pais = input_pais.get()
    ex = re.search(r'^[a-zA-Z\s\-\']+',pais)
    if ex == None:
        messagebox.showerror(title="Pais invalido", message="Pais invalido")
    else:
        datosValidos += 1

    correo = input_correo.get()
    ex = re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$',correo)
    def buscar_correo():
        if(os.path.isfile('usuarios.txt')):
            with open('usuarios.txt', "r") as file:
                for linea in file:
                    if correo in linea:
                        return True
        else:
            return False
        return False
    if ex == None:
        messagebox.showerror(title="Correo invalido", message="Correo invalido")
    elif buscar_correo():
        messagebox.showerror(title="Correo invalido", message="El correo ya se encuentra en la base de datos")
    else:
        datosValidos += 1
    numero = input_numero.get()
    ex = re.search(r'^\+\d{1,3}\d{1,14}$',numero)
    def buscar_numero():
        if(os.path.isfile('usuarios.txt')):
            with open('usuarios.txt', "r") as file:
                for linea in file:
                    if numero in linea:
                        return True
        else:
            return False
        return False
    if ex == None:
        messagebox.showerror(title="Numero invalido", message="Debe colocar su numero con el codigo de país, sin espacios ni guiones")
    elif buscar_numero():
        messagebox.showerror(title="numero invalido", message="El numero ya se encuentra en la base de datos")
    else:
        datosValidos += 1

    if datosValidos == 6:
        if os.path.isfile('usuarios.txt'):
            f = open('usuarios.txt','a')
            dictionary = {'Nombre': nombre, 'Apellido': apellido, 'Nacimiento': nacimiento, 'Pais':pais, 'Correo':correo, 'Numero':numero}
            f.write(f"\n{str(dictionary)}")
        else:
            f = open('usuarios.txt','a')
            dictionary = {'Nombre': nombre, 'Apellido': apellido, 'Nacimiento': nacimiento, 'Pais':pais, 'Correo':correo, 'Numero':numero}
            f.write(f"{str(dictionary)}")
        f.close()
        messagebox.showinfo(message="Registro exitoso", title="Su usuario ha sido registrado exitosamente")
        def envio_email(email_recibir,nombre,apellido):
            email_sender = 'joseperdomopruebas@gmail.com'
            email_password = 'rbfzfobmqpmhbrvw'
            email_receiver = email_recibir

            subject = 'BIENVENIDA'
            body = (f'Bienvenido {nombre} {apellido}')

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())

        envio_email(correo, nombre, apellido)

        def enviar(numero,nombre,apellido):
            webbrowser.open(f'https://web.whatsapp.com/send?phone={numero}')
            time.sleep(40)
            width, height = pyautogui.size()
            x, y = [width * 0.5,height * 0.9]
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(2)
            pyautogui.typewrite(f'Bienvenido {nombre} {apellido}')
            pyautogui.press('enter')
            os.system('cls')
        enviar(numero, nombre, apellido)
    else:
        messagebox.showinfo(message="Registro fallido", title="Ingrese todos los datos correctamente")

boton = tkinter.Button(ventana, text='Registrarse', command=registro)
boton.pack()

def mostrar():
    f = open('usuarios.txt', 'r')
    messagebox.showinfo(message=f.read())

boton2 = tkinter.Button(ventana, text='Mostrar usuarios', command=mostrar)
boton2.pack()

def modificar():
    modificarVentana = tkinter.Tk()
    modificarVentana.geometry('1200x450')
    f = open('usuarios.txt', 'r')
    mostrar_lineas =  tkinter.Label(modificarVentana, text=f.read())
    mostrar_lineas.pack()
    pregunta = tkinter.Label(modificarVentana, text='Cual linea desea modificar?')
    pregunta.pack()
    input_linea = tkinter.Entry(modificarVentana)
    input_linea.pack()
    def aceptar_linea():
        linea = int(input_linea.get())
        with open("usuarios.txt", "r") as f:
            lineas = f.readlines()

        dictionary = json.loads(lineas[linea - 1].replace("'", '"'))

        ventanaDeCambio = tkinter.Tk()
        ventanaDeCambio.geometry('200x400')
        datos = tkinter.Label(ventanaDeCambio, text='Datos')
        datos.pack()
        nombreDLabel = tkinter.Label(ventanaDeCambio, text='Nombre')
        nombreD = tkinter.Entry(ventanaDeCambio)
        nombreD.insert(0, dictionary['Nombre'])
        nombreDLabel.pack()
        nombreD.pack()

        apellidoDLabel = tkinter.Label(ventanaDeCambio, text='Apellido')
        apellidoD = tkinter.Entry(ventanaDeCambio)
        apellidoD.insert(0, dictionary['Apellido'])
        apellidoDLabel.pack()
        apellidoD.pack()

        nacimientoDLabel = tkinter.Label(ventanaDeCambio, text='Fecha de nacimiento')
        nacimientoD = tkinter.Entry(ventanaDeCambio)
        nacimientoD.insert(0, dictionary['Nacimiento'])
        nacimientoDLabel.pack()
        nacimientoD.pack()

        paisDLabel = tkinter.Label(ventanaDeCambio, text='Pais')
        paisD = tkinter.Entry(ventanaDeCambio)
        paisD.insert(0, dictionary['Pais'])
        paisDLabel.pack()
        paisD.pack()
        
        correoDLabel = tkinter.Label(ventanaDeCambio, text='Correo')
        correoD = tkinter.Entry(ventanaDeCambio)
        correoD.insert(0, dictionary['Correo'])
        correoDLabel.pack()
        correoD.pack()

        numeroDLabel = tkinter.Label(ventanaDeCambio, text='Numero')
        numeroD = tkinter.Entry(ventanaDeCambio)
        numeroD.insert(0, dictionary['Numero'])
        numeroDLabel.pack()
        numeroD.pack()

        def cambio():
            datosValidos = 0
            nombre = nombreD.get()
            ex = re.search(r'^[A-Z][a-z]*$',nombre)
            if ex == None:
                messagebox.showerror(title="Nombre invalido", message="Su nombre debe tener una mayúscula y minusculas")
            else:
                datosValidos += 1

            apellido = apellidoD.get()
            ex = re.search(r'^[A-Z][a-z]*$',apellido)
            if ex == None:
                messagebox.showerror(title="Apellido invalido", message="Su apellido debe tener una mayúscula y minusculas")
            else:
                datosValidos += 1

            nacimiento = nacimientoD.get()
            ex = re.search(r'^([0-2][0-9]|3[0-1])(\/)(0[1-9]|1[0-2])\2(\d{4})$',nacimiento)
            if ex == None:
                messagebox.showerror(title="Fecha de nacimiento invalida", message="Su fecha de nacimiento debe tener el siguiente formato DD/MM/AAAA")
            else:
                datosValidos += 1
            
            pais = paisD.get()
            ex = re.search(r'^[a-zA-Z\s\-\']+',pais)
            if ex == None:
                messagebox.showerror(title="Pais invalido", message="Pais invalido")
            else:
                datosValidos += 1

            correo = correoD.get()
            ex = re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$',correo)
            def buscar_correo():
                if(os.path.isfile('usuarios.txt')):
                    with open('usuarios.txt', "r") as file:
                        for linea in file:
                            if correo in linea and correo != dictionary['Correo']:
                                return True
                else:
                    return False
                return False
            if ex == None:
                messagebox.showerror(title="Correo invalido", message="Correo invalido")
            elif buscar_correo():
                messagebox.showerror(title="Correo invalido", message="El correo ya se encuentra en la base de datos")
            else:
                datosValidos += 1
            
            numero = numeroD.get()
            ex = re.search(r'^\+\d{1,3}\d{1,14}$',numero)
            def buscar_numero():
                if(os.path.isfile('usuarios.txt')):
                    with open('usuarios.txt', "r") as file:
                        for linea in file:
                            if numero in linea and numero != dictionary['Numero']:
                                return True
                else:
                    return False
                return False
            if ex == None:
                messagebox.showerror(title="Numero invalido", message="Debe colocar su numero con el codigo de país, sin espacios ni guiones")
            elif buscar_numero():
                messagebox.showerror(title="numero invalido", message="El numero ya se encuentra en la base de datos")
            else:
                datosValidos += 1

            if datosValidos == 6:
                dictionary['Nombre'] = nombre
                dictionary['Apellido'] = apellido
                dictionary['Nacimiento'] = nacimiento
                dictionary['Pais'] = pais
                dictionary['Correo'] = correo
                dictionary['Numero'] = numero
                dictionaryNew = dictionary
                with open('usuarios.txt', 'r+') as f:
                    lineas = f.readlines()
                    lineas[linea - 1] = f'{dictionaryNew}\n'
                    f.seek(0)
                    f.writelines(lineas)
                    f.truncate()
                    f.close()
                messagebox.showinfo(message="Datos cambiados exitosamente", title="Sus datos han sido modificados exitosamente")
            else:
                messagebox.showinfo(message="Error en cambiar los datos", title="Ingrese los datos correctamente")
        

        cambioBoton = tkinter.Button(ventanaDeCambio, text='Cambiar datos', command=cambio)
        cambioBoton.pack()

    aceptar = tkinter.Button(modificarVentana, text='aceptar', command=aceptar_linea)
    aceptar.pack()
    modificarVentana.mainloop()

boton3 = tkinter.Button(ventana, text='Cambiar datos de un usuario', command=modificar)
boton3.pack()

ventana.mainloop()