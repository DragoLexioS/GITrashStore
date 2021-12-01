"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class Anketa(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=50)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=50)
    email = forms.EmailField(label='Ваш email', min_length=10)
    play = forms.ChoiceField(label='Вы играете в Genshin Impact?', choices=[('1', 'Да'),('2', 'Нет')], widget=forms.RadioSelect, initial=1)
    top = forms.ChoiceField(label='На сколько вы оцените удобство сайта?', choices=(('1', 'Плохо'), ('2', 'Хуже среднего'), ('3', 'Нормально'), ('4', 'Хорошо'), ('5', 'Отлично')), initial=1)
    top2 = forms.ChoiceField(label='На сколько вы оцениете разнообразие товаров?', choices=(('1', 'Мало'), ('2', 'Средне'), ('3', 'Много')), initial=1)
    notice = forms.BooleanField(label='Хотите получать новости сайта на ваш e-mail?', required=False)
    message = forms.CharField(label='Опишите Ваши пожелания', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text
class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка",}