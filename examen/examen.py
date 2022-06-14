#examen.py

#Claire Dearing: Ok, encárgate urgente de conseguir a la persona que necesitas, no me importa de
#dónde lo saques. Necesito que proceses urgente este archivo con información del parque y esté
#disponible en mi monitor de informes. Y no olvide determinar cual de nuestro dinosaurios fuel el
#ultimo en ser descubierto y quien lo hizo. [actividad para resolver]
from listas import Lista
from jurassic_park import DINOSAURIOS
class Dinosaurs:
    
    def __init__(self, time,zone_code,dino_number,alert_level):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
    

    def __str__(self):
        return f"{self.time} {self.zone_code}, {self.dino_number}, {self.alert_level}"



lista_dinosaurs = Lista()
lista_alertas = Lista()

file = open('alerts.txt')
lineas = file.readlines()

lista = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    
    # print(datos[4].split('/'))
    
    lista_alertas.insertar(Dinosaurs(datos[0],
                              datos[1],
                              datos[2],
                              datos[3].split('/')),
                         campo='nombre')
    lista.append(Dinosaurs(datos[0],
                      datos[1],
                      datos[2],
                      datos[3].split('/')))

lista_alertas.insertar(Dinosaurs(datos[0],
                             datos[1],
                             datos[2],
                             datos[3].split('/')),
                        campo='fecha')

lista_alertas.barrido_alertas()
print()                      

#3
lista_alertas.eliminar('LYF010', zona_code)
lista_alertas.eliminar('LYF010', zona_code)
lista_alertas.eliminar('WYG075', zona_code)

dato=lista_alertas
if(dato):
    if(dato.zone_code == 'HYD195'):
        dino_number=11
 

#4
if((dato.name == 'Tyrannosaurus Rex')): 
        if((dato.alert_level == 'critical') or (dato.alert_level == 'high')):
            print(dato.name)
            print(dato.type)
            print(dato.number)
            print(dato.period)
            print(dato.named_by)
        
if((dato.name == 'Spinosaurus')): 
        if((dato.alert_level == 'critical') or (dato.alert_level == 'high')):
            print(dato.name)
            print(dato.type)
            print(dato.number)
            print(dato.period)
            print(dato.named_by)           
if((dato.name == 'Giganotosaurus')): 
        if((dato.alert_level == 'critical') or (dato.alert_level == 'high')):
            print(dato.name)
            print(dato.type)
            print(dato.number)
            print(dato.period)
            print(dato.named_by)

#5


#6

#7

#8

