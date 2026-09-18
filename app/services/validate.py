import ipaddress
import re
from urllib.parse import urlparse


# We check that the IP is validated
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except Exception:
        return False

# Method that checks the domain
def check_domain(valor):

    patron = r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return bool(re.match(patron, valor))


# Method to check the URL
def check_url(url):
    if not isinstance(url, str):
        return False
    try:
        resultado = urlparse(url)
        return bool(resultado.scheme) and bool(resultado.netloc)
    except ValueError:
        return False

# We check that the hash has the correct format
def check_hash(variable):
    patron = r'^[0-9a-fA-F]{64}$'
    return bool(re.match(patron, variable))


# We check the database indicators
def check_indicator(indicator):

    if indicator.type == "ip":
        if check_ip(indicator.value):
            if 0 <= indicator.confidence <= 100:
                print(indicator.confidence)
                return {"status" : "ok"}
            else:
                return {"status" : "error",
                        "msg":"EL confidence debe estar entre el 0 y el 100 "}
        else:
            return {"status":"error",
                    "msg":"Formato de ip invalida"}
        
    elif indicator.type == "domain":
        if check_domain(indicator.value):
            if 0 <= indicator.confidence <= 100:
                return {"status":"ok"}
            else:
                return {"status":"error",
                        "msg":"EL confidence debe estar entre el 0 y el 100"
                        }
        else: 
            return {"status":"error",
                    "msg":"El formato del dominio es incorrecto"}
        
    elif indicator.type == "url":
        if check_url(indicator.value):
            if 0 <= indicator.confidence <= 100:
                return {"status":"ok"}
            else:
                return{"status":"error",
                       "msg":"EL confidence debe estar entre el 0 y el 100"}
        else:
            return {
                "status":"error",
                "msg":"El formato de la url es incorrecto"
            }
    elif indicator.type == "hash":
        if check_hash(indicator.value):
            if 0 <= indicator.confidence <= 100:
                return {"status":"ok"}
            else:
                return {"status":"error",
                        "msg":"EL confidence debe estar entre el 0 y el 100"
                        }            
        else:
            return {
                "status":"error",
                "msg":"EL hash introduciodo es incorrecto"}
    else:
        return {"status":"error","msg":"El tipo no es el adecuado, Tipos permitidos -> [ip | url | domain | hash]"}