# Generated by Django 4.0.3 on 2022-03-24 19:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата опубликования работы')),
                ('category', models.CharField(choices=[('informatics', 'информатика'), ('chemistry', 'химия'), ('biology', 'биология')], max_length=60, verbose_name='Категория')),
                ('synopsis', models.TextField(verbose_name='Краткая информация о работе')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'txt', 'pdf'])], verbose_name='Опубликованная работа')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пубикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['date'],
            },
        ),
    ]
