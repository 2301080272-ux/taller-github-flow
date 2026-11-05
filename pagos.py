FACTOR_VIP_MONTO_ALTO = 0.80
FACTOR_VIP_MONTO_BASE = 0.90
UMBRAL_MONTO_VIP = 1000
SIN_IMPUESTO = 0
IMPUESTOS_POR_PAIS = {
    "CO": 0.19,
    "MX": 0.16,
    "CL": 0.19,
}


def calcular_monto_con_descuento(monto, es_vip):
    if not es_vip:
        return monto
    if monto > UMBRAL_MONTO_VIP:
        return monto * FACTOR_VIP_MONTO_ALTO
    return monto * FACTOR_VIP_MONTO_BASE


def aplicar_impuesto(monto, pais):
    return monto + monto * IMPUESTOS_POR_PAIS.get(pais, SIN_IMPUESTO)


def procesar_pago_usuario(usuario, tarjeta, monto, pais, es_vip):
    if usuario is None:
        return False
    if not usuario['activo']:
        print("Usuario inactivo")
        return False
    if tarjeta['saldo'] < monto:
        print("Saldo insuficiente")
        return False

    monto_final = aplicar_impuesto(
        calcular_monto_con_descuento(monto, es_vip), pais
    )
    tarjeta['saldo'] -= monto_final
    return True
