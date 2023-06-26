from django.db import models


# Departamento
class Departamento(models.Model):
    id_departamento = models.CharField(max_length = 10, unique = True, primary_key = True)
    nombre = models.CharField(max_length = 50, null = False)
    director = models.CharField(max_length = 50, null = False)
    descripcion = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return f"{ self.id_departamento }"
    
    class Meta:
        db_table = 'departamento' 


# Profesor
class Profesor(models.Model):
    id_profesor = models.CharField(max_length = 10, unique = True, primary_key = True)
    id_departamento_fk = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50, null = False)
    direccion = models.CharField(max_length = 50, null = False)
    telefono = models.CharField(max_length = 10, unique = True, null = False)

    def __str__(self):
        return f"{ self.id_profesor } - { self.id_departamento_fk }"

    class Meta:
        db_table = 'profesor'


# Curso
class Curso(models.Model):
    id_curso = models.CharField(max_length = 10, unique = True, primary_key = True)
    id_profesor_fk = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 50, null = False)
    nivel = models.CharField(max_length = 20, null = False)
    descripcion = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return f"{ self.id_curso } - { self.id_profesor_fk }"

    class Meta:
        db_table = 'curso'
