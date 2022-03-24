from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

category = [('informatics', 'информатика'),
            ('chemistry', 'химия'),
            ('biology', 'биология')]


class Publication(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    date = models.DateField(verbose_name='Дата опубликования работы', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.CharField(verbose_name='Категория', choices=category, max_length=60)
    synopsis = models.TextField(verbose_name='Краткая информация о работе')
    file = models.FileField(verbose_name='Опубликованная работа',
                            validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'txt', 'pdf'])])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
        verbose_name = 'Пубикация'
        verbose_name_plural = 'Публикации'
