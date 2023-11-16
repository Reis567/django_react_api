from django.shortcuts import render
from rest_framework.views import APIView , Response
from projeto.models import Profissional
from projeto.serializer import ProfissionalSerializer
# Create your views here.

class ProfissinalAPI(APIView):
    def get(self, request , format=None):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data)
