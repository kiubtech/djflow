from django.contrib import admin
from .models import Account, Transaction, Category, TransactionComment


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'name', 'timestamp', 'is_active')


@admin.register(Transaction)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'name', 'amount', 'date')


@admin.register(TransactionComment)
class TransactionCommentAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'transaction', 'timestamp')
    search_fields = ['created_by__first_name', 'created_by__last_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
