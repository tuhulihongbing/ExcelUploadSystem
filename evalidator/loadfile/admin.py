from django.contrib import admin
from loadfile.models import Folder,Excelfile

# Register your models here.
class FolderAdmin(admin.ModelAdmin):
    fields = ('name', 'parent',)
    list_display = ('name', 'pub_date','parent')
    prepopulated_fields = {"name": ("name",)}

class ExcelfileAdmin(admin.ModelAdmin):
    fields = ('name','folder','path',)
    list_display = ('name', 'pub_date','folder','path',)
    prepopulated_fields = {"name": ("name",)}

admin.site.register(Folder, FolderAdmin)
admin.site.register(Excelfile, ExcelfileAdmin)