import unittest

from pagos import procesar_pago_usuario

ACTIVO = {'activo': True}
INACTIVO = {'activo': False}
SALDO_INICIAL = 5000


class TestProcesarPagoUsuario(unittest.TestCase):
    def setUp(self):
        self.tarjeta = {'saldo': SALDO_INICIAL}

    def test_usuario_nulo(self):
        self.assertFalse(
            procesar_pago_usuario(None, self.tarjeta, 100, "CO", False)
        )
        self.assertEqual(self.tarjeta['saldo'], SALDO_INICIAL)

    def test_usuario_inactivo(self):
        self.assertFalse(
            procesar_pago_usuario(
                INACTIVO, self.tarjeta, 100, "CO", False
            )
        )
        self.assertEqual(self.tarjeta['saldo'], SALDO_INICIAL)

    def test_saldo_insuficiente(self):
        self.assertFalse(
            procesar_pago_usuario(
                ACTIVO, self.tarjeta, 6000, "CO", False
            )
        )
        self.assertEqual(self.tarjeta['saldo'], SALDO_INICIAL)

    def test_no_vip_con_impuesto_mx(self):
        self.assertTrue(
            procesar_pago_usuario(ACTIVO, self.tarjeta, 100, "MX", False)
        )
        self.assertAlmostEqual(self.tarjeta['saldo'], SALDO_INICIAL - 116)

    def test_vip_monto_base_con_impuesto_co(self):
        self.assertTrue(
            procesar_pago_usuario(ACTIVO, self.tarjeta, 1000, "CO", True)
        )
        self.assertAlmostEqual(self.tarjeta['saldo'], SALDO_INICIAL - 1071)

    def test_vip_monto_alto_con_impuesto_cl(self):
        self.assertTrue(
            procesar_pago_usuario(ACTIVO, self.tarjeta, 2000, "CL", True)
        )
        self.assertAlmostEqual(self.tarjeta['saldo'], SALDO_INICIAL - 1904)

    def test_pais_sin_impuesto(self):
        self.assertTrue(
            procesar_pago_usuario(ACTIVO, self.tarjeta, 100, "PE", False)
        )
        self.assertAlmostEqual(self.tarjeta['saldo'], SALDO_INICIAL - 100)


if __name__ == '__main__':
    unittest.main()
