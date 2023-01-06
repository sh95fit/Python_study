from django.shortcuts import redirect, render
from shortener.models import Users
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Forms로 작성한 등록 양식 추가
from shortener.forms import RegisterForm
# 로그인, 인증, 로그아웃 관련 모듈 추가
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# 패스워드 초기화, 변경 관련 모듈 추가
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
# Paginator 추가
from django.core.paginator import Paginator
# login 상태 요구 모듈 추가(로그인된 경우만 확인 가능한 페이지 구현)
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):  # request는 항상 써야한다! 미들웨어에서 request를 명시적으로 전달해주고 있기 때문!
    # user = Users.objects.filter(username="admin").first()
    # get을 이용해 user를 특정할 수 있음! 대신 get은 1개만 존재하는 것에 한해서 가져올 수 있음!
    # Abstractuser 사용 시 다음과 같이 user에 직접 접근해서 가져올 수 있다!
    # print(request.user.pay_plan.name)
    user = Users.objects.filter(id=request.user.id).first()
    # user = Users.objects.get(username="admin")
    email = user.email if user else "Anonymous User!"
    print("Logged in?", request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
    print(email)
    return render(request, "base.html", {"welcome_msg": "Hello Django Server!", "email": f"{email}"})


# 리다이렉트 활용 - 유저가 로그인해야만 볼 수 있는 페이지로 접근, 권한 없이 admin 페이지 접근 등
# def redirect_test(request):
#     print("Go Redirect")
#     # urls.py의 name의 index_1을 의미(즉 루트 경로로 리다이렉트해주기 위해 루트 경로의 name을 지정!)
#     return redirect("index_1")


@csrf_exempt    # 요청 위변조 방지!
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        a = request.GET.get("a")
        b = request.GET.get("b")
        user = Users.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user": user, "params": [a, b]})
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)
        return JsonResponse(status=201, data=dict(msg="You just reached with Post Method"), safe=False)


# 등록 관련 추가
# GET : 데이터 요구할 때 사용 / POST : 입력을 줄 때  / PUT : 업데이트 할 때 / DELETE : 지울 때
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입 완료"
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})


# 로그인 관련 추가
def login_view(request):
    msg = None
    # 로그인 정상 수행 확인용 변수
    is_ok = False
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        # msg = "가입되어 있지 않거나 로그인 정보가 잘못 되었습니다."
        # print(form.is_valid)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                # msg = "로그인 성공"
                login(request, user)
        # return render(request, "login.html", {"form": form, "msg": msg})
                is_ok = True
        else:
            msg = "올바른 유저ID와 패스워드를 입력하세요."
    else:
        form = AuthenticationForm()
        # return render(request, "login.html", {"form": form})

    # 보이는 field가 어떤 것들이 있는지 반환해주는 함수
    for visible in form.visible_fields():
        # form의 field에도 클래스를 입혀 디자인 적용
        visible.field.widget.attrs["placeholder"] = "유저ID" if visible.name == "username" else "패스워드"
        visible.field.widget.attrs["class"] = "form-control"
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})


# 로그아웃 관련 추가
def logout_view(request):
    logout(request)
    return redirect("index_1")


# 게시판 관련 추가
@login_required
def list_view(request):
    page = int(request.GET.get("p", 1))
    # 유저 쿼리 - 유저 테이블을 select + order by (id 역순(- 포함))
    users = Users.objects.all().order_by("-id")
    paginator = Paginator(users, 10)    # Paginator(쿼리, 한페이지에 몇개씩 보여줄건지 정하는 개수)
    users = paginator.get_page(page)

    return render(request, "boards.html", {"users": users})
