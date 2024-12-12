import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Contact


@admin.action(description="Exportar para Excel")
def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="contacts.csv"'

    writer = csv.writer(response)
    writer.writerow(["Nome", "E-mail", "Mensagem", "Data de Criação"])

    for contact in queryset:
        writer.writerow(
            [contact.name, contact.email, contact.message, contact.created_at]
        )

    return response


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    actions = [export_to_excel]
