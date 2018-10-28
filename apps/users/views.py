from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import View

from users.models import UserProfile, EmailVerifyRecord
from utils.email_send import send_email
from .forms import LoginForm, RegisterForm, ForgetForm


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


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # # 这里注册时前端的name为email
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()
            send_email(user_name, "register")
        return render(request, "login.html")


class ActiveView(View):
    def get(self, request, email, code):
        try:
            active_filter = EmailVerifyRecord.objects.get(email=email, code=code)
            if active_filter is not None:
                try:
                    user = UserProfile.objects.get(email=email)
                    user.is_active = True
                    user.save()
                    EmailVerifyRecord.objects.get(email=email, code=code).delete()
                    return render(request, "login.html")
                except Exception as e:
                    return render(request, "register.html", {"msg": "您的激活出现错误"})
            else:
                return render(request, "register.html", {"msg": "您的激活链接无效"})
        except Exception as e:
            print(e)
            return render(request, "register.html", {"msg": "您的激活链接无效"})


class ForgetView(View):
    """
    忘记密码视图
    """

    def get(self, request):
        forgetForm = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forgetForm})

    def post(self,request):
        forgeForm = ForgetForm(request.POST)
        if forgeForm.is_valid():
            email = request.POST.get("email","")

            send_email(email=email, send_type="forget")

