from rest_framework.permissions import OR
# from shortener.models import Organization, PayPlan
from ninja import Schema
from django.contrib.auth.models import User as U
from ninja.orm import create_schema

from pydantic.networks import EmailStr  # pip install 'pydantic[email]'
from pydantic import validator
from uuid import uuid4
from shortener.models import Organization
from shortener.models import Users as _users
from django.contrib.auth.hashers import make_password


# create_schema를 통해 모델을 그대로 가져와 활용할 수 있음!
OrganizationSchema = create_schema(Organization)
# 제외할 항목이 있는 경우!
# OrganizationSchema = create_schema(Organization, exclude=["password", "secret_key"])


class Users(Schema):
    id: int
    full_name: str = None
    organization: OrganizationSchema = None


class TelegramUpdateSchema(Schema):
    username: str


class Message(Schema):
    msg: str


class TelegramSendMsgBody(Schema):
    msg: str


class UserRegisterBody(Schema):
    email: EmailStr
    name: str
    password: str
    policy: bool

    @validator('password')
    def password_len_check(cls, v):
        if v and len(v) >= 8:
            return v
        raise ValueError(f"패스워드는 8자 이상 필수 입니다.")

    @validator('policy')
    def policy_check(cls, v):
        if v:
            return v
        raise ValueError(f"이용약관은 필수 동의 사항 입니다.")

    def register(self):

        new_user = U()
        new_user.username = uuid4()
        new_user.password = make_password(self.password)
        new_user.email = self.email
        new_user.save()

        new_users = _users()
        new_users.user = new_user
        new_users.full_name = self.name
        new_users.save()

        return new_user
