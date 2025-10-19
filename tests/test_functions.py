import unittest
import os
from funtions import load_file

class Test(unittest.TestCase):

    def setUp(self):
        # crea un archivo temporal de prueba
        self.test_file = "test_file.csv"
        with open(self.test_file, "w") as f:
            f.write("id;Name;Gender;Eye Color;Race;Hair color;Height;Publisher;Skin color;Alignment;Weight\n")
            f.write("6;Superman;Male;Blue;Kryptonian;Black;191;DC Comics;Fair;Good;107\n")
            f.write("7;Wonder Woman;Female;Blue;Amazon;Black;183;DC Comics;Olive;Good;74\n")

    def tearDown(self):
        # Borrar el archivo temporal después de la prueba
        os.remove(self.test_file)

    def test_load_file_returns_data(self):
        heroes = load_file(self.test_file)
        self.assertIsInstance(heroes, dict, "El resultado es un diccionario")

    def test_load_file_contains_expected_keys(self):
        heroes = load_file(self.test_file)
        self.assertIn("6", heroes)
        self.assertIn("9", heroes)

    def test_load_fields_are_correct(self):
        heroes = load_file(self.test_file)
        superman = heroes["6"]
        self.assertEqual(superman["name"], "Superman")
        self.assertEqual(superman["gender"], "Male")
        self.assertEqual(superman["alignment"], "Bad")

if __name__ == "__main__":
    unittest.main()