from django.contrib import admin
from .models import User,Profile,Driverprofile,Vehicle,Reservation
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserPorfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdminConfig(UserAdmin):
    model = User
    #inlines=[UserPorfileInline]
    search_fields = ('email','first_name','last_name','middle_name','contact_no')
    list_filter = ('email','first_name','last_name','middle_name','contact_no','is_active','is_superuser')
    list_display = ('email','first_name','last_name','middle_name','contact_no','role','is_active','is_superuser','is_staff','is_student','last_login')
    ordering = ('email',)
    fieldsets = (
        (None,{'fields':('email',)}),
        ('Permission',{'fields':('is_active','is_superuser','is_staff','is_student','is_driver','last_login','role','groups')}),
        ('Personal',{'fields':('first_name','last_name','middle_name','contact_no')}),
    )
    filter_horizontal = ('groups', 'user_permissions',)

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','password1','password2','first_name','last_name','middle_name','contact_no')}
            ),
    )
admin.site.register(User,UserAdminConfig)
admin.site.register(Profile)
admin.site.register(Driverprofile)
admin.site.register(Vehicle)
admin.site.register(Reservation)
