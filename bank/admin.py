from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SimpleUser)
admin.site.register(BankAccount)
admin.site.register(BankCard)
admin.site.register(CardTransaction)