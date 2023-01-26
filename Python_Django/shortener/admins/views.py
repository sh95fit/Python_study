from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shortener.urls.decorators import admin_only

from django.db.models.query import Prefetch
from shortener.models import ShortenedUrls, Statistic

# 서브 쿼리 사용 시 추가
from django.db.models import Subquery, OuterRef


@login_required
@admin_only
def url_list(request):
    # command_handler()
    # return render(request, "admin_url_list.html", {})

    urls = (
        ShortenedUrls.objects.order_by("-id")
        # select_related
        # 암시적으로 명시하지 않고 사용이 가능!
        # But, 암시적으로 명시하지 않고 사용하는 경우 쿼리수가 증가하여 부하가 걸린다(즉, 명시하는 경우 쿼리수를 줄일 수 있다!)
        # 데이터가 많아질수록 더 많은 쿼리를 수행하게 되어 부하가 크게 증가한다!
        # 하나의 단일 테이블로 조인해서 여러 테이블에 분포된 데이터를 가져오는 경우 적합
        # .select_related(
        #     "creator",
        #     "creator__user",
        #     "creator__organization",
        #     "creator__organization__pay_plan",
        # )


        # 데이터가 많고 조인을 많이 해야하는 경우 사용
        .prefetch_related(
            Prefetch("creator"),
            Prefetch("creator__user"),
            Prefetch("creator__organization"),
            Prefetch("creator__organization__pay_plan"),
            Prefetch("statistic_set"),
            #     Prefetch("statistic_set", queryset=Statistic.objects.filter(
            #         web_browser="Chrome"), to_attr="chrome_usage"),
        )
        .all()
    )

    # 서브 쿼리 활용
    # 서브 쿼리가 실행되는 시점 : 슬라이싱할 때, first/last/count 등이 실행될 때 등
    # 따라서 장고가 실행될 때 에러를 잡아내지 못한다!
    # subquery = Statistic.objects.filter(
    #     shortened_url_id=OuterRef("pk")).order_by("-id")
    # urls_ = ShortenedUrls.objects.annotate(
    #     last_visit_browser=Subquery(subquery.values("web_browser")[:1]))

    # for u in urls_:
    #     print(u.id, u.last_visit_browser)

    # print(urls)

    # for u in urls:
    #     print(u.chrome_usage)
    #     for e in u.chrome_usage:
    #         print(e.web_browser)

    return render(request, "admin_url_list.html", {"urls": urls})
