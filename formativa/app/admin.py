from django.contrib import admin
from .models import Usuario, Disciplina, Sala, ReservaAmbiente
from django.contrib.auth.admin import UserAdmin


class Usuarioadmin (UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
                "fields":(
                    'tipo', 'ni', 'telefone', 'data_nascimento', 'data_contratacao' 
                ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
                "fields":(
                    'tipo', 'ni', 'telefone', 'data_nascimento', 'data_contratacao'
                ),
        }),
    )


admin.site.register(Usuario,Usuarioadmin)
admin.site.register(Disciplina)
admin.site.register(Sala)
admin.site.register(ReservaAmbiente)

