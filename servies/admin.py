from django.contrib import admin
from servies.models import Servies,ContectUs
# Register your models here.

#sevies model filed (project Details)
class ServiesAdmin(admin.ModelAdmin):
    list_display=('servies_icon','servies_title','servies_des','servies_git_url')

admin.site.register(Servies,ServiesAdmin)

class ContectUsAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_mobile','user_email','user_message')

admin.site.register(ContectUs,ContectUsAdmin)