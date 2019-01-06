from django.db import models


class Person(models.Model):
    SEX = (('M', 'MASCULINO'),
           ('F', 'FEMININO'),
           )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=SEX, default='M')
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField(max_length=400, null=True, blank=True, help_text='Descreva aqui, um pouco da experiência '
                                                                            'profissional do cliente')
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
