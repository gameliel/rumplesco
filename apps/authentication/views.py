from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import Profile, User
from django.contrib.auth import authenticate, login, logout
from apps.store.models import Product, Category
from django.urls import reverse
from apps.helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.contrib.auth.decorators import login_required
from .utils import generate_token
from django.core.mail import EmailMessage
from .forms import UserUpdateForm, ProfileUpdateForm
from django.conf import settings
from apps.core.views import product_list
import threading



class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()


@auth_user_should_not_access
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Enter a valid email address')
            context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username is taken, choose another one')
            context['has_error'] = True

            return render(request, 'register.html', context, status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email is taken, choose another one')
            context['has_error'] = True

            return render(request, 'register.html', context, status=409)

        if context['has_error']:
            return render(request, 'authentication/register.html', context)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        if not context['has_error']:

            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to verify your account')
            return redirect('login')

    return render(request, 'register.html')


@auth_user_should_not_access
def login_user(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR,
                                 'Email is not verified, please check your email inbox')
            return render(request, 'login.html', context, status=401)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid credentials, try again')
            return render(request, 'login.html', context, status=401)

        login(request, user)

        messages.add_message(request, messages.SUCCESS,
                             f'Welcome {user.username}')

        return redirect(reverse('frontpage'))

    return render(request, 'login.html')


def logout_user(request):

    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect(reverse('login'))


def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'activate-failed.html', {"user": user})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'edit_profile.html', context)


@login_required
def myorder(request):
    return render (request, 'myorder.html')


@login_required
def coupon(request):
    return render (request, 'coupon.html')


@login_required
def mysize(request):
    # necksize_id = Necksize.objects.get( id = id)
    return render (request, 'mysize.html')


@login_required
def notification(request):
    return render (request, 'notification.html')


@login_required
def wallet(request):
    return render (request, 'wallet.html')


    