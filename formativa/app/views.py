from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer, SalaSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError

#usuario
class UsuarioListCreate(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    
    
class UsuarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk' #é o id do usuario que ele vai procurar

#disciplina
class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()] #para visualizar qualquer um pode
        return[IsGestor()] #se não for visualizar, ou seja, criar etc. é somente o gestor
    
class DisciplinaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):#get, putch, delete, put
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor=self.request.user)
    
#sala
class SalaListCreate(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsGestor]

class SalaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field= 'pk' # Não necessarimanete é obrigatorio, é por identação _> procura por Pk
    
#reservas
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset
    
    
    def perform_create(self, serializer):
        data = serializer.validated_data
        sala = data['sala_reservada']
        periodo = data['periodo']
        data_inicio = data['data_inicio']
        data_termino = data['data_termino']
        #vai verificar de cada dia dentro desse intervalo que quer fazer reserva existe uma reserva na sala
        from datetime import timedelta
        
        dia_inicial = data_inicio
        while dia_inicial <= data_termino:
            conflitante = ReservaAmbiente.objects.filter(
                sala_reservada=sala,
                periodo=periodo,
                data_inicio__lte=dia_inicial, #lte: less than: significa menor ou igual, é para a menor data ou o dia atual do agendamento
                data_termino__gte=dia_inicial #gte: greater than: significa maior ou igual, é a data maior ou a final
            )
            if conflitante.exists(): #caso o conflito exista, vamos dar um retorno para o usuario
                raise ValidationError(
                    f"Infelizmente a Sala '{sala}' já tem uma reserva no período '{periodo}' no data '{dia_inicial}' :( tente outra por favor."
                )
            dia_inicial +=timedelta(days=1)
        serializer.save() #ele salva se nn tiver conflito nenhum :D
    
    
    
    

class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field= 'pk'

class ReservaAmbienteProfessorList(ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    pagination_class = [IsProfessor]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor=self.request.user) #vai filtrar a reserva daquele professor que está fazendo a consulta
    


#Login
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

