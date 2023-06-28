habitaciones = open('ejercicio4.txt','w')
habitaciones.truncate()
habitaciones.close()

def mostrar_habitaciones_disponibles(habitaciones):
    habitaciones.seek(0)
    lineas = habitaciones.readlines()
    
    linea = 0
    habitaciones_disponibles = []
    for linea in lineas:
        if f'habitacion {hab} ' in linea and ' ocupada ' in linea:
            habitaciones_disponibles.append(linea)
            print(f'La habitación {hab} esta ocupada.')
        elif f'Habitacion {hab} ' in linea and ' desocupada' in linea:
            habitaciones_disponibles.append(linea)
            print(f'La habitación {hab} no esta ocupada.')

def ingresar_paciente(habitaciones, hab, nombre, dni):
    habitaciones.seek(0)
    lineas = habitaciones.readlines()
    habitaciones.seek(0)
    
    lineas_modificadas = []
    linea = 0
    for linea in lineas:
        if f'habitacion {hab} ' in linea and ' ocupada ' in linea:
            print(f'La habitación {hab} esta ocupada. No se puede asignar al paciente.')
            return
        elif f'Habitacion {hab} ' in linea and ' ocupada ' not in linea:
            lineas_modificadas.append(f'La habitacion {hab} esta ocupada por el paciente {nombre}, DNI: {dni}\n')
        else:
            lineas_modificadas.append(linea)
    
    habitaciones.seek(0)
    habitaciones.truncate()
    habitaciones.writelines(lineas_modificadas)
    habitaciones.flush()
    print(f'El paciente {nombre} ha sido asignado a la habitación {hab}.')

def dar_de_alta_paciente(habitaciones, hab):
    habitaciones.seek(0)
    lineas = habitaciones.readlines()
    habitaciones.seek(0)
    
    linea = 0
    lineas_modificadas = []
    for linea in lineas:
        if f'habitacion {hab} ' in linea and ' ocupada ' in linea:
            lineas_modificadas.append(f'Habitacion {hab} esta desocupada\n')
            print(f'La habitación {hab} ha sido liberada.')
        elif f'Habitacion {hab} ' in linea and ' desocupada' in linea:
            lineas_modificadas.append(linea)
            print(f'La habitación {hab} no esta ocupada.')
        else:
            lineas_modificadas.append(linea)
    
    habitaciones.seek(0)
    habitaciones.truncate()
    habitaciones.writelines(lineas_modificadas)
    habitaciones.flush()
opc = 1

with open('ejercicio4.txt', 'a+') as habitaciones:
    for i in range(20):
        habitaciones.write(f'Habitacion {i + 1} esta desocupada\n')
    habitaciones.seek(0)

    while opc != 4:
        print('\n-------------------------------')
        print('MENU de Habitaciones de Hospital')
        print('--------------------------------')
        print('1. Ingresar paciente')
        print('2. Estado de habitación')
        print('3. Dar de alta a un paciente')
        print('4. Salir')
        opc = int(input('Ingrese una opción: '))
        
        if opc == 1:
            nombre = input('\nIngrese el nombre del paciente: ')
            dni = int(input('Ingrese el DNI del paciente: '))
            hab = int(input('Ingrese a qué habitación sera asignado este paciente: '))
            while hab > 20 or hab < 1:
                hab = int(input('Habitación no valida, ingrese una habitación valida: '))
            ingresar_paciente(habitaciones, hab, nombre, dni)
        elif opc == 2:
            hab = int(input('\nIngrese que número de habitación quiere revisar: '))
            while hab > 20 or hab < 1:
                hab = int(input('Habitación no valida, ingrese una habitación valida: '))
            mostrar_habitaciones_disponibles(habitaciones)
        elif opc == 3:
            num_hab = int(input('\nIngrese la habitación que quiere desocupar: '))
            while num_hab > 20 or num_hab < 1:
                num_hab = int(input('Número de habitación no valido, ingrese un número de habitación valido: '))
            dar_de_alta_paciente(habitaciones, num_hab)
        elif opc == 4:
            print('Muchas gracias por usar el programa')
            break
        else:
            print('Número no valido, por favor ingrese un número valido')