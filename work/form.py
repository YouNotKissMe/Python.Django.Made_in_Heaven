from .models import Publication
from django.forms import ModelForm, modelform_factory
from django.contrib.auth.models import User


class PublictionForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'category', 'author', 'synopsis', 'file')


# verbouse_name_form = {'first_name': 'Имя',
#                       'password': 'Пароль',
#                       'last_login': 'Логин',
#                       'last_name': 'Фамилия',
#                       'email': 'Email', }
#
# Registration_form = modelform_factory(User, fields=(
#     'first_name', 'last_name', 'username', 'password', 'email'),
#                                       labels=verbouse_name_form)
