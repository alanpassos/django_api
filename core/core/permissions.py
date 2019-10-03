from rest_framework.permissions import DjangoModelPermissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class CustomModelPermission(DjangoModelPermissions):
    
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']        
        self.perms_map['OPTIONS'] = ['%(app_label)s.view_%(model_name)s'],
        self.perms_map['HEAD'] = ['%(app_label)s.view_%(model_name)s'],
    
    
class IsOwnerPessoaOrReadOnly(CustomModelPermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user

class IsOwnerPostOrReadOnly(CustomModelPermission):
    
    def has_object_permission(self, request, view, obj):    
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.pessoa.user