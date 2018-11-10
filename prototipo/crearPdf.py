from reportlab.pdfgen import canvas
import time


def crear_aula(departamento, carrera, nombreaula, nombredocente, apellidodocente,
               dni, emailprofesor, rol, descripcion):
    c = canvas.Canvas("crear_aula.pdf")
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)
    c.drawString(85, 630, 'Departameto:')
    c.drawString(95, 615, departamento)
    if departamento == '11':
        c.drawString(85, 585, 'Carrera:')
        c.drawString(95, 570, carrera)
    else:
        c.drawString(85, 585, 'Nombre del aula:')
        c.drawString(95, 570, nombreaula)
    c.drawString(85, 540, 'Nombre del Docente:')
    c.drawString(95, 525, nombredocente)
    c.drawString(85, 495, 'Apellido del docente:')
    c.drawString(95, 480, apellidodocente)
    c.drawString(85, 450, 'Dni:')
    c.drawString(95, 435, dni)
    c.drawString(85, 405, 'Email del profesor:')
    c.drawString(95, 390, emailprofesor)
    c.drawString(85, 360, 'Rol del profesor:')
    c.drawString(95, 345, rol)
    c.drawString(85, 315, 'Descripcion:')
    c.drawString(95, 300, descripcion)
    c.drawString(430, 765, time.strftime("%c"))
    c.drawImage("static\silversonic.jpg", 80, 780, 50, 50)
    c.line(60, 760, 535, 760)
    c.line(85, 665, 205, 665)
    c.setFont('Helvetica', 15)
    c.drawString(85, 670, 'Datos ingresados:')
    c.setFont('Helvetica', 18)
    c.drawString(170, 800, 'Universidad Tecnologica Nacional')
    c.drawString(200, 720, 'Solicitud: Crear aula')

    c.save()


def matricular():
    c = canvas.Canvas("matricular.pdf")
    c.drawString(100, 750, "matricular")
    c.save()


def microtaller(nombre, apellido, mail, telefono, dni, departamento, carrera, motivo, microtaller):
    c = canvas.Canvas("microtaller.pdf")
    c.drawString(100, 750, nombre)
    c.drawString(100, 740, apellido)
    c.drawString(100, 730, mail)
    c.drawString(100, 720, telefono)
    c.drawString(100, 710, dni)
    c.drawString(100, 700, departamento)
    if departamento == '11':
        c.drawString(100, 690, carrera)
    else:
        c.drawString(100, 690, '------------')
    c.drawString(100, 680, motivo)
    c.drawString(100, 670, microtaller)

    c.save()


def tutoria(motivo, nombre, apellido, email, telefono, dni, departamento, carrera, rol, cant_personas,
            dia1, dia1_hora1, dia1_hora2, dia2, dia2_hora1, dia2_hora2, dia3, dia3_hora1, dia3_hora2,):
    c = canvas.Canvas("tutoria.pdf")
    c.drawString(100, 760, motivo)
    c.drawString(100, 750, nombre)
    c.drawString(100, 740, apellido)
    c.drawString(100, 730, email)
    c.drawString(100, 720, telefono)
    c.drawString(100, 710, dni)
    c.drawString(100, 700, departamento)
    if departamento == '11':
        c.drawString(100, 690, carrera)
    else:
        c.drawString(100, 690, '------------')
    c.drawString(100, 680, rol)
    c.drawString(100, 670, cant_personas)
    c.drawString(100, 660, dia1)
    c.drawString(100, 650, dia1_hora1)
    c.drawString(100, 640, dia1_hora2)
    c.drawString(100, 630, dia2)
    c.drawString(100, 620, dia2_hora1)
    c.drawString(100, 610, dia2_hora2)
    c.drawString(100, 600, dia3)
    c.drawString(100, 590, dia3_hora1)
    c.drawString(100, 580, dia3_hora2)

    c.save()


def matricular(departamento, carrera):
    c = canvas.Canvas("matricular.pdf")
    c.drawString(100, 750, departamento)
    if departamento == '11':
        c.drawString(100, 740, carrera)
    else:
        c.drawString(100, 740, '------------')

    c.save()