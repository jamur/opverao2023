# Generated by Django 4.2.1 on 2023-05-13 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadestagiarios', '0003_remove_cidade_estado_estagiario_end_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaodeestagiario',
            name='estagiario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadestagiarios.estagiario'),
        ),
    ]
