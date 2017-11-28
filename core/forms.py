from django import forms

from django import forms
from django.contrib.auth.models import User

from core.models import *
from random import randint
import smtplib

def envia_email(email,ra,s):
    remetente    = 'henriqueytt@gmail.com'
    senha        = 'l11timao'
    
    # Informações da mensagem
    destinatario = email
    assunto      = 'Matricula em Fac. Impacta'
    texto        =  ("Parabens por se matricular! \n Segue seus dados para logar-se no site : \n Seu RA: {0} \n Senha {1} senha \n Por favor altere a senha assim que fizer o login".format(ra,s))
    # Preparando a mensagem
    msg = '\r\n'.join([
    'From: %s' % remetente,
    'To: %s' % destinatario,
    'Subject: %s' % assunto,    '',    
    
    "{}".format(texto)   ])
 
    # Enviando o email
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    server.login(remetente,senha)
    server.sendmail(remetente, destinatario, msg)


class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = "__all__"

class QuestaoForm(forms.ModelForm):

    class Meta:
        model = Questao
        exclude = ["turma"]

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        exclude = ["perfil","last_login","password","ativo","ra"]

    def save(self, commit=True):
        user = super(AlunoForm, self).save(commit=False)
        user.set_password('mudar@mudar')
        user.perfil = 'A'
        user.ra = randint(100000,199999)
        if commit:
            user.save()
            
            envia_email(user.email,user.ra,s=('123@mudar'))  
        return user
        

    '''nome = forms.CharField()
    email = forms.EmailField()
    ra = forms.CharField() '''       

'''class FotoForm(forms.ModelForm):

    class Meta:
        model = Foto
        fields = "__all__"


        '''
    

