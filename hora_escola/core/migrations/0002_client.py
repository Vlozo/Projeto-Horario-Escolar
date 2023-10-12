# Generated by Django 4.2.6 on 2023-10-12 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("student_id", models.CharField(blank=True, max_length=24, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("aluno", "Aluno(a)"),
                            ("professor", "Professor(a)"),
                            ("responsavel", "Responsável"),
                            ("diretoria", "Diretoria"),
                        ],
                        max_length=40,
                    ),
                ),
                ("birthdate", models.DateField(blank=True, null=True)),
                ("phone", models.CharField(blank=True, max_length=14, null=True)),
                (
                    "dependent",
                    models.ManyToManyField(
                        related_name="user_dependent", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "room_class",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.room_class",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
            },
        ),
    ]