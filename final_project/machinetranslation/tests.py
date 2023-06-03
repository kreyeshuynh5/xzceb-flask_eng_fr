import unittest
import json
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_english_to_french_Bonjour(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_au_revoir(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main() 