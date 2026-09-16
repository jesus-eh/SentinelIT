from storage.get_indicators import get_indicators as indicadores
from storage.get_indicators import get_indicatorsID as indicadoresID
from storage.get_indicators import post_indicator as subida_indicator



# Services: Obtenemos el indicador, comprobamos y lo enviamos
# Route
def obtener_indicador(db):
    lista = indicadores(db)

    if not lista:
        return "No se obtubo indicadores de la BBDD"
    else:
        return lista

def obtener_indicadorID(db, id):
    lista = indicadoresID(db, id)

    if lista == None:
        return f"No se ha encontrado el indicador el {id}"
    else:
        return lista

def insertar_indicadores(indicator, db):

    post = subida_indicator(indicator, db)

    if post.get("succes") == "ok":
        return "Indicadores subido correctamente"
    else:
        return post.get("msg")