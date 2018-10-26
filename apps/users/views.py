from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# from django.views.generic.base import View
from django.views import View

from users.models import UserProfile
from .forms import LoginForm


class CustomBackend(ModelBackend):
    """
    实现用户名邮箱均可登录
    继承ModelBackend类，因为它有方法authenticate，可点进源码查看
    在settings文件中添加
    AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
    )
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            # 也就是说如果数据库中存在两个以上的数据 get就会失败
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def index_view(request):
    return render(request, "index.html")


class LoginView(View):
    """
     from django.views.generic.base import View
     from django.views import View
     这两一样

     实现cbv 的方式
    """

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        """
        post请求操作
        先通过自定义的LoginForm类（users/forms.py）去验证请求的数据是否有效
        接着将数据通过authenticate(重载后 可以通过用户名或者邮箱进行验证 类见上面的CustomBackend)进行判断得到user对象
        如果存在对象就返回index页面 否则返回登录页面同时带回错误信息
        :param request:
        :return:
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                context = {
                    "msg": "用户名或密码错误"
                }
                return render(request, "login.html", context=context)
        else:
            context = {
                "login_form": form
            }
            return render(request, "login.html", context=context)
