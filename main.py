#Explicació inicial

print('\033[1m' + 'JOC DEL PENJAT \n' + '\033[0m')

print('\033[1m' + 'Introducción: \n' + '\033[0m')

print("Éste es un juego de pregunta-respuesta que consta de cuatro temáticas de preguntas diferentes para elegir, Matemáticas, Historia, Ciencia y Cine.\n")

print("Cada pregunta acertada suma 1 punto.\n")



#Dades:

import random

Vides = 3
Pasar = 1
Puntuacio = 0

#Llistat amb preguntes:

Preguntes_h = [
'El periodo en el que aparecieron la agricultura y los asentamientos sedentarios se llama:','Neolitico',
  
'¿Cómo se llamaban los gobernantes del antiguo Egipto?', 'Faraones',
  
'Según las leyendas de la antiguedad, ¿quiénes fundaron a Roma?', 'Romulo y Remo',
  
'¿Contra quiénes se enfrentaron los griegos en las Guerras Médicas del siglo V a.C.?', 'Persas',
  
'¿Que emperador fue alumno de Aristoteles?', 'Alejandro Magno',
  
'El primer emperador romano que se hizo cristiano fue:', 'Constantino I',
  
'¿Quien fue el principal profeta del Islam?', 'Mahoma',
  
'¿En que país se inventó la polvora?', 'China',
  
'¿De que país eran los samurais?', 'Japon',
  
'¿Por que otro nombre se conoce el Imperio Romano de Oriente?', 'Imperio Bizantino',
  
'¿En que país pintó Miguel Ángel la bóveda de la Capilla Sixtina?', 'Vaticano',

'¿En que país se construyó la gran ciudad de Teotihuacan?', 'Mexico',

'¿Que idioma hablaban los aztecas?', 'Nahuatl',

'¿En que año sucedió la caída de Tenochtitlan, capital del imperio Azteca-mexica?', '1521',

'¿Cuál fue el último emperador inca?', 'Atahualpa',

'¿En que año comenzó la Revolución Francesa', '1789',

'¿Quién es el patriota suramericano conocido como el "Gran Mariscal de Ayacucho"?', 'Antonio Jose de Sucre',

'¿Cuando se celebraron los Primeros Juegos Olímpicos de la modernidad?', '1896',

'¿Cuál fue la primera persona en ganar el premio Nobel en dos oportunidades?', 'Marie Curie',

'Con qué nombre se conoce la crisis económica generada por el crac financiero de Wall Street en 1929?', 'La gran depresion',
  
]


Preguntes_m = [

'¿Menos por menos es:', 'Mas',

'¿200 dividido por 2 es igual a cuanto?', '100',

'¿Cuántos segundos hay en un día?', '86400',

'9*N es igual a 1296. ¿Cuánto es N?', '144',

'¿Una imagen que también se puede ver en tres dimensiones?', 'Holograma',

'¿Cual es el promedio de la suma de los 120 primeros  números naturales?', '3630',

'¿Cual es el valor de cos(0)*100?', '100',

'¿Quién empezó a usar “∇” el símbolo de Nabla?', 'William Rowan Hamilton',

'¿De cuantos grados es un angulo completo?','360',

'¿De cuantos grados es un angulo llano?', '180',

'¿Cuántos pies hay en cien brazas?', '600',

'¿Qué forma tienen las celdas de panal?', 'Hexagonal',

'¿Cuál es el número anterior a 1000?', '999',

'Un perro pesa 200 kilos y un cachorro pesa 10 kilos menos que él, ¿cuántos kilos pesa la cría?','190',

'¿Cuál es el resultado de multiplicar 7x9x10?', '630',

'¿Cuantos minutos tienen dos horas?', '120',

'¿Cuantos dias tienen 10 meses de 30 dias cada uno?', '300',

'¿Cuantos años son 100 lustros?', '500',

'¿Cómo se llama el polígono de siete lados?', 'Heptagono',

'¿Cuál es el nombre del triángulo que tiene dos lados iguales y uno desigual?', 'Isosceles'
  
]


