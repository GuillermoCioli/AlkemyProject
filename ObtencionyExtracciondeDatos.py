# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:07:46 2022

@author: Laptop ASUS
"""

import requests
import os

bibliotecas = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects = True)
os.makedirs('ProyectoAlkemy/bibliotecas/2022-Jul')
open('ProyectoAlkemy/bibliotecas/2022-Jul/bibliotecas-25-Jul-2022.csv', 'wb').write(bibliotecas.content)

cines = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv", allow_redirects= True)
os.makedirs('ProyectoAlkemy/cines/2022-Jul')
open('ProyectoAlkemy/cines/2022-Jul/cines-25-Jul-2022.csv', 'wb').write(cines.content)

museos = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv", allow_redirects = True  )
os.makedirs('ProyectoAlkemy/museos/2022-Jul')
open('ProyectoAlkemy/museos/2022-Jul/museos-25-Jul-2022.csv', 'wb').write(museos.content)
