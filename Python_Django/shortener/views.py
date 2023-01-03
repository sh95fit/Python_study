from django.shortcuts import redirect, render
from shortener.models import Users

# Create your views here.


def index(request):  # request는 항상 써야한다! 미들웨어에서 request를 명시적으로 전달해주고 있기 때문!
    user = Users.objects.filter(username="admin").first()
    # get을 이용해 user를 특정할 수 있음! 대신 get은 1개만 존재하는 것에 한해서 가져올 수 있음!
    # user = Users.objects.get(username="admin")
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
        print(email)
    return render(request, "base.html", {"welcome_msg": "Hello Django Server!", "email": f"{email}"})


# 리다이렉트 활용 - 유저가 로그인해야만 볼 수 있는 페이지로 접근, 권한 없이 admin 페이지 접근 등
def redirect_test(request):
    print("Go Redirect")
    # urls.py의 name의 index_1을 의미(즉 루트 경로로 리다이렉트해주기 위해 루트 경로의 name을 지정!)
    return redirect("index_1")
