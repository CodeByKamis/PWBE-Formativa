from rest_framework import serializers
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


## o serializer serve para transformar os dados complexos em formatos simples como JSON com o objetivo de simplificar armazenamento e transporte.

# -> nos serializers abaixo são pegos todas as informações dos models.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'
        
class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

#aqui é pego apenas o username e o password para ser feito o login. Para isso é necessário a realização da validação do usuario
class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] ={
            'username': self.user.username,
            'email': self.user.email,
            'tipo': self.user.tipo
        }
        
        return data