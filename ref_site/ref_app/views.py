from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView

# 회원관리
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# 쇼핑리스트
from .models import Shopping_list

# Create your views here.
class HomeView(TemplateView):
    template_name = "base.html"

#  회원가입
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


# 쇼핑리스트
def ShoppingListView(request):
    return render(request, 'shoppinglist/list.html',
                  dict({'shopping_list': Shopping_list.objects.all()}))