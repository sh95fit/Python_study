from django.contrib import admin
from shortener.models import PayPlan

# Register your models here.

# Django 관리자 페이지에 model 등록
admin.site.register(PayPlan)
