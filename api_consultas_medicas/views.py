from django.http import JsonResponse
from api_consultas_medicas.admin import Alunos

def alunos(request):
    if request.method == 'GET':        
        return JsonResponse(Alunos)