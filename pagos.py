def procesar_pago_usuario(usuario, tarjeta, monto, pais, es_vip):
    if usuario != None:
        if usuario['activo'] == True:
            if tarjeta['saldo'] >= monto:
                if es_vip == True:
                    if monto > 1000:
                        monto_final = monto * 0.80
                    else:
                        monto_final = monto * 0.90
                else:
                    monto_final = monto

                if pais == "CO":
                    monto_final += monto_final * 0.19
                elif pais == "MX":
                    monto_final += monto_final * 0.16
                elif pais == "CL":
                    monto_final += monto_final * 0.19

                tarjeta['saldo'] -= monto_final
                return True
            else:
                print("Saldo insuficiente")
                return False
        else:
            print("Usuario inactivo")
            return False
    else:
        return False