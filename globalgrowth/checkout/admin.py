from django.contrib import admin
from .models import MpesaPayment

@admin.register(MpesaPayment)
class MpesaPaymentAdmin(admin.ModelAdmin):
    list_display = ('mpesa_receipt_number', 'phone_number', 'amount', 'transaction_date', 'result_code')
    list_filter = ('result_code', 'transaction_date')
    search_fields = ('mpesa_receipt_number', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')