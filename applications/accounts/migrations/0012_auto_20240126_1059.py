# Generated by Django 3.2 on 2024-01-26 04:59

import applications.accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_payment_payment_accepted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name_de',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Имя на немецком'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name_de',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Фамилия на немецком'),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name_de',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество на немецком'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments_accepted', to=settings.AUTH_USER_MODEL, validators=[applications.accounts.models.is_staff_or_superuser], verbose_name='Оплату принял'),
        ),
    ]
