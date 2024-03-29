# from shortener.models import ShortenedUrls, Users
from shortener.models import ShortenedUrls, Statistic, Users
# from shortener.urls.serializers import UserSerializer, UrlListSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# from rest_framework import generics
from rest_framework.response import Response

# from shortener.utils import MsgOk
from django.http.response import Http404
from django.shortcuts import get_object_or_404

from shortener.urls import serializers
# from shortener.urls.serializers import UrlListSerializer, UserSerializer, UrlCreateSerializer
from shortener.urls.serializers import BrowerStatSerializer, UrlCreateSerializer, UserSerializer, UrlListSerializer

from rest_framework import status

from rest_framework.decorators import renderer_classes
# from shortener.utils import MsgOk, url_count_changer
from shortener.utils import MsgOk, get_kst, url_count_changer

from rest_framework.renderers import JSONRenderer

from rest_framework.decorators import action

from datetime import timedelta
from django.db.models.aggregates import Count, Min


# 캐시 적용을 위한 내장 프레임워크 활용
from django.core.cache import cache

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allow users to be viewed or edited.
#     """


class UrlListView(viewsets.ModelViewSet):
    queryset = ShortenedUrls.objects.order_by("-created_at")
    # queryset = ShortenedUrls.objects.all().order_by("-created_at")
    serializer_class = UrlListSerializer
    # permissions.IsAdminUser : DRF에서는 별도로 admin_only 데코레이터을 사용하지 않아도 어드민 판단이 가능하다!
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # POST METHOD
        serializer = UrlCreateSerializer(data=request.data)
        # print(serializer.is_valid())
        if serializer.is_valid():
            # cache.delete(f"url_lists_{request.users_id}")
            rtn = serializer.create(request, serializer.data)
            return Response(UrlListSerializer(rtn).data, status=status.HTTP_201_CREATED)
        pass

    def retrieve(self, request, pk=None):
        # Detail GET
        # queryset = self.get_queryset().filter(pk=pk)
        # serializer = UrlListSerializer(queryset, many=True)
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = UrlListSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # PUT METHOD
        pass

    def partial_update(self, request, pk=None):
        # PATCH METHOD
        pass

    @renderer_classes([JSONRenderer])
    def destroy(self, request, pk=None):
        # DELETE METHOD
        # pass
        # queryset = self.get_queryset().filter(pk=pk, creator_id=request.user.id)
        # queryset = self.get_queryset().filter(pk=pk, creator_id=request.users_id)
        queryset = (
            self.get_queryset().filter(pk=pk, creator_id=request.users_id)
            if not request.user.is_superuser
            else self.get_queryset().filter(pk=pk)
        )
        # print(pk, request.user.id)
        if not queryset.exists():
            raise Http404
        # print(123123)
        queryset.delete()
        # 쿼리가 끝나면 캐시를 지워주도록 설정
        # cache.delete(f"url_lists_{request.users_id}")
        url_count_changer(request, False)
        return MsgOk()

    def list(self, request):
        # GET ALL
        # queryset = self.get_queryset().all()
        # queryset = self.get_queryset().filter(creator_id=request.user.id).all()
        # queryset = cache.get('url_list')
        # queryset = cache.get('url_lists')
        # queryset = cache.get(f"url_lists_{request.users_id}")
        # if not queryset:
        #     queryset = self.get_queryset().filter(creator_id=request.user.id).all()
        # 쿼리 캐시 방법
        # cache.set('url_list', queryset, 300)
        # cache.set('url_lists', queryset, 20)
        # cache.set(f"url_lists_{request.users_id}", queryset, 20)
        queryset = self.get_queryset().filter(creator_id=request.users_id).all()
        serializer = UrlListSerializer(queryset, many=True)
        return Response(serializer.data)

    # 디테일 뷰
    @action(detail=True, methods=["get", "post"])
    # @action(detail=True, methods=['get', 'post'])
    # def add_click(self, request, pk=None):
    #     # if request.method == "POST":
    #     queryset = self.get_queryset().filter(pk=pk, creator_id=request.user.id)
    def add_browser_today(self, request, pk=None):
        # queryset = self.get_queryset().filter(pk=pk, creator_id=request.user.id).first()
        queryset = self.get_queryset().filter(pk=pk, creator_id=request.users_id).first()
        new_history = Statistic()
        new_history.record(request, queryset, {})
        return MsgOk()

    @action(detail=True, methods=["get"])
    def get_browser_stats(self, request, pk=None):
        queryset = Statistic.objects.filter(
            shortened_url_id=pk,
            # shortened_url__creator_id=request.user.id,
            shortened_url__creator_id=request.users_id,
            created_at__gte=get_kst() - timedelta(days=14),
        )
        if not queryset.exists():
            raise Http404
        # rtn = queryset.first().clicked()
        # serializer = UrlListSerializer(rtn)
        browers = (
            queryset.values("web_browser", "created_at__date")
            .annotate(count=Count("id"))
            .values("count", "web_browser", "created_at__date")
            .order_by("-created_at__date")
        )
        browers = (
            queryset.values("web_browser")
            .annotate(count=Count("id"))
            .values("count", "web_browser")
            .order_by("-count")
        )
        serializer = BrowerStatSerializer(browers, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=["get"])
    # def remove_click(self, request, pk=None):
    #     print("removed")
