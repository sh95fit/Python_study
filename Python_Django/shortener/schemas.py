from rest_framework.permissions import OR
from shortener.models import Organization, PayPlan
from ninja import Schema
from django.contrib.auth.models import User as U
from ninja.orm import create_schema


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
