from django.urls import path
from .views import LoginView, UsuarioListCreate, UsuarioRetrieveUpdateDestroy, ReservaAmbienteListCreate, ReservaAmbienteRetrieveUpdateDestroy, ReservaAmbienteProfessorList, DisciplinaListCreate, DisciplinaRetrieveUpdateDestroy, DisciplinaProfessorList, SalaListCreate, SalaRetrieveUpdateDestroy

urlpatterns = [
    #login
    path('login/', LoginView.as_view()),

    #usuario
    path('usuario/', UsuarioListCreate.as_view()),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view()),

    #reserva de ambiente
    path('reservas/', ReservaAmbienteListCreate.as_view()),
    path('reservas/<int:pk>/', ReservaAmbienteRetrieveUpdateDestroy.as_view()),#PAREI AQUI
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    #disciplina
    path('disciplina/', DisciplinaListCreate.as_view()),
    path('disciplina/<int:pk>/', DisciplinaRetrieveUpdateDestroy.as_view()),
    path('professor/disciplina', DisciplinaProfessorList.as_view()),
    
    #sala
    path('sala/', SalaListCreate.as_view()),
    path('sala/<int:pk>/', SalaRetrieveUpdateDestroy.as_view()),

]

#-> ALTA FAZER ESSES TODOS E DEPOIS O URLS DE SALA E FALTA TAMBÉM A TRATATIVA DE ERRO DE HORARIO NO AGENDAMENTO