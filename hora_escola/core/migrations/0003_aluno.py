# Generated by Django 4.2.2 on 2023-06-21 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_turmas_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turma')),
            ],
        ),
    ]
