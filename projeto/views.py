from django.shortcuts import render
from rest_framework.views import APIView , Response
from projeto.models import Profissional
from projeto.serializer import ProfissionalSerializer
from rest_framework.status import HTTP_200_OK


# Create your views here.

class ProfissinalAPI(APIView):
    def get(self, request , format=None):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
