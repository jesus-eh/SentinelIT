from storage.get_indicators import get_indicators as indicadores


# Services: Obtenemos el indicador, comprobamos y lo enviamos
# Route
def obtener_indicador(db):
    lista = indicadores(db)

    if not lista:
        return "No se obtubo indicadores de la BBDD"
    else:
        return lista