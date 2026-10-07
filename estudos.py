from django.db import models
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json

class TopicoEstudo(models.Model):
    """
    Modelo simplificado que representa um tópico ou tarefa de estudo de programação.
    """
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    concluido = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "estudos"

    def __str__(self) -> str:
        return self.titulo

def listar_topicos(request: HttpRequest) -> JsonResponse:
    """
    Retorna todos os tópicos de estudo cadastrados no banco de dados.
    """
    topicos = list(TopicoEstudo.objects.values("id", "titulo", "descricao", "concluido"))
    return JsonResponse(topicos, safe=False, json_dumps_params={"ensure_ascii": False})

@csrf_exempt
def criar_topico(request: HttpRequest) -> JsonResponse:
    """
    Cria um novo tópico de estudo através de uma requisição POST com dados JSON.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if not data.get("titulo"):
                return JsonResponse({"erro": "O título é obrigatório"}, status=400)
            
            topico = TopicoEstudo.objects.create(
                titulo=data.get("titulo"),
                descricao=data.get("descricao", "")
            )
            return JsonResponse({"id": topico.id, "status": "criado"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido"}, status=400)
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=500)
            
    return JsonResponse({"erro": "Método não permitido"}, status=405)