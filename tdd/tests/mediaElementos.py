import unittest

def calcular_media(num1, num2):
    return (num1 + num2) / 2

class TestCalcularMedia(unittest.TestCase):

    def test_media_inteiros(self):
        self.assertEqual(calcular_media(10, 20), 15)

    def test_media_decimais(self):
        self.assertEqual(calcular_media(3.5, 7.5), 5.5)

    def test_media_negativos(self):
        self.assertEqual(calcular_media(-10, 10), 0)

if __name__ == '__main__':
    unittest.main()
