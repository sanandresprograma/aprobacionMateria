print ('¡Bienvenido! Con esta aplicación podrás gestionar las notas de su materia y saber si la aprobaste o no.')
  
nombre = input('ingrese el nombre del estudiante :').capitalize()
materia = input('ingrese el nombre de  la materia :').capitalize()
    
acum = 0
    
nota_acumulada = 0 
while True:   
    nota = float(input('ingrese la nota del  estudiante :'))
    porcentaje = int(input('ingrese el porcentaje de la nota :'))
    nota_acumulada += (porcentaje*nota)/100
        
    if (nota_acumulada >=  3):
        aprobacion = 'aprobado'
    else:
        aprobacion = 'reprobado'
            
    acum += porcentaje    
    
    if (acum < 100):
        falta = input('¿falta añadir notas S/N?') 
        if (falta == 'N' or falta == 'n'):
            print(f'El estuiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
            break
            
        elif  falta == 'S' or falta =='s':
            continue
                
        else:
            break
    elif (acum == 100):
        print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {round(nota_acumulada,2)} resultando en {aprobacion}')
        break
    else: 
        print('El porcentaje evaluado de una materia no puede ser mayor a 100')
        acum -= porcentaje
        nota_acumulada -= (porcentaje*nota)/100
        continue
        
