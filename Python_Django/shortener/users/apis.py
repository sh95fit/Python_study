from django.contrib.auth import login
from shortener.schemas import Message, UserRegisterBody, Users as U
from django.contrib.auth.models import User

from typing import List
# from shortener.schemas import Users as U
from shortener.models import Users
from ninja.router import Router

from shortener.schemas import TelegramUpdateSchema

from shortener.urls.decorators import admin_only

user = Router()


@user.get("", response=List[U])
@admin_only
# @admin_only
def get_user(request):
    # Django ORM 사용!
    a = Users.objects.all()
    return list(a)


@user.post("", response={201: None})
def update_telegram_username(request, body: TelegramUpdateSchema):
    # user = Users.objects.filter(user_id=request.user.id)
    user = Users.objects.filter(user_id=request.users_id)
    if not user.exists():
        return 404, {"msg": "User not found"}
    user.update(telegram_username=body.username)
    return 201, None


@user.post("register", response={201: None, 409: Message})
def user_register(request, body: UserRegisterBody):
    email_check = User.objects.filter(email=body.email)
    if email_check.exists():
        return 409, {"msg": "이미 사용 중인 이메일 입니다."}
    user = body.register()
    login(request, user)
    return 201, None
