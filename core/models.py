# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

from core.models import *


#from django.contrib.auth.models import User
class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50,blank=True,null=True)
    ra = models.IntegerField(unique=True,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=150,blank=True,null=True)
    perfil = models.CharField(max_length=1, default='C',blank=True,null=True)
    ativo = models.BooleanField(default=True)

    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome','email']

    objects = UsuarioManager()

    @property   #Objetos para roubar
    def is_staff(self):
        return self.perfil == 'C'  


    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True


    def get_short_name(self):
        return self.nome
    def get_full_name(self):
        return self.nome

    def __str__(self):
        return self.nome


class Curso(models.Model):

    sigla = models.CharField(max_length=5,unique=True,null=False)
    nome = models.CharField(max_length=50,unique=True,null=False)
    

    def __str__(self):
        return "{} - {}".format(self.sigla,self.nome)

    class Meta:
        db_table = 'Curso'    

class Turma(models.Model):
    
    disciplinaOfertada = models.ForeignKey(to='DisciplinaOfertada', related_name="turmas", null=False, blank=False) 
    professor = models.ForeignKey(to='Professor', related_name="turmas", null=False, blank=False) 
    turno = models.CharField(max_length=15)
    turma_sigla = models.CharField(max_length=1,unique=True)
    cursos = models.ManyToManyField('Curso', db_table='CursoTurma', related_name='turmas', blank=False)

    def __str__(self):
        return "{} " .format(self.turma_sigla)

    class Meta:
        db_table = 'Turma'  



class Aluno(Usuario):
    celular = models.CharField(max_length=50,blank=True,null=True)
    #confirma_matricula = models.ForeignKey(to='Matricula',related_name="data_aluno",db_column="nome_matricula")
    #curso = models.ForeignKey(to='Curso',related_name="curso_aluno",db_column="sigla_curso")
    turma = models.ForeignKey(to='Turma',related_name="turma_aluno",db_column="turma")

    

    def __str__(self):
        return '%s' % int(self.ra)

'''class Curso(models.Model):
    sigla = models.CharField(max_length=5,primary_key=True)
    nome = models.CharField(unique=True, max_length=50)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default = True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome   '''  

class Professor(Usuario):
    apelido = models.CharField(max_length=30,unique = True, null = True)

    def __str__(self):
        return self.nome 
 
'''class Matricula(models.Model):
    nome_matricula = models.CharField(max_length=50,primary_key=True,unique=True)
    data = models.CharField(max_length=20) #ADICIONAR DATA DO NOW
    SEMESTRE_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    semestre = models.CharField(max_length=1,choices=SEMESTRE_CHOICES)
    curso = models.ForeignKey(to='Curso',related_name="Matricula_curso",db_column="sigla")
    periodo = models.ForeignKey(to='Periodo',related_name="Matricula_periodo",db_column="periodo_matricula")



    def __str__(self):
        return self.nome_matricula'''



'''class Curso(models.Model):
    sigla = models.CharField(max_length=5,primary_key=True)
    nome = models.CharField(unique=True, max_length=50)
    carga_horaria = models.IntegerField(default=1000)
    qtd_semestres = models.IntegerField()
    def __str__(self):
        return self.nome'''




'''class Periodo(models.Model):
    PERIODO_CHOICES = (
        ('M', 'M'),
        ('N', 'N'),
    )
    periodo = models.CharField(max_length=1,choices=PERIODO_CHOICES,primary_key=True)

    def __str__(self):
        return self.periodo'''


'''class Disciplinas(models.Model):
    #Retirar sigla na opção (deixar somente no Banco de Dados)
    nome_disciplina = models.CharField(max_length=50)
    nome = models.ForeignKey(to='Professor',related_name="Disciplinas_professor",db_column="nome_professor")
    sigla = models.ForeignKey(to='Curso',related_name="Disciplinas_professor",db_column="sigla_curso")
    turma = models.ForeignKey(to='Turma',related_name="Disciplinas_turma",db_column="nome_turma")
    
    def __str__(self):
        return self.nome_disciplina'''


'''class Turma(models.Model):
    nome_turma = models.CharField(max_length=2,primary_key=True)
    #ra_aluno = models.ForeignKey(to='Aluno',related_name="ra_aluno",db_column="ra")
    #professor = models.ForeignKey(to='Professor',related_name="Turma_professor",db_column="nome")
    periodo = models.ForeignKey(to='Periodo',related_name="Turma_periodo",db_column="periodo")
    curso = models.ForeignKey(to='Curso',related_name="Turma_curso",db_column="sigla_curso")
    #semestre = models.ForeignKey(to='Matricula',related_name="Turma_matricula",db_column="semestre")




    #nome_turma = models.ForeignKey(to='Turma',related_name="Disciplinas_turma",db_column="nome_turma")

    def __str__(self):
        return "%s - %s - %s" % (self.nome_turma, self.periodo, self.curso)'''

















'''class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', db_column='curso', null=False) 
    ano = models.SmallIntegerField(null=False,primary_key=True)
    semestre = models.CharField(max_length=1,null=False)

    USERNAME_FIELD = 'ano'


    def __str__(self):
        return '%s - SEM: %s - ANO: %s' % (self.curso.nome,self.semestre, self.ano)'''


