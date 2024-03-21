from django.contrib import admin

# Register your models here.
from .models import DocumentAnalysis, PDFfile
admin.site.register(DocumentAnalysis)
admin.site.register(PDFfile)

