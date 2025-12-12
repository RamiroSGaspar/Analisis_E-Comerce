def calculo_conversion_global(funnel):
    '''
    Docstring for calculo_conversion_global
    
    :param funnel: Array con el camino que hizo cada usario en el sitio web
    :return tasa_conversion: Porcentaje de visitantes que llegaron a realizar una compra
    '''
    cantidad_compradores = (funnel == 3).sum()
    cantidad_usuarios = funnel.size
    tasa_global = (cantidad_compradores / cantidad_usuarios) * 100
    return tasa_global

def calculo_conversion_especifica(funnel, tipo_usuario):
    '''
    Docstring for calculo_conversion_especifica
    
    :param funnel: Array con el camino de cada usuario
    :param tipo_usuario: Array con el tipo de usuario de cada visitante (nuevo, recurrente)
    :return tasa_nuevos: Devuelve el porcentaje de compradores nuevos
    :retunr tasa_recurrentes: Devuelve la cantidad
    '''
    # usuarios nuevos
    cantidad_compradores_nuevos = ((funnel == 3) & (tipo_usuario == 0)).sum()
    cantidad_nuevos = (tipo_usuario == 0).sum()
    tasa_nuevos = (cantidad_compradores_nuevos / cantidad_nuevos) * 100

    # usuarios recurrentes
    cantidad_compradores_recurrentes = ((funnel == 3) & (tipo_usuario == 1)).sum()
    cantidad_recurrentes = (tipo_usuario == 1).sum()
    tasa_recurrentes = (cantidad_compradores_recurrentes / cantidad_recurrentes) * 100

    return tasa_nuevos, tasa_recurrentes

def ticket_promedio_de_compra(montos, funnel):
    '''
    Docstring for ticket_promedio_de_compra
    
    :param montos: Array con los gastos de cada visitante
    :param funnel: Array con el estado del funnel para identificar compradores
    '''
    montos_compradores = montos[funnel == 3]
    promedio_monto_gastado = montos_compradores.mean()
    return promedio_monto_gastado

def cantidad_compras_no_concretadas(funnel):
    '''
    Docstring for cantidad_compras_no_concretadas
    
    :param funnel: Array con el funnel para identificar los que agregaron al carrito
    '''
    cantidad_agregado_carrito = (funnel == 2).sum()
    return cantidad_agregado_carrito
