# Generated by Django 3.2 on 2024-01-28 13:24

import applications.accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20240126_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments_accepted', to=settings.AUTH_USER_MODEL, validators=[applications.accounts.models.is_staff_or_superuser], verbose_name='Оплату принял'),
        ),
    ]