'''class Periodo(models.Model):
    curso = models.ForeignKey(to='GradeCurricular', db_column="curso", null=False) 
    ano = models.ForeignKey(to='GradeCurricular', db_column="ano", null=False, related_name="ano_grade")
    semestre = models.ForeignKey(to='GradeCurricular', db_column="semestre", null=False,related_name="semestre_grade")
    numero = models.SmallIntegerField(null=False,primary_key=True) #tinyint

    USERNAME_FIELD = 'numero'


    
    def __str__(self):
        return '%s - %s - %s' % (self.curso, self.semestre,self.ano )'''


'''class Disciplina(models.Model):
    nome = models.CharField(max_length=240,primary_key=True)
    carga_horaria = models.SmallIntegerField()  #tinyint
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()  

    def __str__(self):
        return self.nome  '''

  



'''class Matricula(models.Model):
    nome = models.CharField(primary_key=True, max_length=50)
    sobrenome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    numero = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome '''

'''
class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', related_name="gradesCurriculares", null=False, blank=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    def __str__(self):
        return self.nome     

class Periodo(models.Model):
    GradeCurricular = models.ForeignKey(to='GradeCurricular', related_name="periodos", null=False, blank=False) #onetomany
    numero = models.SmallIntegerField(null=False) #tinyint
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return self.nome  

'''


class Disciplina(models.Model):
    nome = models.CharField(max_length=240,unique=True)
    carga_horaria = models.SmallIntegerField()
    teoria = models.DecimalField(max_digits=3,decimal_places=2)
    pratica = models.DecimalField(max_digits=3,decimal_places=2)
    ementa = models.TextField()
    competencias = models.TextField()
    habilidades = models.TextField()
    conteudo = models.TextField()
    bibliografia_complementar = models.TextField()
    bibliografia_basica = models.TextField()

    def __str__(self):
        return "{}".format(self.nome)

    class Meta:
        db_table = 'Disciplina'

'''class Matricula(models.Model):
    id_matricula = models.AutoField('id_matricula', primary_key=True)
    ra_aluno = models.ForeignKey(to='Aluno', db_column='ra_aluno', null=False)
    nome_disciplina = models.ForeignKey(to='disciplina', related_name = 'mnome_disciplina', db_column='nome_disciplina', null=False)
    ano_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'mano_ofertado', db_column='ano_ofertado', null=False)
    semestre_ofertado = models.ForeignKey(to='disciplinaofertada', related_name = 'msemestre_ofertado', db_column='semestre_ofertado', null=False)
    cod_turma = models.ForeignKey(to='Turma', related_name = 'mcod_turma', db_column='cod_turma', null=False)

    def __str__(self):
        return '%s - %s' % (self.ra_aluno, self.cod_turma)

    class Meta:
        db_table = 'matricula'
        '''
        
class Matricula(models.Model):
    ra = models.OneToOneField(to='Aluno',related_name="Matriculas", null=False, blank=False,unique=True)
    disciplina = models.ForeignKey(to='DisciplinaOfertada', related_name = 'Mat_DO_D', null=False)
    ano = models.ForeignKey(to='DisciplinaOfertada', related_name = 'Mat_DO_A', null=False)
    semestre = models.ForeignKey(to='DisciplinaOfertada', related_name = 'Mat_DO_S',  null=False)
    turma = models.ForeignKey(to='Turma', related_name = 'Matricula_Turma',  null=False)

    def __str__(self):
        return '%s - %s' % (self.ra, self.turma)

    class Meta:
        db_table = 'Matricula'

class DisciplinaOfertada(models.Model):
    disciplina = models.ForeignKey(to='Disciplina', related_name="disciplinasOfertadas", null=False, blank=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)

    def __str__(self):
        return "{}: {} - {}".format(self.disciplina, self.ano, self.semestre)
    class Meta:
        db_table = 'DisciplinaOfertada'





class GradeCurricular(models.Model):
    curso = models.ForeignKey(to='Curso', related_name="gradesCurriculares", null=False, blank=False) #onetomany
    ano = models.SmallIntegerField(null=False)
    semestre = models.CharField(max_length=1,null=False)
    
    def __str__(self):
        return "{}: {} - {}".format(self.curso, self.ano, self.semestre)

    class Meta:
        db_table = 'GradeCurricular'


class Periodo(models.Model):
    gradeCurricular = models.ForeignKey(to='GradeCurricular', related_name="periodos", null=False, blank=False) 
    numero = models.SmallIntegerField(null=False) 
    disciplinas = models.ManyToManyField('Disciplina', db_table='PeriodoDisicplina', related_name='periodos', blank=False)

    def __str__(self):
        return "{}: {} - {}".format(self.numero,self.gradeCurricular,self.disciplinas)

    class Meta:
        db_table = 'Periodo'




def monta_arquivo(questao,nome_arquivo):
    return "{}/{}/{}".format(questao.turma.turma_sigla, questao.numero,nome_arquivo)



class Questao(models.Model):
    turma = models.ForeignKey(Turma)
    numero = models.IntegerField("Numero")
    entrega = models.DateField("Entrega")
    arquivo = models.FileField(upload_to=monta_arquivo)   

    def __str__(self):
        return "{}".format(self.numero)


'''class Foto(models.Model):
    ra = models.ForeignKey(Professor)
    foto = models.FileField(upload_to="fotos/")'''




      


        


