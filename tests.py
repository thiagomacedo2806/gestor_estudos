import os
import django
import json

# Configura o ambiente Django antes de executar os testes
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manage")
django.setup()

from django.test import TestCase, Client
from estudos import TopicoEstudo

class EstudosTestCase(TestCase):
    """
    Conjunto de testes automatizados para verificar as operações do Gestor de Estudos.
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_fluxo_gerenciamento_estudos(self) -> None:
        # 1. Tenta criar um tópico válido
        payload = {
            "titulo": "Estudar Django Inline",
            "descricao": "Entender como rodar Django com configurações simplificadas"
        }
        response_criar = self.client.post(
            "/criar/",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response_criar.status_code, 201)
        self.assertIn("id", response_criar.json())

        # 2. Tenta listar os tópicos de estudo
        response_listar = self.client.get("/")
        self.assertEqual(response_listar.status_code, 200)
        topicos = response_listar.json()
        self.assertEqual(len(topicos), 1)
        self.assertEqual(topicos[0]["titulo"], "Estudar Django Inline")

        # 3. Tenta criar um tópico sem título (deve retornar erro 400)
        response_invalido = self.client.post(
            "/criar/",
            data=json.dumps({"descricao": "Sem titulo"}),
            content_type="application/json"
        )
        self.assertEqual(response_invalido.status_code, 400)