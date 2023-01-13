from django.contrib import messages
from shortener.forms import UrlCreateForm
# from django.shortcuts import redirect, render
from django.shortcuts import redirect, render, get_object_or_404
# from shortener.models import ShortenedUrls
from shortener.models import ShortenedUrls, Statistic
from django.contrib.auth.decorators import login_required
# from ratelimit.decorators import ratelimit
from django_ratelimit.decorators import ratelimit
from django.contrib.gis.geoip2 import GeoIP2

from shortener.utils import url_count_changer

from django.db.models import Count
from shortener.models import TrackingParams

# 어뷰징과 같은 행위를 제한할 수 있음! 쓸모 없는 리소스 낭비를 막을 수 있다   ex> 3/m : 분당 3회 이상 발생시 제한


@ratelimit(key="ip", rate="10/s")
def url_redirect(request, prefix, url):
    # print(prefix, url)
    was_limited = getattr(request, "limited", False)
    if was_limited:
        return redirect("index")
    get_url = get_object_or_404(
        ShortenedUrls, prefix=prefix, shortened_url=url)
    is_permanent = False        # True : 301로 검색엔진에 잡힘 / False : 302로 검색엔진에 잡히지 않음!
    target = get_url.target_url
    if get_url.creator.organization:
        is_permanent = True

    if not target.startswith("https://") and not target.startswitch("http://"):
        target = "https://" + get_url.target_url

    custom_params = request.GET.dict() if request.GET.dict() else None

    history = Statistic()
    # history.record(request, get_url)
    history.record(request, get_url, custom_params)

    return redirect(target, permanet=is_permanent)


def url_list(request):
    a = (
        Statistic.objects.filter(shortened_url_id=13)
        .values("custom_params__email_id")
        .annotate(t=Count("custom_params__email_id"))
    )
    print(a)
    get_list = ShortenedUrls.objects.order_by("-created_at").all()
    return render(request, "url_list.html", {"list": get_list})


@login_required
def url_create(request):
    msg = None
    if request.method == "POST":
        form = UrlCreateForm(request.POST)
        if form.is_valid():
            msg = f"{form.cleaned_data.get('nick_name')} 생성 완료!"
            messages.add_message(request, messages.INFO, msg)
            form.save(request)
            return redirect("url_list")
        else:
            form = UrlCreateForm()
    else:
        form = UrlCreateForm()
    return render(request, "url_create.html", {"form": form})


@login_required
def url_change(request, action, url_id):
    if request.method == "POST":
        url_data = ShortenedUrls.objects.filter(id=url_id)
        if url_data.exists():
            if url_data.first().creator_id != request.user.id:
                msg = "자신이 소유하지 않은 URL입니다."
            else:
                if action == "delete":
                    msg = f"{url_data.first().nick_name} 삭제 완료!"
                    # url_data.delete()
                    try:
                        url_data.delete()
                    except Exception as e:
                        print(e)
                    else:
                        url_count_changer(request, False)
                    messages.add_message(request, messages.INFO, msg)
                elif action == "update":
                    msg = f"{url_data.first().nick_name} 수정 완료!"
                    form = UrlCreateForm(request.POST)
                    form.update_form(request, url_id)

                    messages.add_message(request, messages.INFO, msg)

        else:
            msg = "해당 URL 정보를 찾을 수 없습니다."

    elif request.method == "GET" and action == "update":
        url_data = ShortenedUrls.objects.filter(pk=url_id).first()
        form = UrlCreateForm(instance=url_data)
        return render(request, "url_create.html", {"form": form, "is_update": True})

    return redirect("url_list")
