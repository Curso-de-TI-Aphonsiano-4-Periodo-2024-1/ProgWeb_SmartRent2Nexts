import unittest
from SmartRent2Nexts import executar_app

class SmartRent2NextsTest(unittest.TestCase):
    def test_executar_app(self):
        executando = executar_app();
        self.assertTrue(executando)
        

if __name__ == '__main__':
    unittest.main()