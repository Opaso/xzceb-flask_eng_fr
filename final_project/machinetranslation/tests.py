import unittest
from translator import englishToFrench, frenchToEnglish

class Testtranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(), )

    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(), )

if __name__ == "__main__":
    unittest.main()
