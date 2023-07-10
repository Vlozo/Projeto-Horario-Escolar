from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_aluno_email_aluno_telefone_responsavel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responsavel',
            options={'verbose_name': 'Responsável', 'verbose_name_plural': 'Responsáveis'},
        ),
    ]