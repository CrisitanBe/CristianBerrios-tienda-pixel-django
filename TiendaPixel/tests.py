from django.test import TestCase


class InicioViewTests(TestCase):
    def test_inicio_entrega_catalogo_y_metricas(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('juegos', response.context)
        self.assertEqual(len(response.context['juegos']), 8)
        self.assertEqual(response.context['precio_promedio'], 32490)
        self.assertEqual(response.context['cantidad_en_oferta'], 4)


class DetalleJuegoViewTests(TestCase):
    def test_detalle_calcula_descuento_y_etiqueta(self):
        response = self.client.get('/juego/2/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['precio_descuento'], 35992)
        self.assertEqual(response.context['precio_con_descuento'], 35992)
        self.assertEqual(response.context['etiqueta'], 'Para jugar en grupo')

        oferta_response = self.client.get('/juego/3/')
        self.assertEqual(oferta_response.context['precio_descuento'], 31992)
        self.assertEqual(oferta_response.context['etiqueta'], 'En oferta')
