from django.contrib import admin
from .models import Blog, User, Comment, Portfolio, Setting, Contact

# Register your models here.

admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Portfolio)
admin.site.register(Setting)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
