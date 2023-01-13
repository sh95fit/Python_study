from django.contrib import admin
from shortener.models import PayPlan
from shortener.models import Users
from shortener.models import Statistic
# Register your models here.

# Django 관리자 페이지에 model 등록
admin.site.register(PayPlan)
admin.site.register(Users)
admin.site.register(Statistic)