Preguntes_c = [

  '¿Cuál es el gas más abundante en la atmósfera de la Tierra?', 'Nitrogeno',

  '¿Cuantos huesos tiene el cuerpo humano?', '206',

  '¿Cuál es el material natural más duro del planeta?', 'diamante',

  '¿Cuál es el hueso más grande en el cuerpo humano?', 'femur',

  '¿Cuál es el animal terrestre más grande que existe?', 'Elefante africano',

  '¿Cuál es la partícula más pequeña que existe en el universo?', 'quarks',

  '¿Cuál es el metal que se encuentra en el centro de la tierra?', 'hierro',

  '¿Cuántos elementos químicos existen en la tabla periódica?', '118',

  '¿Cuántos paises hay?', '195',

  '¿Quién es el padre de la química?', 'Antoine Lavoisier',

  '¿Qué significa ADN?', 'Acido desoxirribonucleico',

  '¿Quién escribió el libro “Breve historia del tiempo”', 'Stephen Hawking',

  '¿Cómo se llama el estudio de los hongos?', 'Micologia',

  '¿Cuál es la galaxia espiral más cercana a la Via Láctea?', 'Andromeda',

  '¿Cuántas patas tienen 100 arañas en total?', '800',

  '¿Qué planeta es el más cercano al Sol?', 'Mercurio',

  '¿A cuantos grados se evapora el agua?', '100',

  '¿Cuantos asteroides hay reconocidos en el Sistema Solar?','1097148',

  '¿Que planeta enano fue considerado planeta?', 'Pluton',

  '¿CUal es el elemento mas abundante en el Sol?', 'Hidrogeno'
  
]

Preguntes_f = [

  '¿Quién dirigió Reservoir Dogs?', 'Quentin Tarantino',

  '¿Que pelicula ganó 11 oscars?', 'Titanic',

  '¿Quién dirigió El Gran Lebowski?', 'Hermanos Coen',

  '¿Quién protagoniza El Paciente Inglés?', 'Ralph Fiennes',

  '¿Quién dirigió La delgada línea roja?', 'Terrence Malick',

  '¿En qué año se estrenó Bailando con Lobos?', '1990',

  '¿Cuál es el idioma original de El viaje de Chihiro?', 'Japones',

  '¿Como se llama el protagonista de Regreso al Futuro?', 'Marty McFly',

  '¿Quién es Alfred en el Batman de Christopher Nolan?', 'Michael Caine',

  '¿Quién escribió el relato en el que está basada la película Cadena Perpetua?', 'Stephen King',

  '¿Quien interpretó a Rocky Balboa?', 'Sylvester Stallone',

  '¿Quién dirigió Los otros?', 'Alejandro Amenabar',

  '¿En qué año se estrenó Harry Potter?', '2001',

  '¿Qué color está presente en casi todas las tomas de El Resplandor?', 'Rojo',

  '¿A qué año viajan Marty y Doc en "Regreso al futuro II"?', '2015',

  '¿Qué ciudad está plagada de fantasmas en “Cazafantasmas”?', 'Nueva York',

  '¿Cuánto dinero apostaron Al y Ty en un juego de golf con el juez Smails en “Caddyshack”?', '80000',

  'Que actor protagoniza "Piratas del Caribe"', 'Johnny Depp',

  '¿En qué película protagonizada por Robert De Niro en 1976 tiene una escena muy famosa en la que dice "Me hablas a mi"?', 'Taxi Driver',

  '¿Qué thriller de Alfred Hitchcock es conocido por su impactante escena de la ducha?', 'Psicosis'
  
]

#Introducció de la tematica y dificultat per part de l'usuari, i comprovació de si es correcte:

Tematica = input('\033[1m' + 'Elige la tematica:' + '\033[0m').upper()

while Tematica != "HISTORIA" and Tematica != "MATEMATICAS" and Tematica != "CIENCIA" and Tematica != "CINE":

  print('\033[1m' + 'Tematica incorrecta' + '\033[0m')
  
  Tematica = input('\033[1m' + 'Elige la tematica:' + '\033[0m').upper()

