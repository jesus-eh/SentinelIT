#===========================================
# Author: Jesus Escaño Herrero
# Funcion para calcular el risk de las amenazas
#===========================================

def calculate_risk(indicators):
    # Recogemos el confidence del indicator
    confidence = indicators.confidence

    # Confidence -> 60%
    calculo = confidence*0.60

    # Add type of threat
    threattype = indicators.threat_type
    if (threattype == "malware"):
        calculo += 25
    elif (threattype == "phising"):
        calculo += 20
    elif (threattype == "botnet"):
        calculo += 20
    elif (threattype == "suspicius"):
        calculo += 10
    else:
        calculo += 0

    valorTag = calculate_tags(indicators.tags)
    calculo += valorTag

    return calculo


def calculate_tags(tag):

    valueTag = 0

    for valor in tag:
        if valor == "known_malicious":
            valueTag += 15
        elif valor == "c2":
            valueTag += 15
        elif valor == "tor":
            valueTag += 10
        elif valor == "scanner":
            valueTag += 5
        
    return valueTag