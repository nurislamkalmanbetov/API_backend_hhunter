# Generated by Django 3.2 on 2023-12-29 04:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, upload_to='company_icons/', verbose_name='Изображение')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('country', models.CharField(blank=True, default='', max_length=128, verbose_name='страна')),
                ('description', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='Описание')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Работодатель')),
            ],
            options={
                'verbose_name': 'Работодатель',
                'verbose_name_plural': 'Работодатели',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('de', 'Немецкий'), ('ru', 'Руский'), ('en', 'Английский')], default='', max_length=2, verbose_name='Язык')),
                ('proficiency', models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], default='', max_length=2, verbose_name='Уровень владения')),
                ('picture', models.ImageField(blank=True, upload_to='vacancy_pics/')),
                ('required_positions', models.PositiveIntegerField(default=1, verbose_name='Требуемое количество мест')),
                ('required_positions_reviews', models.PositiveIntegerField(default=0, verbose_name='Колличество одобренных вакансии')),
                ('exchange', models.CharField(blank=True, choices=[('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR'), ('KGS', 'KGS'), ('KZT', 'KZT')], default='', max_length=10)),
                ('name', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('duty', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='Обязанности работника')),
                ('city', models.CharField(blank=True, default='', max_length=128, verbose_name='Город')),
                ('accomodation_type', models.CharField(blank=True, choices=[('yes', 'Предоставляется'), ('no', 'Не предоставляется')], default='', max_length=50, verbose_name='Жилье')),
                ('accomodation_cost', models.CharField(blank=True, default='', max_length=128, verbose_name='Стоимость жилья')),
                ('is_vacancy_confirmed', models.BooleanField(default=False, verbose_name='Прошел на вакансию')),
                ('insurance', models.BooleanField(default=False, verbose_name='Страховка')),
                ('transport', models.CharField(blank=True, default='', max_length=128, verbose_name='Транспорт')),
                ('contact_info', models.CharField(blank=True, default='', max_length=100, verbose_name='Контактные данные')),
                ('destination_point', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='Пункт назначения')),
                ('employer_dementions', models.CharField(blank=True, default='', max_length=128, verbose_name='Требования работодателя')),
                ('extra_info', models.CharField(blank=True, default='', max_length=255, verbose_name='Доп. информация')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('employer_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='core.employercompany', verbose_name='Компания работодателя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Работодатель')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
