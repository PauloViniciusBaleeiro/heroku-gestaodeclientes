# Generated by Django 2.1.4 on 2019-01-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMININO')], default='M', max_length=1)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bio', models.TextField(blank=True, help_text='Descreva aqui, um pouco da experiência profissional do cliente', max_length=400, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
        ),
    ]
