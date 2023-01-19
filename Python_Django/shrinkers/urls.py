"""shrinkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# # from shortener.views import index, redirect_test, get_user
# from shortener.views import index, get_user
# # 회원가입 관련 추가
# from shortener.views import register
# debug_toolbar 추가
# import debug_toolbar
from shrinkers.settings import DEBUG
# if DEBUG :
#     import debug_toolbar

# # 로그인, 로그아웃 관련 추가
# from shortener.views import login_view, logout_view
# # 게시판 관련 추가
# from shortener.views import list_view
# # url_list 추가
# from shortener.views import url_list
# # url_create, url_change 추가
# from shortener.views import url_create, url_change

from shortener.urls.views import url_redirect

from shortener.urls.urls import router as url_router

# Ninja 프레임워크 추가
from ninja import NinjaAPI
from shortener.users.apis import user as user_router


# Swagger 관련
# 버전 패치로 url 미사용!
# from django.conf.urls import url
from django.urls import re_path as url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shrinkers API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


apis = NinjaAPI(title="Shrinkers API")
apis.add_router("/users/", user_router, tags=["Users"])


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index_1'),
    # # path('redirect', redirect_test),

    # # 여기서 입력된 user_id와 함께 get_user 함수 실행
    # path("get_user/<int:user_id>", get_user),

    # Django Debug Toolbar 경로 설정
    # path("__debug__/", include(debug_toolbar.urls)),

    # # 회원가입 관련 (/register로 이동하면 회원가입을 할 수 있도록 해줌!)
    # # 단일로 하는 경우 뒤에 /를 포함핮 않아도 된다! 이후에 추가할 경로가 있는경우 붙여줘야함!
    # path("register", register, name="register"),

    # # 로그인, 로그아웃 경로 추가
    # path("login", login_view, name="login"),
    # path("logout", logout_view, name="logout"),

    # # 게시판 경로 추가
    # path("list", list_view, name="list_view"),

    # url_list 추가
    # path("url_list", url_list, name="url_list"),

    # url 관련 경로 추가
    # path("urls", url_list, name="url_list"),
    # path("urls/create", url_create, name="url_create"),
    # path("urls/<str:action>/<int:url_id>", url_change, name="url_change"),

    path("", include("shortener.index.urls")),
    path("urls/", include("shortener.urls.urls")),

    path("api/", include(url_router.urls)),


    path("ninja-api/", apis.urls),


    # Swagger 관련
    url(r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger",
                                           cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc",
                                         cache_timeout=0), name="schema-redoc"),

    path("<str:prefix>/<str:url>", url_redirect),
]

# if DEBUG:
#     urlpatterns += [
#         path("__debug__/", include(debug_toolbar.urls)),  # Django Debug Tool
#     ]
