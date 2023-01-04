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
# from shortener.views import index, redirect_test, get_user
from shortener.views import index, get_user
# debug_toolbar 추가
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index_1'),
    # path('redirect', redirect_test),

    # 여기서 입력된 user_id와 함께 get_user 함수 실행
    path("get_user/<int:user_id>", get_user),

    # Django Debug Toolbar 경로 설정
    path("__debug__/", include(debug_toolbar.urls)),
]
