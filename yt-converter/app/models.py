from django.db import models


class YoutubeURL(models.Model):
    urls = models.TextField("URL")
    create_day = models.DateTimeField(verbose_name="コンバート実行日", auto_now_add=True)

    def __str__(self):
        return self.url
