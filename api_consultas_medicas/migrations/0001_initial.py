# Generated by Django 4.2.6 on 2023-11-06 12:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_curso', models.IntegerField(null=True)),
                ('descricao', models.CharField(max_length=255)),
                ('nivel', models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaProfissional',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('nome_social', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('celular', models.CharField(max_length=14)),
                ('especialidade', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_consultas_medicas.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_consultas_medicas.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateField(blank=True, null=True)),
                ('pessoa_profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_consultas_medicas.pessoaprofissional')),
            ],
        ),
    ]
