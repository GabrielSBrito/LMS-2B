from django.shortcuts import render
from core.models import *

from django.shortcuts import render, redirect
from django.views.generic.base import View
from core.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from random import randint



# Create your views here.

# PARTE EXTERNA (MATRICULAR-SE E LOGIN)
def testara_Aluno(n):
    lista = []
    contexto = Usuario.objects.all()
    for x in contexto:
        lista.append(x.ra)
    while n in lista:
        n = randint(100000,199999)
    return n   

def index(request):
    contexto = {
        'cursos': Curso.objects.all()
            
    } #Esse comando puxa as inf. do BD e printa na página
    return render(request,"index.html",contexto)


def matricula(request):


    
    form = AlunoForm(request.POST)
    
    if request.POST:
        form = AlunoForm(request.POST)
        n = randint(100000,199999)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['nome'])
            

        form = AlunoForm()
    else:
        form = AlunoForm()

    contexto = {
        "form" : form,
    }

    return render(request,"matricula.html",contexto)



def login(request):
    return render(request,"logn.html")




# DEPOIS DE LOGAR ------------------------------------------------------------------ PROFESSOR -
#def checa_professor(user):
    #return user.perfil == 'P'

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def pagina_inicial_professor(request):
    return render(request,"Professor/pagina_inicial.html")

def perfil_professor(request):

   
    return render(request, "Professor/PerfilProf.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def subir_aula(request):
    return render(request,"Professor/subir_aula.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def boletim(request):
    return render(request,"Professor/boletim.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def notas(request):
    return render(request,"Professor/notas.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def seleciona_turma_falta(request):
    return render(request,"Professor/seleciona_turma_falta.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def faltas(request):
    return render(request,"Professor/faltas.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def aplicar_teste(request):
    pass

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def mensagens(request):
    return render(request,"Professor/mensagens.html")

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def subir_atividades(request):
    turmas = Turma.objects.all()
    for turma in turmas:
        turma.questoes = Questao.objects.filter(turma=turma)

    contexto = {
        "turmas" : turmas
    }
    return render(request,"Professor/subir_atividades.html",contexto)

def questao_form(request,turma_sigla, questao_id=None):
    turma = Turma.objects.get(turma_sigla=turma_sigla) 

    if questao_id:
        questao = Questao.objects.get(id=questao_id)
    else:
        questao = Questao(turma=turma)   

    if request.POST:
        form = QuestaoForm(request.POST, request.FILES, instance=questao)
        if form.is_valid():
            form.save()
            return redirect("/subir_atividades")
    else:
        form = QuestaoForm(instance=questao)
    
    contexto = {
        "form" : form,
        "turma_sigla" : turma
    }
    
    return render(request, "Professor/questao_form.html", contexto)

#@user_passes_test(checa_professor, login_url='/?error=acesso', redirect_field_name=None)
#@login_required(login_url='/entrar')
def atividades_recebidas(request):
    return render(request,"Professor/atividades_recebidas.html")

def cancelar_matricula(request):
    return render(request,"Professor/cancelar_matricula.html")

    
# DEPOIS DE LOGAR ------------------------------------------------------------------ ALUNO -

def pagina_inicial_aluno(request):
    return render(request,"Aluno/aluno.html")
def perfilaluno (request):
    return render(request,"Aluno/perfilaluno.html")    
   

def entregas(request):
    return render(request,"Aluno/entregas.html")    

def avisos(request):
    return render(request,"Aluno/avisos.html")     

def disponivel(request):
    return render(request,"Aluno/disponivel.html")  

def recepcao(request):
    return render(request,"Aluno/recepcao.html")   
   


def trabalhos(request):
    return render(request,"Aluno/trabalhos.html")   
def exercicios(request):
    return render(request,"Aluno/exercicios.html")   
def envio(request):
    return render(request,"Aluno/envio.html")  


def boletim(request):
    return render(request,"Aluno/boletim.html")   
def visualizacao(request):
    return render(request,"Aluno/visualizacao.html")   


def localidade (request):
    return render(request,"Aluno/localidade.html")   
