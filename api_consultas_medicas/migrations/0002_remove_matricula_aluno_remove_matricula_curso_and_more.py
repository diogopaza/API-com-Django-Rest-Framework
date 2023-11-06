# Generated by Django 4.2.6 on 2023-11-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_consultas_medicas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='curso',
        ),
        migrations.AlterField(
            model_name='pessoaprofissional',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
