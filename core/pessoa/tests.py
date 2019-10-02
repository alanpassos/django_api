from django.test import TestCase
from .models import Pessoa

class PessoaTestCase(TestCase):
    def setUp(self):
        Pessoa.objects.create(nome='Teste 1')

    def test_pessoa_by_name(self):
        pessoa = Pessoa.objects.get(nome='Teste 1')
        self.assertEqual(pessoa.nome, 'Teste 1')



