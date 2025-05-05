from rest_framework.permissions import BasePermission


class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'G' #É a autenticação para gestor que abre as permissoes dele
    
class IsProfessor (BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'P' #É a autenticação para professor que abre as permissoes dele

class IsDonoOuGestor (BasePermission):
    def has_object_permission(self, request, view, obj): #esse é para ver quem tem permissoa para ver as reservas de ambiente
        if request.user.tipo == 'G':
            return True
        return obj.professor == request.user