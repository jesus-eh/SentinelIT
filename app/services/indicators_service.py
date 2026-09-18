from app.storage.indicator_storage import get_indicators as indicators
from app.storage.indicator_storage import get_indicatorsID as indicatorsID
from app.storage.indicator_storage import post_indicator as post_indicator
from app.storage.indicator_storage import del_indicator as delete_indicador
from app.services.validate import check_indicator


# Services: We get the indicator, check it, and send it
# Route
def indicador(db):
    lista = indicators(db)

    if not lista:
        return "No se obtubo indicadores de la BBDD"
    else:
        return lista

def indicadorID(db, id):
    lista = indicatorsID(db, id)

    if lista == None:
        return f"No se ha encontrado el indicador el {id}"
    else:
        return lista

def insert_indicadores(indicator, db):

    resultado = check_indicator(indicator)

    if resultado.get("status") == "ok":
        post = post_indicator(indicator, db)
    else:
        return resultado.get("msg")

    if post.get("succes") == "ok":
        return "Indicadores subido correctamente"
    else:
        return post.get("msg")

def delete_indicadores(id, db):

    comfirmacion = delete_indicador(id, db)

    if comfirmacion.get("succes") == "ok":
        return "Indicadores borrados correctamente"
    else:
        return f"Error: No se ha podido borrar el indicador con id {id}"
