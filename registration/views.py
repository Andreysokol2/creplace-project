from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .forms import UserRegisterForm
from .forms import LoginForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from account.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
# from mysite.settings import AUTH_USER_MODEL as User
User = get_user_model()
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def aboutdata(request):
    return render(request, 'helpers/aboutdata.html', locals())

def donat(request):
    return render(request, 'helpers/donat.html', locals())

def main(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_account'))
    else:
        return render(request, 'registration/main.html', locals())
from django.core.exceptions import ObjectDoesNotExist

def login_user(request):
    if request.method == 'POST':
            form = LoginForm(request, request.POST)
            email = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password, is_verificated=True)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                pass
    else:
        form = LoginForm()
    context = {'form': form}
    context['login_form'] = form
    return render(request, 'registration/login.html', context)
def email_confirmation(request, email, p):
    email_obj = email
    if request.method == 'POST':
        if User.objects.filter(email=email_obj, is_verificated=False).exists():
            code = User.objects.get(email=email_obj).code
            data = request.POST
            data_code = data["code"]
            if data_code == str(code):
                User.objects.filter(email=email_obj).update(is_verificated=True)
                quser = User.objects.get(email=email_obj)
                login(request, quser)
                return redirect('/')
    context = {'email': email}
    return render(request, 'registration/email_confirmation.html', context)
#
#                   ПРОБЛЕМА! ОШИБКИ ИЗ ФОРМ А НЕ ИЗ ДВИЖКО ВЫВОДЯТСЯ ТОЛЬКО В ЛОГИНЕ НА РЕГИСТРАЦИИ ВЫЛЕТАЙ ОШИБКА ЕСЛИ ПИСАТЬ КАК ЗДЕСЬ
#
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        # if User.objects.filter(email=email, is_verificated = True).exists():
        #     form.add_error('email', "Пользователь с таким E-MAIL уже зарегестрирован!")
        first_name = request.POST.get('first_name')
        if form.is_valid():
            ins = form.save()
            # username = form.cleaned_data['username']
            code = generate_code()
            password = form.cleaned_data['password1']
            message = f"""
                        <div class="mini-logo-main" style="height: 60px;
                            text-align: center;
                            margin-top: 2px;margin-bottom: 2px;">
                            <img src="https://i.ibb.co/HHMthJw/Creplace-Logo.jpg" alt="Creplace-Logo" border="0" style="height:100%;">
                        </div>
                        <h3 class="">Ваш код подтверждения - {code}</h4><br>
                        <span style="font-size:16px;">Никому не сообщайте этот код, если регистрировались не вы, просто проигнорируйте это сообщение</span><br>
                        <div style="text-align:center;margin-top: 40px;width:100%;">
                        <a style="height: 100%;     text-decoration: none;
                        color: white;
                        margin: 10px;
                        padding: 20px;
                        width: 70%;
                        font-size: 13px;
                        border-radius: 70px;
                        background-color:#04d579;
                        border-color:#04d579;" href="creplace.ru/email_confirmation/{email}">Войти на этом устройстве</a></div>
                      """""
            send_email(message, email)
            quser = authenticate(password=password, email=email, code = code)
            # user.profile.avatar = 'images/avatar/standart.jpg'
            ins.email = email
            ins.first_name = first_name
            ins.code = code
            ins.save()
            form.save_m2m()
            print('register process')
            messages.success(request, 'Вы успешно зарегестрировались!')
            # login(request, quser)
            return redirect(f'/email_confirmation/{email}')
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'registration/register.html', context)

def send_email(message, recipient):
    login =
    password =
    server = smtplib.SMTP_SSL("smtp.yandex.com", 465)
    # server.set_debuglevel(True)
    # server.starttls()

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Подтверждение Регистрации на Creplace"
    msg["From"] = "creplace@yandex.ru"

    part1 = MIMEText(message, 'html')
    msg.attach(part1)
    try:
        server.login(login, password)
        server.sendmail(login, recipient, msg.as_string())

        print("Email was sent successfully!")
        server.quit()
    except Exception as ex:
        print(f"{ex}Ошибка при отправке имейла")

def generate_code():
    code = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
    return code



