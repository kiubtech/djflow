import random, string
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View, ListView, DeleteView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib import messages
from .forms import LoginForm
from .models import UserProfile
from .functions import SecurityUtils
from djflow.apps.general_functions import send_email
from djflow.core.json_settings import get_settings
from djflow.apps import response_messages

settings = get_settings()


class Login(View):
    template_name = "login.html"
    form = LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('flow:dashboard'))
        else:
            ctx = {'form': self.form}
            if 'next' in request.GET:
                ctx['next'] = request.GET['next']
            return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            login(request, form.my_user)
            messages.success(request, _("¡Bienvenido {0}!".format(form.my_user.first_name)))
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse_lazy('flow:dashboard'))
        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('website:index'))


class UserProfileData(LoginRequiredMixin, View):
    template_name = "userprofile.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        userprofile = request.user.userprofile
        image_profile = request.FILES['image_profile'] if 'image_profile' in request.FILES else None
        if image_profile:
            userprofile.image_profile = image_profile
            userprofile.save()
        request.user.username = request.POST['email']
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        request.user.save()
        return HttpResponseRedirect(reverse_lazy('flow:dashboard'))


class ChangePassword(LoginRequiredMixin, View):
    template_name = "change_password.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        password_one = request.POST['password_one'] if 'password_one' in request.POST else None
        password_two = request.POST['password_two'] if 'password_two' in request.POST else None
        if password_one and password_two:
            if password_one == password_two:
                request.user.set_password(password_one)
                request.user.save()
                logout(request)
                return HttpResponseRedirect(reverse_lazy('security:login'))
            else:
                messages.error(request, _("Las contraseñas no coinciden"))
        else:
            messages.error(request, _("Error en los datos recibidos"))
        return self.get(request)


class UserList(LoginRequiredMixin, ListView):
    template_name = "user_list.html"
    model = UserProfile
    paginate_by = 10


class UserDelete(LoginRequiredMixin, DeleteView):
    template_name = "user_delete.html"
    model = UserProfile
    success_url = reverse_lazy('security:user-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, response_messages.DELETE_SUCCESSFULL)
        return super(UserDelete, self).delete(request, *args, **kwargs)


class UserNew(LoginRequiredMixin, View):
    template_name = "user_new.html"
    utils = SecurityUtils()

    def send_welcome_mail(self, request, new_user, new_user_password):
        ctx = {'user': request.user, 'new_user': new_user, 'new_user_password': new_user_password, 'URL_SERVER': settings['URL_SERVER']}
        html_content = render_to_string('mailing/welcome.html', ctx)
        subject = _("Bienvenido a Cashflow / invitación")
        send_email(subject, to_email=new_user.email, html_content=html_content)

    def get(self, request):
        ctx = {'random_password': self.utils.random_password()}
        return render(request, self.template_name, ctx)

    def post(self, request):
        try:
            user_exist = User.objects.get(email=request.POST['email'])
        except:
            user_exist = None
        if user_exist:
            messages.error(request, _("Email {0} ya se encuentra registrado en el sistema".format(request.POST['email'])))
            ctx = {'random_password': self.utils.random_password(), 'first_name': request.POST['first_name'],
                   'last_name': request.POST['last_name'], 'email': request.POST['email']}
            return render(request, self.template_name, ctx)
        else:
            new_user = User.objects.create_user(request.POST['email'],
                                                request.POST['email'],
                                                request.POST['password'])
            new_user.first_name = request.POST['first_name']
            new_user.last_name = request.POST['last_name']
            new_user.is_active = True  # Activamos al usuario
            new_user.save()
            # Enviamos un email de bienvenida
            self.send_welcome_mail(request, new_user, request.POST['password'])
            messages.success(request, response_messages.SAVE_SUCCESSFULL)
            return HttpResponseRedirect(reverse_lazy('security:user-list'))


class ActiveInactiveUser(LoginRequiredMixin, View):
    """
    Activamos / Desactivamos usuarios.
    """

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.is_active = not user.is_active
            user.save()
            messages.success(request, response_messages.UPDATE_SUCCESSFULL)
        except User.DoesNotExist:
            messages.error(request, _("Usuario no encontrado"))
        return HttpResponseRedirect(reverse_lazy('security:user-list'))


# ===================================================
# Registering Tenants
# ===================================================


class TenantRegisterView(View):
    template_name = "register_tenant.html"
    active_menu = "register"

    def get(self, request):
        return render(request, self.template_name, {'active_menu': self.active_menu})