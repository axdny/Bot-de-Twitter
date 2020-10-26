#Importamos las librerias tweepy, time, random y sys (para utilizar los modulos)
import tweepy
import time
import random
import sys

#En mi caso tengo que importar los modulos de esta manera.
sys.path.insert(0, "/Users/Andres/Google Drive/Cursos de Programacion/Python/bot_twitter/credenciales.py")
sys.path.insert(0, "/Users/Andres/Google Drive/Cursos de Programacion/Python/bot_twitter/listado.py")

from credenciales import *
from listado import *

#Creamos el objeto para autenticarnos en Twitter.
twitter_API = tweepy.API(auth)

#Creamos un bucle for que buscara de manera aleatoria las frases en la lista CANCIONES
#y las ira publicando cada 43200 segundos (12 horas).
for i in canciones:
    lyric = random.choice (canciones)
    twitter_API.update_status (lyric)
    time.sleep (43200)
