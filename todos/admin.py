from django.contrib import admin
from .models import Category, Todo

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = (id,)

admin.site.register(Todo)
admin.site.register(Category, CategoryAdmin)