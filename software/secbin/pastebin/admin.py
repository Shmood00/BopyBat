from django.contrib import admin
from .models import Bopie
from .models import Profile

# Register your models here.

class AppAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Bopie, AppAdmin)
admin.site.register(Profile, AppAdmin)
