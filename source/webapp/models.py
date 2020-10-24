from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='pics', verbose_name='Фотография')
    signature = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='photos', verbose_name='Автор')

    def __str__(self):
        return f"{self.author} -- {self.signature}"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural= 'Фотографии'


