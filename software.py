import os
import re
from email.message import EmailMessage
import smtplib
import ssl
import json
import time
import pyautogui, webbrowser

def software():
    def registrar_nombre():
        while True:
            nombre = input('Ingrese su nombre\n')
            ex = re.search(r'^[A-Z][a-z]*$',nombre)
            os.system('cls')
            if ex == None:
                print('Nombre invalido, su nombre debe tener una mayúscula y minusculas')
            else:
                confirmarN = int(input(f'Su nombre es el siguiente: {nombre}, presione 1 para confirmar o presione 2 para cambiarlo\n'))
                if confirmarN == 1:
                    os.system('cls')
                    return nombre
                else:
                    os.system('cls')
    def registrar_apellido():
        while True:
            apellido = input('Ingrese su apellido\n')
            ex = re.search(r'^[A-Z][a-z]*$',apellido)
            os.system('cls')
            if ex == None:
                print('Apellido invalido, su apellido debe tener una mayúscula y minusculas')
            else:
                confirmarA = int(input(f'Su apellido es el siguiente: {apellido}, presione 1 para confirmar o presione 2 para cambiarlo\n'))
                if confirmarA == 1:
                    os.system('cls')
                    return apellido
                else:
                    os.system('cls')
    def registrar_nacimiento():
        while True:
            nacimiento = input('Ingrese su fecha de nacimiento (FORMATO: DD/MM/AAAA)\n')
            ex = re.search(r'^([0-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(19\d{2}|200[0-9]|202[0-3])$',nacimiento)
            os.system('cls')
            if ex == None:
                print('Fecha de nacimiento invalido, su fecha de nacimiento debe tener el siguiente formato DD/MM/AAAA')
            else:
                confirmarNa = int(input(f'Su fecha de nacimiento es la siguiente: {nacimiento}, presione 1 para confirmar o presione 2 para cambiarla\n'))
                if confirmarNa == 1:
                    os.system('cls')
                    return nacimiento
                else:
                    os.system('cls')
    def registrar_pais():
        while True:
            pais = input('Ingrese su pais\n')
            ex = re.search(r'^[a-zA-Z\s\-\']+',pais)
            os.system('cls')
            if ex == None:
                    print('Pais invalido')
            else:
                confirmarP = int(input(f'Su pais es el siguiente: {pais}, presione 1 para confirmar o presione 2 para cambiarlo\n'))
                if confirmarP == 1:
                    os.system('cls')
                    return pais
                else:
                    os.system('cls')
    def registrar_correo():
        while True:
            correo = input('Ingrese su correo\n')
            ex = re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$',correo)
            os.system('cls')
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
                print('Correo invalido')
            elif buscar_correo():
                print('El correo ya se encuentra en la base de datos')    
            else:
                confirmarP = int(input(f'Su correo es el siguiente: {correo}, presione 1 para confirmar o presione 2 para cambiarlo\n'))
                if confirmarP == 1:
                    os.system('cls')
                    return correo
                else:
                    os.system('cls')
    def registrar_numero():
        while True:
            numero = input('Ingrese su numero de telefono\n')
            ex = re.search(r'^\+\d{1,3}\d{1,14}$',numero)
            os.system('cls')
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
                print('Numero invalido, debe colocar su numero con el codigo de país, sin espacios ni guiones')
            elif buscar_numero():
                print('El numero ya se encuentra en la base de datos')
            else:
                confirmarNu = int(input(f'Su Numero es el siguiente: {numero}, presione 1 para confirmar o presione 2 para cambiarlo\n'))
                if confirmarNu == 1:
                    os.system('cls')
                    return numero
                else:
                    os.system('cls')
    while True:
        decision = int(input('Pulse 1 para registrar un usuario\npulse 2 para ver los usuarios registrados\npulse 3 para modificar un dato de la base de datos\npulsa 4 para cerrar el programa\n'))
        os.system('cls')
        if decision == 1:
            nombre = registrar_nombre()
            apellido = registrar_apellido()
            nacimiento = registrar_nacimiento()
            pais = registrar_pais()
            correo = registrar_correo()
            numero = registrar_numero()
                        
            if os.path.isfile('usuarios.txt'):
                f = open('usuarios.txt','a')
                dictionary = {'Nombre': nombre, 'Apellido': apellido, 'Nacimiento': nacimiento, 'Pais':pais, 'Correo':correo, 'Numero':numero}
                f.write(f"\n{str(dictionary)}")
            else:
                f = open('usuarios.txt','a')
                dictionary = {'Nombre': nombre, 'Apellido': apellido, 'Nacimiento': nacimiento, 'Pais':pais, 'Correo':correo, 'Numero':numero}
                f.write(f"{str(dictionary)}")

            f.close()

            input('USUARIO REGISTRADO, PULSE ENTER PARA CONTINUAR')
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
        elif decision == 2:
            f = open('usuarios.txt', 'r')
            print(f.read())
        elif decision == 3:
            linea = int(input('ingrese que linea quiere modificar\n'))
            with open("usuarios.txt", "r") as f:
                lineas = f.readlines()
            dictionary = json.loads(lineas[linea - 1].replace("'", '"'))
            print(dictionary)
            valor = int(input('Que valor desea cambiar?\n 1=Nombre,\n 2=Apellido,\n 3=Fecha de nacimiento,\n 4=Pais,\n 5=Correo,\n 6=Numero\n'))
            if valor == 1:
                nombre = registrar_nombre()
                dictionary['Nombre'] = nombre
            elif valor == 2:
                apellido = registrar_apellido()
                dictionary['Apellido'] = apellido
            elif valor == 3:
                nacimiento = registrar_nacimiento()
                dictionary['Nacimiento'] = nacimiento
            elif valor == 4:
                pais = registrar_pais()
                dictionary['Pais'] = pais
            elif valor == 5:
                correo = registrar_correo()
                dictionary['Correo'] = correo
            elif valor == 6:
                numero = registrar_numero()
                dictionary['Numero'] = numero
            dictionaryNew = str(dictionary)
            with open('usuarios.txt', 'r+') as f:
                lineas = f.readlines()
                lineas[linea - 1] = f'{dictionaryNew}\n'
                f.seek(0)
                f.writelines(lineas)
                f.truncate()
                f.close()
            print('Dato cambiado exitosamente')
        elif decision == 4:
            break

software()