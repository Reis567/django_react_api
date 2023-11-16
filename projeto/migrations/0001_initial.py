# Generated by Django 4.2.7 on 2023-11-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('foto', models.URLField(max_length=255)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
    ]
