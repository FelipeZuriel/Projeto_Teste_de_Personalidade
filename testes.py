from unittest import main, TestCase
from random import randint

from app import question, cont_animal, show_animal

class TestQuestion(TestCase): 
    def test_se_chega_numero_da_questao_1(self):
        result = randint(0, 19)

        self.assertTrue(question(result))

class TestCont_animal(TestCase):
    def test_se_animais_certos_1(self):
        aux = ["coruja", "coruja", "leão"]
        result = cont_animal(aux)
        expected = "coruja"

        self.assertEqual(result, expected)

    def test_se_animais_certos_1_1(self):
        aux = ["coruja", "panda", "leão", "leão"]
        result = cont_animal(aux)
        expected = "coruja"

        self.assertEqual(result, expected, "Teste animal certo 1.1 errado")

    def test_se_animais_certos_2(self):
        aux = ["tigre", "coruja", "panda"]
        result = cont_animal(aux)
        expected = "leão"

        self.assertEqual(result, expected, "Teste animal certo 2 deu errado")

    def test_se_animais_certos_3(self):
        aux = ["panda", "tubarão", "panda"]
        result = cont_animal(aux)
        expected = "panda"

        self.assertEqual(result, expected)

    def test_se_animais_certos_4(self):
        aux = ["tigre", "coruja", "leão", "tigre", "tigre"]
        result = cont_animal(aux)
        expected = "tigre"

        self.assertEqual(result, expected)

    def test_se_animais_certos_5(self):
        aux = ["tubarão", "tubarão", "tubarão"]
        result = cont_animal(aux)
        expected = "tubarão"

        self.assertEqual(result, expected)

class TestShoq_animal(TestCase): 
    def test_se_mostra_animal_1(self):
        result = show_animal("coruja")
        expectd = "coruja"

        self.assertTrue(result)
    
    def test_se_mostra_animal_2(self):
        result = show_animal("dente-de-sabre")
        expectd = "tigre"

        self.assertTrue(result)

if __name__ == '__main__':
    main()