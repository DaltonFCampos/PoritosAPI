# Generated by Django 4.2.5 on 2023-10-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_compra_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