print('\033[1m' + 'Has elegido la tematica:' + '\033[0m', Tematica)

print("")
print("Existen 4 dificultades posibles por elegir: Facil, Normal, Dificil y Personalizada\n")

print("Facil: 3 pistas, 3 intentos")
print("Normal: 2 pistas, 2 intentos")
print("Dificil: 1 pista, 1 intento\n")

print("El usuario tiene 3 vidas, cada una de ellas se termina cuando se han terminado los intentos por acertar la respuesta correcta que éste posee y cuando el usuario se queda sin vidas, pierde. Cuando el usuario ha perdido una vida, se restablece la cantidad de intentos que tiene.\n")

print("Las pistas muestran un termino aleatorio de la respuesta.")


Dificultat = input('\033[1m' + 'Elige la dificultad:' + '\033[0m').upper()

while Dificultat != "FACIL" and Dificultat != "NORMAL" and Dificultat != "DIFICIL" and Dificultat != "PERSONALIZADA":
  print('\033[1m' + 'Dificultad incorrecta' + '\033[0m')
  Dificultat = input('\033[1m' + 'Elige la dificultad:' + '\033[0m').upper()


#Definició de les variables que depenen de la dificultat:

Intents = {}
Pistes = {}

if Dificultat == "FACIL":
  Intents = 3
  Pistes = 3

elif Dificultat == "NORMAL":
  Intents = 2
  Pistes = 2

elif Dificultat == "DIFICIL":

  Intents = 1
  Pistes = 1

else:
  Intents = input('\033[1m' + 'Introduce el número de intentos:' + '\033[0m')
  while Intents.isdigit() == False:
    print('\033[1m' + 'Numero de intentos incorrecto' + '\033[0m')
    Intents = input('\033[1m' + 'Introduce el número de intentos:' + '\033[0m')
  Pistes = input('\033[1m' + 'Introduce el número de pistas:' + '\033[0m')
  while Pistes.isdigit() == False:
    print('\033[1m' + 'Numero de pistas incorrecto' + '\033[0m')
    Pistes = input('\033[1m' + 'Introduce el número de pistas:' + '\033[0m')

Pistes = int(Pistes)
a = Intents = int(Intents)

print("")
print("Comandos espaciales:\n")
print("/pista: Da una pista")
print("/")

print('\033[1m' + 'Comienza el juego con la tematica:' + '\033[0m', Tematica, '\033[1m' + 'y la dificultad:' + '\033[0m', Dificultat)

#Funcionament de la selecció aleatoria de preguntes segons la tematica triada:

#Llista de nombres parells aleatoris. Son parells perque les preguntes es troben en la posició parell de la llista:

Par = []

#Programa per únicament donar 10 valors a la llista Par, i que a més no es repeteixen.
Contador = 0

while Contador < 10:
  Valors = random.randrange(0, 20, 2)
  if Valors in Par:
    pass
    
  else:
    Par.append(Valors)
    Contador = Contador+1
  

#Diccionari format per preguntes y respostes agafades de cada llista de preguntes segons la temàtica:

Preguntes = {}

#Llista amb cada una de les preguntes triades aleatoriament per poder accedir-hi mitjançant un nombre:

Llista = []

if Tematica == "HISTORIA":
  
  for i in range(10):
    Preguntes.update({Preguntes_h[Par[i]]: Preguntes_h[Par[i]+1]})
    Llista.append(Preguntes_h[Par[i]])

elif Tematica == "MATEMATICAS":

  for i in range(10):
    Preguntes.update({Preguntes_m[Par[i]]: Preguntes_m[Par[i]+1]})
    Llista.append(Preguntes_m[Par[i]])

elif Tematica == "CIENCIA":

  for i in range(10):
    Preguntes.update({Preguntes_c[Par[i]]: Preguntes_c[Par[i]+1]})
    Llista.append(Preguntes_c[Par[i]])

elif Tematica == "CINE":

  for i in range(10):
    Preguntes.update({Preguntes_f[Par[i]]: Preguntes_f[Par[i]+1]})
    Llista.append(Preguntes_f[Par[i]])


