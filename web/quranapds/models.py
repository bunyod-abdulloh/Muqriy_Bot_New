from django.db import models


class QuranAudioPhotoDoc(models.Model):
    sequence = models.IntegerField(verbose_name="Tartib raqam")
    sura_name = models.CharField(verbose_name="Sura nomi", max_length=60)
    total_verses = models.IntegerField(verbose_name="Oyatlar soni")
    link = models.CharField(verbose_name="Link", max_length=200, null=True, blank=True)
    zip = models.CharField(verbose_name="ZIP ID", max_length=200, null=True, blank=True)
    audio = models.CharField(verbose_name="Audio ID", max_length=200, null=True, blank=True)
    photo = models.CharField(verbose_name="Photo ID", max_length=200, null=True, blank=True)
    docs = models.CharField(verbose_name="Document ID", max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Qur'oni Karim"
        verbose_name_plural = "Qur'oni Karim"
