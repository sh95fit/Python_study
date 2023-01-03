
# 가상환경의 경우 python 경로를 default로 python이 설치된 directory를 잡고 있어서 python 경로를 잡아주지 못해 경고가 발생한다!
# 가상환경의 인터프리터로 설정해주어야 함! venv\Scripts\python.exe
from django.db import models

# UserDetail 클래스를 만들기 위한 추가(처음에는 Django에서 제공하는 기본 모델을 활용하다 추후 추가 데이터 필요시 활용)
from django.contrib.auth.models import User as U
# AbstractUser를 설정할 때 사용!
from django.contrib.auth.models import AbstractUser


# Create your models here.


class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)


# User 만들기

# AbstractUser에 추가정보를 넣는 경우 (하나의 테이블에 쓸 수 있다!)
# settings.py에 AUTH_USER_MODEL = "shortener.Users" 추가
# 유저 테이블이 상속 받으면서 기존 유저 테이블이 쓸모가 없어지므로 인증을 위해 어떤 유저 모델을 쓸지 정의해주어야 함
class Users(AbstractUser):
    pay_plan = models.ForeignKey(
        PayPlan, on_delete=models.DO_NOTHING, null=True)    # null = True를 붙여주지 않으면 계정 생성 시 django.db.utils.IntegrityError: NOT NULL constraint failed 에러 발생


# UserDetail 클래스 만들기 (두 개의 테이블로 나누어 쓸 때 활용)
class UserDetail(models.Model):
    # AbstractUser과 함께 사용할 시 해당 클래스를 반영해주어야 한다
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    # 기존
    # user = models.OneToOneField(U, on_delete=models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
