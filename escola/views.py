#from django.http import JsonResponse
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMastriculasAlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibir todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculasViewSet(viewsets.ModelViewSet):
    """ Exibindo Matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMastriculasAlunoSerializer