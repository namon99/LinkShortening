from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from general.models import ShortenedLink


class LoginView(auth_views.LoginView):
    template_name = 'authentication/login.html'


class LogoutView(auth_views.LogoutView):
    pass


class SignUpView(CreateView):
    template_name = 'authentication/signup.html'
    form_class = UserCreationForm


class ProfileView(ListView):
    template_name = 'authentication/profile.html'
    paginate_by = 15
    model = ShortenedLink

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        links = ShortenedLink.objects.order_by('pk').filter(user=self.request.user)
        paginator = Paginator(links, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
