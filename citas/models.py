from django.db import models

# Create your models here.

class Centro(models.Model): 
    nombre = models.CharField(max_length=100)
    nombre_legal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    web = models.URLField(max_length=100)
    logo = models.ImageField(upload_to='logos')

    def __unicode__(self):
        return self.nombre


class Especialidad(models.Model):
	nombre = models.CharField(max_length=100)
        def __unicode__(self):
            return self.nombre

class Medico(models.Model):
    id_rut = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fono = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad)
    centro = models.ForeignKey(Centro)
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __unicode__(self):
        return self.id_rut

class Prevision(models.Model):

    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Prevision"
        verbose_name_plural = "Previsiones"

    def __unicode__(self):
        return self.nombre
    

class Paciente(models.Model):
    
    id_rut = models.CharField(max_length=100, primary_key=True)
    nombres = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    celular = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    prevision = models.ForeignKey(Prevision)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __unicode__(self):
        return self.id_rut
    
class Reserva(models.Model):

    idPaciente = models.ForeignKey(Paciente)
    idMedico = models.ForeignKey(Medico)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50)
    confirmado = models.BooleanField()


    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __unicode__(self):
        return '%s %s' % (self.idPaciente,self.idMedico)