import requests #Importo libreria que previamente instalé
#por consola con pip, esta sirve para hacer solicitudes a APIs

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)  #Devuelve un string con el mensaje solicitado
    print(type(r.text)) #Vemos que es de tipo string y no lo podemos tratar como un itelable
    categories = r.json() #Al tomar el json este viene como una lista de diccionarios que sí podemos iterar

    #Tomamos todos los nombres de los diccionarios de la lista
    for category in categories:
        print(category['name'])
