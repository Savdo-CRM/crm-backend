from django.contrib import admin

# Register your models here.
from api.v1.company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'u_name', 'inn', 'subdomain', 'created_at')
    list_display_links = ('id', 'name')
