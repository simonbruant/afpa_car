from django.contrib import admin
from .models import ZipCode_City, Adress_User, Address, ZipCode, City

class ZipCodeInline(admin.TabularInline):        
    model = ZipCode_City
    verbose_name = "Code Postal"
    verbose_name_plural = "Codes Postaux"
    extra= 1

class ZipCodeAdmin(admin.ModelAdmin):
    inlines = (ZipCodeInline, )

class CityInline(admin.TabularInline):
    model = ZipCode_City
    verbose_name = "Ville"
    verbose_name_plural = "Villes"
    extra = 1

class CityAdmin(admin.ModelAdmin):
    inlines = (CityInline,)

# ------------------------------

class UserInLine(admin.TabularInline): # autre variante : admin.StackedInline
    model = Adress_User
    verbose_name = "Utilisateur de cette adresse"
    verbose_name_plural = "Utilisateurs de cette adresse"
    fk_name = "address"
    extra = 0


class AdressAdmin(admin.ModelAdmin):
    inlines = (UserInLine,)
    
    list_display = ('city', 'zip_code', 'street', 'adress_label', 'get_users' )

    def get_users(self, obj):
        return " ; ".join([u.get_full_name() for u in obj.users.all()])
    get_users.short_description = 'Utilisateurs'

    search_fields = ('city__city_name', 'zip_code__zip_code', 'street', 'adress_label', 'users__first_name', 'users__last_name', )
                                        #Pourquoi zip_code__zip_code et non zipcode__zip_code ?

# Register your models here.
admin.site.register(Address, AdressAdmin)
admin.site.register(ZipCode, ZipCodeAdmin)
admin.site.register(City, CityAdmin)
