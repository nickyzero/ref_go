from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView

# 회원관리
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# 쇼핑리스트
from django.views.generic import ListView
from .models import Shopping_list, Refrigerator, Setting_user



# Create your views here.
#class HomeView(TemplateView):
#    template_name = "base.html"
def HomeView(request):
   return render(request, 'base.html',
                 dict({'Setting_user': Setting_user.objects.all()}))

#---회원가입
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

#---쇼핑리스트
class ShoppingListView(LoginRequiredMixin, ListView):
    model = Shopping_list
    template_name = 'shoppinglist/list.html'

    def get_queryset(self):
        return Shopping_list.objects.filter(user=self.request.user)

class ShoppingListCreateView(LoginRequiredMixin, CreateView):
    model = Shopping_list
    fields = ['product','count','price']
    success_url = reverse_lazy('list')
    template_name='Shoppinglist/listadd.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ShoppingListCreateView, self).form_valid(form)

class ShoppingListUpdateView(LoginRequiredMixin, UpdateView):
    model = Shopping_list
    fields = ['check','product','count','price']
    success_url = reverse_lazy('list')
    template_name='Shoppinglist/listupdate.html'

class ShoppingListDeleteView(LoginRequiredMixin, DeleteView):
    model = Shopping_list
    success_url = reverse_lazy('list')
    template_name = 'Shoppinglist/list_confirm_delete.html'

#---냉장고 생성
class RefCreateView(LoginRequiredMixin, CreateView):
    model = Refrigerator
    fields = ['name']
    success_url = reverse_lazy('home')
    template_name='ref/Refrigerator_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        name = form.cleaned_data['name']
        return super(RefCreateView, self).form_valid(form)

#---냉장고 등록
class RefRegisterView(LoginRequiredMixin, UpdateView):
    model = Setting_user
    fields = ['gid']
    success_url = reverse_lazy('home')
    template_name = 'ref/Refrigerator_register.html'




