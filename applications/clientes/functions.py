#Funciones para generar numero de registro

import random
import string

#genera un codigo de 6 digitos al azar
def generador_num_registro(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
