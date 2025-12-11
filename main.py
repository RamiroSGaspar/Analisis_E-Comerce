import data.dataset as dt
import source.calculos as calc
import reportes.formateadores as form


def generar_informe_completo():
    # Asignacion de nombres
    tasa_global = calc.calculo_conversion_global(dt.funnel)
    tasa_nuevos, tasa_recurrentes = calc.calculo_conversion_especifica(dt.funnel, dt.tipo_usuario)
    promedio_monto = calc.ticket_promedio_de_compra(dt.montos, dt.funnel)
    cantidad_carrito = calc.cantidad_compras_no_concretadas(dt.funnel)

    # Impresion de reporte
    print("="* 50)
    print("INFORME")
    print("="* 50)

    form.informe_calculos(
        tasa_conversion_global= tasa_global,
        tasa_conversion_nuevos= tasa_nuevos,
        tasa_conversion_recurrentes= tasa_recurrentes,
        promedio_ticket= promedio_monto,
        cant_compras_no_concretadas= cantidad_carrito
    )

    print("="* 50)

if __name__ == "__main__":
    generar_informe_completo()