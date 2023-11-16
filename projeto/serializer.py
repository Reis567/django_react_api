from rest_framework import serializers
from projeto.models import Profissional



class ProfissionalSerializer(serializers.ModelSerializer ):
    class Meta :
        model = Profissional
        fields = '__all__'