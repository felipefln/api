from rest_framework import serializers
from .models import Clientes

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ('id', 'nome', 'nome_medico', 'data_consulta', 'data_nascimento', 'data_coleta')