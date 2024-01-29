# Generated by Django 3.2 on 2024-01-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_invitation_is_works'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.branch', verbose_name='Филиал'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.positionemployee', verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]
