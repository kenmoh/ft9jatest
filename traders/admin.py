from django.contrib import admin
from .models import Trade, User


class TradeInline(admin.TabularInline):
    model = Trade
    readonly_fields = ['user', 'timestamp', 'profit_or_loss']
    extra = 0

    # Disables the delete option
    def has_delete_permission(self, request, obj=None):
        return False

    # Disables the ability to add new trades from the user admin page
    def has_add_permission(self, request, obj=None):
        return False


class TradeAdmin(admin.ModelAdmin):
    list_display = ['user', 'profit_or_loss', 'timestamp']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'balance']
    inlines = [TradeInline]
    exclude = ('email', 'is_active',
               'is_staff', 'date_joined',
               'password', 'first_name', 'last_name',
               'user_permissions', 'groups',
               'last_login', 'is_superuser'

               )
    readonly_fields = ['username', 'balance']
    #


admin.site.register(User, UserAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.site_header = 'FT9ja Test'
