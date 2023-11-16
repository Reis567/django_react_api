from django.shortcuts import render
from rest_framework.views import APIView , Response
from projeto.models import Profissional

# Create your views here.

class ProfissinalAPI(APIView):
    profissionais = Profissional.objects.all()
