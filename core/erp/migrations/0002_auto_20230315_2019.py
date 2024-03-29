# Generated by Django 3.1.10 on 2023-03-15 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bill',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='bill',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.sale', verbose_name='Venta'),
        ),
    ]
