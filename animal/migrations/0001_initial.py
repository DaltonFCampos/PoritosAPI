# Generated by Django 4.2.5 on 2023-10-08 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0004_remove_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especie', models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato'), ('outro', 'Outro')], max_length=100)),
                ('raca', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, default='0.00', max_digits=5)),
                ('idade', models.PositiveIntegerField()),
                ('sexo', models.CharField(choices=[('macho', 'Macho'), ('femea', 'Fêmea')], max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagens/animal_fotos/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animais', to='usuarios.usuario')),
            ],
        ),
    ]