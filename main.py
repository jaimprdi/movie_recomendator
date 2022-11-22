import pandas as pd 
import sys 
import time 
import re 


def menu():
    print('\nTiene que seleccionar una de las  siguientes opciones: ') 
    print(" 1. Genero\n 2. Idioma\n 3. tiempo/duracion pleicula en minutos ")
    opciones=['genre','language','runtime',0,0,0,0]
    opcion=0
    while opcion!= 1 or 2 or 3:
        print('seleccione un 0 a continuacion si quiere salir del programa')
        opcion = int(input("Elija un numero del uno al 3 segun su preferencia de busqueda: "))
        if opcion== 1 or 2 or 3 :
            return opcion
        if opcion==5:
            return 0
        
def salida_controlada():
    
    print('\nEnding program at users request')
    sys.exit()
    
def genero(df):
    lista_generos=[]
    genre = input("¿Que genero le gusta? ",)
    # comprobamos que lo introducido sea un genero 
    data_check = []
    for i in range(len(df['Type'])):
        genero = df['Type'][i]
        if genero==genre:
            lista_generos.append(df['Title'][i])
        if re.search(genre,str(genre),re.IGNORECASE) != None:
            data_check.append(idioma)
    return lista_generos

def idioma(df):
    lista_idiomas=[]
    idiomas = input("¿Que idioma le interesa escuchar? ",)
    # comprobamos que lo introducido sea un idioma
    data_check = []
    for i in range(len(df['languages'])):
        idioms = df['languages'][i]
        if idioms==idiomas:
            lista_idiomas.append(df['Title'][i])
        if re.search(idiomas,str(idioma),re.IGNORECASE) != None:
            data_check.append(idioma)
    return lista_idiomas

def duracion(df,tiempo):
    
    margen_tiempo=[tiempo-20,tiempo+20]
    peli=[]
    df_t=df['runtime']
    for i in range(len(df_t)):
        if int(df_t[i])== tiempo: 
            #si damos una con el tiempo exacto paramos la busqueda 
            return df['Title'][i]
        else: 
            if int(df_t[i])> margen_tiempo[0] and int(df_t[i])< margen_tiempo[1]:
                peli.append(df['Title'][i])
    return peli
                
if __name__ == "__main__":
    df = pd.read_csv('netflix.csv',sep=";",encoding="LATIN_1")
    # Selecciona la opción de búsqueda
    opcion = menu()
    if opcion==0:
        ending=True
        sys.exit()
    else:
        ending=False
    # Puedes hacer tantas búsquedas como quieras
    while not ending:
        opcion= menu()
        if opcion==0:
            ending=True
        else:
            ending=False
        # Búsqueda por género
        if opcion == 1:
            genre = genero(df)
            if len(genre)!=0: 
                print('Le recomendamos:')
                print('')
                for i in range(5):
                    print(genre[i])
            else:
                print("no hay peliculas recomendadas en ese genero")
        # Búsqueda por idioma
        elif opcion == 2:
            idiomass= idioma(df)
            if len(idiomass)!= 0:
                print('Le recomendamos:')
                for i in range(5):
                    print(idiomass[i])
            else :
                print("no hay peliculas recomandadas en ese idioma ")
        # Búsqueda runtime
        elif opcion == 3 :
            tiempo_esperado= int(input('Escriba el tiempo en minutos que quiere que dure su pelicula (sea razonable):'))
            peliculas = duracion(df,tiempo_esperado)
            print('\nNuestras recomendacion(es):' )
            print('')
            print(peliculas)
        
    if ending: 
        salida_controlada()
        