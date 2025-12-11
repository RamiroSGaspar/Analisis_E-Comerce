def informe_calculos(**resultado_calculos):

    print("----- CALCULOS -----")
    if 'tasa_conversion_global' in resultado_calculos:
        print(f"La tasa de compradores global es de: {resultado_calculos['tasa_conversion_global']:.2f}%")

    if 'tasa_conversion_nuevos' in resultado_calculos and 'tasa_conversion_recurrentes' in resultado_calculos:
        print(f"La tasa de compradores nuevos es de : {resultado_calculos['tasa_conversion_nuevos']:.2f}%")
        print(f"La tasa de compradores recurrentes es de : {resultado_calculos['tasa_conversion_recurrentes']:.2f}%")

    if 'promedio_ticket' in resultado_calculos:
        print(f"El promedio de ticket de compra es: {resultado_calculos['promedio_ticket']:.2f}")

    if 'cant_compras_no_concretadas' in resultado_calculos:
        print(f"La cantidad de visitantes que solo agregaon al carrito pero no compraron: {resultado_calculos['cant_compras_no_concretadas']}")