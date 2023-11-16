from rest_framework import serializers
from projeto.models import Profissional,Job



class ProfissionalSerializer(serializers.ModelSerializer ):
    class Meta :
        model = Profissional
        fields = '__all__'


class CadastrarJobSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_lenght=100)
    email = serializers.EmailField(max_lenght=255)