#Funcionament de les preguntes:

#Contador per anar passant pregunta a pregunta:

n = 0

#Tres valors aleatoris per donar una lletra aleatoria de la resposta, però no s'ha de repetir la mateixa pista si n'empren més d'una en la mateixa pregunta:

m = []
#Contador per anar pasant un a un per els valors de la llista m:

v = 0
#Contador per només agafar la quantitat de valors corresponents al nombre de pistes:
Contador2 = 0

#Fa la pregunta y demana la resposta:
print("")
print(Llista[n])
Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')

#Funcions segons la resposta introduida:

while n<10:
  
  if Resposta.upper() == Preguntes.get(Llista[n]).upper(): 
    Puntuacio = Puntuacio+1
    n = n+1
    m=[]
    v = 0
    Contador2 = 0
    if n<10:
      print(Llista[n])
      Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
    

  elif Resposta == "/datos":
    print("")
    print('\033[1m' + 'Vidas restantes:' +     '\033[0m', Vides)
    print('\033[1m' + 'Posibilidades de pasar:' + '\033[0m', Pasar)
    print('\033[1m' + 'Pistas disponibles:' + '\033[0m', Pistes)
    print('\033[1m' + 'Intentos disponibles:' + '\033[0m', Intents)
    print('\033[1m' + 'Puntuacion:' + '\033[0m', Puntuacio)
    print(Llista[n])
    Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
    
  elif Resposta == "/pista":
    
    
    if Pistes == 0:
          
            print("No tienes mas pistas disponibles")
            v = 0
            Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
            
    else:
        
        while Contador2< Pistes and Contador2<len(Preguntes.get(Llista[n])):
           k = random.randint(0, len(Preguntes.get(Llista[n]))-1)
         
           if k in m:
            pass
              
          
           else:
            m.append(k)
            Contador2 = Contador2+1
            
        if v>=len(Preguntes.get(Llista[n])):
          
          print('\033[1m' + 'Ya se han mostrado todos los terminos de la respuesta' + '\033[0m')
          
          Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
        
        
        
     
        if v<len(Preguntes.get(Llista[n])):
          if Preguntes.get(Llista[n])[m[v]].isalnum() == False:
              print('\033[1m' + 'Un termino aleatorio de la respuesta es:', '{}')
              Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
              v = v+1
      
          else:
              print('\033[1m' + 'Un termino aleatorio de la respuesta es:' + '\033[0m', Preguntes.get(Llista[n])[m[v]])
              v = v+1
              Pistes = Pistes-1
              Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
   
    
    
    
    
    
  elif Resposta == "/pasar":
    if Pasar == 1:
      print('\033[1m' + 'Has pasado' + '\033[0m')
      Intents = a
      n = n+1
      m=[]
      v = 0
      Pasar = Pasar-1
      if n<9:
        print(Llista[n])
        Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
    else:
      print('\033[1m' + 'Ya has pasado previamente' + '\033[0m')
      Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
  else:    
    if int(Intents)>0:
      print('\033[1m' + 'Respuesta equivocada, has perdido un intento' + '\033[0m')
      Intents = Intents-1
      Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
    else:
      if Vides>0:
        print('\033[1m' + 'Has perdido una vida' + '\033[0m')
        Intents = a
        Vides = Vides-1
        Resposta = input('\033[1m' + 'Respuesta:' + '\033[0m')
      else:
        print('\033[1m' + 'Has perdido' + '\033[0m')
        n = 10
        
#Dades per l'usuari i fi del joc
print("")
print('\033[1m' + 'Vidas restantes:' + '\033[0m', Vides)
print('\033[1m' + 'Posibilidades de pasar:' + '\033[0m', Pasar)
print('\033[1m' + 'Pistas disponibles:' + '\033[0m', Pistes)
print('\033[1m' + 'Puntuacion final:' + '\033[0m', Puntuacio)
print("")
print('\033[1m' + 'FIN DEL JUEGO' + '\033[0m')
    


      