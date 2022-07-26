# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:55:38 2022

@author: Laptop ASUS
"""

import pandas as pd


df_bibliotecas = pd.read_csv('ProyectoAlkemy/bibliotecas/2022-Jul/bibliotecas-25-Jul-2022.csv')
df_cines = pd.read_csv('ProyectoAlkemy/cines/2022-Jul/cines-25-Jul-2022.csv')
df_museos = pd.read_csv('ProyectoAlkemy/museos/2022-Jul/museos-25-Jul-2022.csv')

"""CREACIÓN DE TABLA MAESTRA PRINCIPAL"""

Tabla_Maestra = pd.DataFrame(columns=['cod_localidad', 'id_provincia', 'id_departamento', 'categoría', 'provincia', 'localidad', 'nombre', 'domicilio', 'código postal', 'número de teléfono', 'mail', 'web'])

df_bibliotecas2 = df_bibliotecas.drop(['Observacion', 'Subcategoria', 'Departamento','Piso', 'Cod_tel', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud','Fuente', 'Tipo_gestion',	'año_inicio',	'Año_actualizacion'], axis=1)
df_cines2 = df_cines.drop(['Observaciones', 'Departamento','Piso', 'cod_area', 'Información adicional','Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion',	'Pantallas',	'Butacas',	'espacio_INCAA', 'año_actualizacion'], axis=1)
df_museos2 = df_museos.drop(['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion'], axis=1)

df_museos2 = df_museos2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría', 'direccion':'domicilio', 'CP':'código postal', 'telefono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_cines2 = df_cines2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia','Dirección':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
df_bibliotecas2 = df_bibliotecas2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})

Tabla_Maestra = Tabla_Maestra.append(df_bibliotecas2)
Tabla_Maestra = Tabla_Maestra.append(df_cines2)
Tabla_Maestra = Tabla_Maestra.append(df_museos2)

"""TABLA INCAA"""

col_incaa = df_cines[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
col_incaa['espacio_INCAA'] = col_incaa['espacio_INCAA'].replace('SI', 'si').replace('si', 1)
col_incaa['espacio_INCAA'] = col_incaa['espacio_INCAA'].fillna(0)
col_incaa['espacio_INCAA'] = col_incaa['espacio_INCAA'].astype("int")
col_incaa = col_incaa.groupby('Provincia').sum()

col_incaa

"""TABLA DE FUENTES Y CATEGORÍAS POR PROVINCIA:"""

df_museos3 = df_museos.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})
df_bruta = df_museos3.append(df_cines).append(df_bibliotecas)
df_limpia = df_bruta.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion', 'Departamento', 'Localidad', 'Dirección', 'Piso', 'Teléfono', 'Información adicional', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA', 'año_actualizacion', 'Observacion', 'Subcategoria', 'Domicilio', 'Cod_tel', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

df_reg_prov = df_limpia.pivot_table(values='Nombre', index=['Fuente', 'Categoría'], columns=['Provincia'], aggfunc='count', margins=True)

