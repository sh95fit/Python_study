from functools import wraps
from django.http import HttpResponseRedirect
from django.http.response import Http404


def admin_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        # 설정에 따라 특정 유저만 들어오게 할 수도 있음
        # ex>
        # users = [1, 2, 3]
        # if request.user.id not in users:
        #     return function(request, *args, **kwargs)
        # else:
        #     raise Http404
        is_admin = request.user.is_superuser
        if is_admin:
            return function(request, *args, **kwargs)
        else:
            raise Http404

    return wrap
