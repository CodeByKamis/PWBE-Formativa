from django.urls import path
from .views import LoginView, UsuarioListCreat, UsuarioRetrieveUpdateDestroy, ReservaAmbienteListCreate, ReservaAmbienteRetrieveUpdateDestroy, ReservaAmbienteProfessorList, DisciplinaListCreate, DisciplinaRetrieveUpdateDestroy, DisciplinaProfessorList

urlpatterns = [
    #login
    path('login/', LoginView.as_view()),

    #usuario
    path('usuario/', UsuarioListCreat.as_view()),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view()),

    #reserva de ambiente
    path('reservas/', ReservaAmbienteListCreate.as_view()),
    path('reservas/<int:pk>/', ReservaAmbienteRetrieveUpdateDestroy.as_view()),
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    #disciplina
    path('disciplina/', DisciplinaListCreate.as_view()),
    path('disciplina/<int:pk>/', DisciplinaRetrieveUpdateDestroy.as_view()),
    path('professor/disciplina', DisciplinaProfessorList.as_view())
]