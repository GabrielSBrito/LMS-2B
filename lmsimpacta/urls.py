"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from core.views import *

from django.contrib.auth.views import login, logout

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset_done

urlpatterns = [

    url(r'^admin/',     admin.site.urls),
    url(r'^$',          index,                                     name="home" ),
    url(r'^matricula/', matricula,                                 name="matricula"),

    url(r'^entrar/',    login,   {"template_name":"login.html"},   name="login"),
    url(r'^sair/',      logout,  {"template_name":"index.html"},   name="logout"),



    url(r'^pagina_inicial_professor/', pagina_inicial_professor,   name="pagina_inicial_professor"),
        url(r'^perfil_professor/$',         perfil_professor,           name="perfil_professor"),
        
            url(r'^change-password/', auth_views.PasswordChangeView.as_view(template_name='Professor/mudar_senha.html'),),
            

    url(r'^subir_aula/',               subir_aula,                 name="subir_aula"),

    url(r'^boletim/',                  boletim,                    name="boletim"),
        url(r'^notas/',                    notas,                      name="notas"),

    url(r'^seleciona_turma_falta/',   seleciona_turma_falta,       name="seleciona_turma_falta"),    
        url(r'^faltas/',                   faltas,                     name="faltas"),

    url(r'^mensagens/',               mensagens,                   name="mensagens"), 


    url(r'^subir_atividades/$',        subir_atividades,            name="subir_atividades"), 
        url(r'^subir_atividades/(?P<turma_sigla>[A-Z,a-z]+)/questao/(?P<questao_id>[0-9]*)',          questao_form,            name="questao_form"),        

    url(r'^atividades_recebidas/',    atividades_recebidas,       name="atividades_recebidas"),

    url(r'^cancelar_matricula/',    cancelar_matricula,       name="cancelar_matricula"),

#--------------------------------------------------------------------------------------------------------------------
     url(r'^pagina_inicial_aluno/',    pagina_inicial_aluno,       name="pagina_inicial_aluno"),
        url(r'^perfilaluno/$',         perfilaluno,           name="perfilaluno"),
            url(r'^change-password/', auth_views.PasswordChangeView.as_view(template_name='Aluno/mudar_senha.html'),),

     url(r'^entregas/',    entregas,       name="entregas"),

     url(r'^avisos/',    avisos,       name="avisos"),

     url(r'^avisos/',    avisos,       name="avisos"),

     url(r'^disponivel/',    disponivel,       name="disponivel"),

     url(r'^recepcao/',    recepcao,       name="recepcao"),
        url(r'^trabalhos/',    trabalhos,       name="trabalhos"),
        url(r'^exercicios/',    exercicios,       name="exercicios"),
        url(r'^envio/',    envio,       name="envio"),

    url(r'^boletim/',    boletim,       name="boletim"), 
    url(r'^visualizacao/',    visualizacao,       name="visualizacao"), 

    url(r'^localidade/',    localidade,       name="localidade"), 






]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)





    