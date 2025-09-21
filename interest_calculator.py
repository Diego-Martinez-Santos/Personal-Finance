'''
C0 : inversión o capital inicial.
n : número de periodos de capitalización.
i : tasa de interes de cada periodo (puede ser constante o varible).
i_const : booleano que recoge si i, la tasa de intereses de una operación financiera, es constante o variable.
i_tasas : lista con las tasas de interes de cada periodo (en caso de ser la tasa de inteses variable)
'''

def compound_capitalization(C0, i, n, i_const, i_tasas = None):
    if i_const:
        CF = C0 * (1 + i)**n
        return CF
    
    elif i_const == False:
        product_tasas = 0
        for i_tasa in i_tasas:
            product_tasas = product_tasas * (1 + i_tasa)

        CF = C0 * product_tasas
        return CF
    
    else:
        return None



def simple_capitalization(C0, i, n, i_const, i_tasas = None):
    if i_const:
        CF = C0 * (1 + n*i)
        return CF
    
    elif i_const == False:
        sum_tasas = 0
        for i_tasa in i_tasas:
            sum_tasas += i_tasa

        CF = C0 * (1 + sum_tasas)
        return CF

    else:
        return None