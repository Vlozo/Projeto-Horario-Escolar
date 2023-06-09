# Generated by Django 4.2.2 on 2023-06-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_responsavel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.EmailField(default='wcarlos3@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]
