# Generated by Django 3.2 on 2024-02-15 10:34

import applications.accounts.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to=applications.accounts.utils.user_directory_path, validators=[django.core.validators.validate_image_file_extension], verbose_name='Фото профиля')),
                ('first_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Имя на латинице')),
                ('first_name_ru', models.CharField(blank=True, default='', max_length=255, verbose_name='Имя на кириллице')),
                ('first_name_de', models.CharField(blank=True, default='', max_length=255, verbose_name='Имя на немецком')),
                ('last_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Фамилия на латинице')),
                ('last_name_ru', models.CharField(blank=True, default='', max_length=255, verbose_name='Фамилия на кирилице')),
                ('last_name_de', models.CharField(blank=True, default='', max_length=255, verbose_name='Фамилия на немецком')),
                ('middle_name', models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество на латинице')),
                ('middle_name_ru', models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество на кирилице')),
                ('middle_name_de', models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество на немецком')),
                ('gender_ru', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=50, verbose_name='Пол на кириллице')),
                ('gender_en', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, verbose_name='Пол на латинице')),
                ('gender_de', models.CharField(blank=True, choices=[('Männlich', 'Männlich'), ('Weiblich', 'Weiblich')], max_length=50, verbose_name='Пол на немецком')),
                ('nationality_ru', models.CharField(blank=True, max_length=50, verbose_name='Гражданство на кирилице')),
                ('nationality_en', models.CharField(blank=True, max_length=50, verbose_name='Гражданство на латинице')),
                ('nationality_de', models.CharField(blank=True, max_length=50, verbose_name='Гражданство на немецком')),
                ('birth_country_ru', models.CharField(blank=True, default='', max_length=50, verbose_name='Страна рождения на кириллице')),
                ('birth_country_en', models.CharField(blank=True, default='', max_length=50, verbose_name='Страна рождения на латинице')),
                ('birth_country_de', models.CharField(blank=True, default='', max_length=50, verbose_name='Страна рождения на немецком')),
                ('birth_region_ru', models.CharField(blank=True, default='', max_length=50, verbose_name='Область рождения на кириллице')),
                ('birth_region_en', models.CharField(blank=True, default='', max_length=50, verbose_name='Область рождения на латинице')),
                ('birth_region_de', models.CharField(blank=True, default='', max_length=50, verbose_name='Область рождения на немецком')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Номер телефона')),
                ('whatsapp_phone_number', models.CharField(blank=True, max_length=50, verbose_name='Номер Whatsapp')),
                ('german', models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=50, verbose_name='Знание немецкого языка')),
                ('english', models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=50, verbose_name='Знание английского языка')),
                ('russian', models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=50, verbose_name='Знание русского языка')),
            ],
            options={
                'verbose_name': 'Профиль соискателя',
                'verbose_name_plural': 'Профили соискателей',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_rating', models.IntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], default=1, verbose_name='Значение рейтинга')),
                ('rating_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата рейтинга')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_reset_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='whatsapp_phone',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('is_employer', 'Работодатель'), ('is_employee', 'Соискатель')], default=django.utils.timezone.now, max_length=50, verbose_name='Роль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Понедельник')),
                ('tuesday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Вторник')),
                ('wednesday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Среда')),
                ('thursday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Четверг')),
                ('friday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Пятница')),
                ('saturday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Суббота')),
                ('sunday', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], default='DAY', max_length=50, verbose_name='Воскресенье')),
                ('custom', models.CharField(blank=True, choices=[('DAY', 'День (08:00-20:00)'), ('EVENING', 'Ночь (17:00-01:00)'), ('NIGHT', 'Вечер (20:00-08:00)'), ('ANY', 'Свой график')], max_length=50, verbose_name='Свой график')),
                ('custom_start_time', models.TimeField(blank=True, help_text='Введите время в формате HH:MM', null=True, verbose_name='Начало работы (Свой график)')),
                ('custom_end_time', models.TimeField(blank=True, help_text='Введите время в формате HH:MM', null=True, verbose_name='Окончание работы (Свой график)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_times', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'Графики работ',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_company', models.CharField(blank=True, choices=[('Hotel', 'Отель'), ('Restaurant', 'Ресторан'), ('Cafe', 'Кафе'), ('Factory', 'Фабрика'), ('Salon', 'Салон'), ('Sales', 'Продажи'), ('Other', 'Другое')], max_length=50, verbose_name='Тип компании')),
                ('company', models.CharField(blank=True, max_length=255, verbose_name='Компания')),
                ('position', models.CharField(blank=True, choices=[('Manager', 'Менеджер'), ('Waiter', 'Официант'), ('Cook', 'Повар'), ('Seller', 'Продавец'), ('Driver', 'Водитель'), ('Cashier', 'Кассир'), ('Builder', 'Строитель'), ('Butcher', 'Мясник'), ('Backer', 'Пекарь'), ('Other', 'Другое')], max_length=50, verbose_name='Должность')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('responsibilities', models.TextField(blank=True, verbose_name='Обязанности')),
                ('country', models.CharField(blank=True, max_length=255, verbose_name='Страна')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работы',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=255, verbose_name='Название университета на кириллице')),
                ('name_en', models.CharField(blank=True, max_length=255, verbose_name='Название университета на латинице')),
                ('name_de', models.CharField(blank=True, max_length=255, verbose_name='Название университета на немецком')),
                ('degree_type_ru', models.CharField(blank=True, choices=[('Бакалавриат', 'Бакалавриат'), ('Магистратура', 'Магистратура')], max_length=255, verbose_name='Тип обучения на кириллице')),
                ('degree_type_en', models.CharField(blank=True, choices=[('Bachelor', 'Bachelor'), ('Master', 'Master')], max_length=255, verbose_name='Тип обучения на латинице')),
                ('degree_type_de', models.CharField(blank=True, choices=[('Bachelor', 'Bachelor'), ('Master', 'Master')], max_length=255, verbose_name='Тип обучения на немецком')),
                ('faculty_ru', models.CharField(blank=True, max_length=255, verbose_name='Факультет на кириллице')),
                ('faculty_en', models.CharField(blank=True, max_length=255, verbose_name='Факультет на латинице')),
                ('faculty_de', models.CharField(blank=True, max_length=255, verbose_name='Факультет на немецком')),
                ('address_ru', models.CharField(blank=True, max_length=255, verbose_name='Адрес на кириллице')),
                ('address_en', models.CharField(blank=True, max_length=255, verbose_name='Адрес на латинице')),
                ('address_de', models.CharField(blank=True, max_length=255, verbose_name='Адрес на немецком')),
                ('phone_number_university_ru', models.CharField(blank=True, max_length=50, verbose_name='Номер телефона университета')),
                ('email_university', models.EmailField(blank=True, max_length=254, verbose_name='Email университета')),
                ('website_university', models.URLField(blank=True, verbose_name='Сайт университета')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Год поступления в университет')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Год окончания университета')),
                ('total_years', models.IntegerField(blank=True, null=True, verbose_name='Общее количество лет')),
                ('kurs_year', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('Other', 'Другое')], max_length=5, verbose_name='Курс')),
                ('start_holiday', models.DateField(blank=True, null=True, verbose_name='Начало каникул')),
                ('end_holiday', models.DateField(blank=True, null=True, verbose_name='Конец каникул')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'Университет',
                'verbose_name_plural': 'Университеты',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Текст отзыва')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_reviews', to='accounts.user', verbose_name='Работодатель')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.rating')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_given', to='accounts.user', verbose_name='Работодатель'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_received', to='accounts.profile', verbose_name='Соискатель'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.user', verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField(blank=True, null=True, verbose_name='Общая сумма')),
                ('total_amount_in_words', models.CharField(blank=True, max_length=255, verbose_name='Общая сумма прописью')),
                ('initial_fee', models.IntegerField(blank=True, null=True, verbose_name='Первоначальный взнос')),
                ('initial_fee_in_words', models.CharField(blank=True, max_length=255, verbose_name='Первоначальный взнос прописью')),
                ('average_fee', models.IntegerField(blank=True, null=True, verbose_name='Средний взнос')),
                ('average_fee_in_words', models.CharField(blank=True, max_length=255, verbose_name='Средний взнос прописью')),
                ('final_fee', models.IntegerField(blank=True, null=True, verbose_name='Окончательный взнос')),
                ('final_fee_in_words', models.CharField(blank=True, max_length=255, verbose_name='Окончательный взнос прописью')),
                ('debt', models.IntegerField(blank=True, null=True, verbose_name='Долг')),
                ('debt_in_words', models.CharField(blank=True, max_length=255, verbose_name='Долг прописью')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('payment_accepted_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата принятия оплаты')),
                ('payment_accepted', models.BooleanField(default=False, verbose_name='Оплата принята')),
                ('payment_accepted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments_accepted', to='accounts.user', verbose_name='Оплату принял')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
        migrations.CreateModel(
            name='PassportAndTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_id_passport', models.CharField(blank=True, max_length=50, verbose_name='Номер ID паспорта')),
                ('inn', models.CharField(blank=True, max_length=50, verbose_name='ИНН')),
                ('passport_number', models.CharField(blank=True, max_length=50, verbose_name='Номер загран паспорта')),
                ('passport_date_of_issue', models.DateField(blank=True, null=True, verbose_name='Дата выдачи паспорта')),
                ('passport_end_time', models.DateField(blank=True, null=True, verbose_name='Дата окончания загранпаспорта')),
                ('pnr_code', models.CharField(blank=True, max_length=50, verbose_name='PNR код')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to=applications.accounts.utils.user_directory_path, verbose_name='PDF файл')),
                ('term_date_time', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время термина')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passport_data', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'Паспортные данные и термин',
                'verbose_name_plural': 'Паспортные данные и термины',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=50, verbose_name='Номер телефона')),
                ('participant', models.CharField(blank=True, max_length=50, verbose_name='Участник')),
                ('flight_date', models.DateField(blank=True, null=True, verbose_name='Дата полета в Германию')),
                ('steuer_id', models.CharField(blank=True, max_length=50, verbose_name='Steuer ID - Налоговый номер')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('stage', models.CharField(blank=True, max_length=50, verbose_name='Стадия сделки')),
                ('program', models.CharField(blank=True, max_length=50, verbose_name='Программа')),
                ('contract_date', models.DateField(blank=True, null=True, verbose_name='Дата заключения договора')),
                ('inn', models.CharField(blank=True, max_length=50, verbose_name='ИНН')),
                ('comment', models.CharField(blank=True, max_length=50, verbose_name='Комментарий')),
                ('hijab', models.CharField(blank=True, max_length=50, verbose_name='Носит Хиджаб')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='accounts.profile', verbose_name='Соискатель')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
        migrations.AddIndex(
            model_name='university',
            index=models.Index(fields=['user'], name='accounts_un_user_id_51349f_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['user', 'gender_en', 'german', 'russian'], name='accounts_pr_user_id_20decd_idx'),
        ),
        migrations.AddIndex(
            model_name='passportandterm',
            index=models.Index(fields=['user'], name='accounts_pa_user_id_41adac_idx'),
        ),
    ]