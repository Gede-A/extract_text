# from django.db import models

from djongo import models

class PDFfile(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
class DocumentAnalysis(models.Model):
    extraxt =models.ForeignKey(PDFfile, on_delete = models.CASCADE)
    text = models.TextField(models.Model)
    email = models.EmailField(unique=True)
    nouns = models.TextField()
    verbs = models.TextField()

    

    '''class Meta:
        verbo")
        verbose_names")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        ret_detail", kwargs={"pk": self.pk})

    nouns = models.TextField()
    verbs = models.TextField()'''
