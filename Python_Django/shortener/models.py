# 가상환경의 경우 python 경로를 default로 python이 설치된 directory를 잡고 있어서 python 경로를 잡아주지 못해 경고가 발생한다!
# 가상환경의 인터프리터로 설정해주어야 함! venv\Scripts\python.exe
from django.db import models

# UserDetail 클래스를 만들기 위한 추가(처음에는 Django에서 제공하는 기본 모델을 활용하다 추후 추가 데이터 필요시 활용)
from django.contrib.auth.models import User as U
# AbstractUser를 설정할 때 사용!
# 다른 테이블이 추가된 상태에서 적용하기는 어려움! 초기에 가장 먼저 세팅할 때 활용
# from django.contrib.auth.models import AbstractUser


from django.contrib.gis.geoip2 import GeoIP2

# 게시판 만들기 관련
import string
import random


import itertools
from typing import Dict

from django.db.models.base import Model
from shortener.model_utils import dict_filter, dict_slice, location_finder


# Create your models here.

# 코드 중복을 최소화하기 위해 클래스 형태로 구성 후 상속시킴
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 추상화 객체로 만들어 테이블을 생성하지 않고 상속되어 사용됨
    class Meta:
        abstract = True


# class PayPlan(models.Model):
class PayPlan(TimeStampedModel):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    # updated_at = models.DateTimeField(auto_now=True)
    # create_at = models.DateTimeField(auto_now_add=True)


# 유료버전
# class Organization(models.Model):
class Organization(TimeStampedModel):
    class Industries(models.TextChoices):
        PERSONAL = "personal"
        RETAIL = "retail"
        MANUFCTURING = "manufacturing"
        IT = "it"
        OTHERS = 'others'
    name = models.CharField(max_length=50)
    industry = models.CharField(
        max_length=15, choices=Industries.choices, default=Industries.OTHERS)
    pay_plan = models.ForeignKey(
        PayPlan, on_delete=models.DO_NOTHING, null=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # create_at = models.DateTimeField(auto_now_add=True)


# User 만들기

# AbstractUser에 추가정보를 넣는 경우 (하나의 테이블에 쓸 수 있다!)
# settings.py에 AUTH_USER_MODEL = "shortener.Users" 추가
# 유저 테이블이 상속 받으면서 기존 유저 테이블이 쓸모가 없어지므로 인증을 위해 어떤 유저 모델을 쓸지 정의해주어야 함
# class Users(AbstractUser):
class Users(models.Model):
    user = models.OneToOneField(U, on_delete=models.CASCADE)    #
    full_name = models.CharField(max_length=100, null=True)
    telegram_username = models.CharField(max_length=100, null=True)
    # pay_plan = models.ForeignKey(
    #     PayPlan, on_delete=models.DO_NOTHING, null=True)    # null = True를 붙여주지 않으면 계정 생성 시 django.db.utils.IntegrityError: NOT NULL constraint failed 에러 발생
    url_count = models.IntegerField(default=0)
    organization = models.ForeignKey(
        Organization, on_delete=models.DO_NOTHING, null=True)

# # UserDetail 클래스 만들기 (두 개의 테이블로 나누어 쓸 때 활용)
# class UserDetail(models.Model):
#     # AbstractUser과 함께 사용할 시 해당 클래스를 반영해주어야 한다
#     user = models.OneToOneField(Users, on_delete=models.CASCADE)
#     # 기존
#     # user = models.OneToOneField(U, on_delete=models.CASCADE)
#     pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)


# 유저 이메일 증명하기
# class EmailVerification(AbstractUser):
class EmailVerification(TimeStampedModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    # updated_at = models.DateTimeField(auto_now=True)
    # create_at = models.DateTimeField(auto_now_add=True)


# URL 카테고리 나누기
# class Categories(models.Model):
class Categories(TimeStampedModel):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(
        Organization, on_delete=models.DO_NOTHING, null=True)   # ForeignKey에 null이 가능하도록 하는 것은 꼬일 위험이 있으므로 지양
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    # updated_at = models.DateTimeField(auto_now=True)
    # create_at = models.DateTimeField(auto_now_add=True)


# class ShortenedUrls(models.Model):
class ShortenedUrls(TimeStampedModel):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE = "web"
        TELEGRAM = "telegram"

    def rand_string():
        str_pool = string.digits + string.ascii_letters
        return ("".join([random.choice(str_pool) for _ in range(6)])).lower()

    def rand_letter():
        str_pool = string.ascii_letters
        return random.choice(str_pool).lower()

    nick_name = models.CharField(max_length=100)
    # created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING, null=True)
    # prefix = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50, default=rand_letter)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    click = models.BigIntegerField(default=0)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    create_via = models.CharField(
        max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(null=True)

    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "prefix",
                    "shortened_url",
                ]
            ),
        ]

    def clicked(self):
        self.click += 1
        self.save()
        return self


class Statistic(TimeStampedModel):
    class ApproachDevice(models.TextChoices):
        PC = "PC"
        MOBILE = "mobile"
        TABLET = "tablet"

    shortened_url = models.ForeignKey(ShortenedUrls, on_delete=models.CASCADE)
    ip = models.CharField(max_length=15)
    web_browser = models.CharField(max_length=15)
    device = models.CharField(max_length=6, choices=ApproachDevice.choices)
    device_os = models.CharField(max_length=30)
    country_code = models.CharField(max_length=2, default="XX")
    country_name = models.CharField(max_length=100, default="UNKNOWN")

    custom_params = models.JSONField(null=True)

    # def record(self, request, url: ShortenedUrls):
    def record(self, request, url: ShortenedUrls, params: Dict):
        self.shortened_url = url
        # 장고가 기본으로 가지고 있는 주소 (로드밸런서가 있는 경우 사용 불가! AWS 등에서 고객 주소를 헤더로 제공하는 것을 활용해야한다!)
        self.ip = request.META["REMOTE_ADDR"]
        self.web_browser = request.user_agent.browser.family
        # self.device = self.ApproachDevice.MOBILE if request.user_agent.is_mobile else self.ApproachDevice.TABLET if request.user_agent.is_tablet else self.ApproachDevice.PC
        self.device = (
            self.ApproachDevice.MOBILE
            if request.user_agent.is_mobile
            else self.ApproachDevice.TABLET
            if request.user_agent.is_tablet
            else self.ApproachDevice.PC
        )
        self.device_os = request.user_agent.os.family

        t = TrackingParams.get_tracking_params(url.id)
        self.custom_params = dict_slice(dict_filter(params, t), 5)

        try:
            # country = GeoIP2().country(self.ip)
            country = location_finder(request)
            self.country_code = country.get("country_code", "XX")
            self.country_name = country.get("country_name", "UNKNOWN")
        except:
            pass
        url.clicked()
        self.save()


class TrackingParams(TimeStampedModel):
    shortened_url = models.ForeignKey(ShortenedUrls, on_delete=models.CASCADE)
    params = models.CharField(max_length=20)

    @classmethod
    def get_tracking_params(cls, shortened_url_id):
        # flat이 True일 때 -> ["email_id", "ref_by"]    단순히 리스트로 받기 위해 True 사용!
        # flat이 False일 때 -> [{"params" : "email_id"}, {"params" : "ref_by"}]
        return cls.objects.filter(shortened_url_id=shortened_url_id).values_list("params", flat=True)
    # def get_tracking_params(cls, shortened_url_id: int):
    #     return TrackingParams.objects.filter(shortened_url_id=shortened_url_id).values_list("params", flat=True)
