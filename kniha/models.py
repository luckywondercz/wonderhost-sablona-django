from django.db import models


class Vzkaz(models.Model):
    jmeno = models.CharField("jméno", max_length=80)
    text = models.TextField("vzkaz", max_length=2000)
    vytvoreno = models.DateTimeField("vytvořeno", auto_now_add=True)
    zverejneno = models.BooleanField("zveřejněno", default=True)

    class Meta:
        ordering = ["-vytvoreno"]
        verbose_name = "vzkaz"
        verbose_name_plural = "vzkazy"

    def __str__(self):
        return f"{self.jmeno}: {self.text[:40]}"
