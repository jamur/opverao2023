# Generated by Django 4.2.1 on 2023-05-13 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadestagiarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaodeestagiario',
            name='estagiario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='cadestagiarios.estagiario'),
        ),
    ]
