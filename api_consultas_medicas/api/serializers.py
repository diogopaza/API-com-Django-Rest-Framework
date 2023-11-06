from rest_framework import serializers
from api_consultas_medicas import models
from api_consultas_medicas.api import validators

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PessoaProfissional
        fields = '__all__'
    def validate(self, data):
        errors = {}
        if not validators.cpf_valido(data['cpf']):
            errors['cpf'] =  {'cpf':"O número do CPF é inválido"}       
        if not validators.celular_valido(data['celular']):
            errors['celular'] = {'celular':"Digite um numero de celular valido. Exemplo (11 91234-1234)."}
        if errors:
            raise serializers.ValidationError(errors)
        return data   
class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consulta
        fields = '__all__'

class ConsultasPorProfissionaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consulta
        fields = '__all__'


