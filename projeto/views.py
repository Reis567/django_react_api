from django.shortcuts import render
from rest_framework.views import APIView , Response
from projeto.models import Profissional,Job
from projeto.serializer import ProfissionalSerializer,CadastrarJobSerializer
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404


# Create your views here.

class ProfissinalAPI(APIView):
    def get(self, request , format=None):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
class CadastrarJobAPI(APIView):
    def post(self, request , id , format=None):
        profissional = get_object_or_404(profissional , id=id)
        serializer = CadastrarJobSerializer(data=request.data)
        if serializer.is_valid():
            job = Job(
                nome = serializer.validated_data.get('nome'),
                email = serializer.validated_data.get('email'),
                profissional = profissional
            )