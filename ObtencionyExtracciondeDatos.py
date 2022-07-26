# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:07:46 2022

@author: Laptop ASUS
"""

import requests
import os

museos = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv", allow_redirects = True  )
os.makedirs('D:/User Documents/Downloads/ProyectoAlkemy/museos')
open('D:/User Documents/Downloads/ProyectoAlkemy/museos/museos-25-Jul-2022.csv', 'wb').write(museos.content)

cines = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv", allow_redirects= True)
os.makedirs('D:/User Documents/Downloads/ProyectoAlkemy/cines')
open('D:/User Documents/Downloads/ProyectoAlkemy/cines/cines-25-Jul-2022.csv', 'wb').write(cines.content)

bibliotecas = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects = True)
os.makedirs('D:/User Documents/Downloads/ProyectoAlkemy/bibliotecas')
open('D:/User Documents/Downloads/ProyectoAlkemy/bibliotecas/bibliotecas-25-Jul-2022.csv', 'wb').write(bibliotecas.content)