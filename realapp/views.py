from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.contrib import messages
from django.views.generic import *
from .forms import *
from .models import *
from django.http import *
from django.contrib.auth import *
from django.contrib.auth import get_user_model
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import *

# Create your views here.
class RegisterUserView(FormView):

    template_name = "realapp/register.html"
    form_class = RegisterUserForm
    success_url = '/login/'

    def form_valid(self, form):
        # form.save()
        # user.set_password(password)
        get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                             form.cleaned_data.get('password'),
                                             form.cleaned_data.get('mobile_no'),
                                             form.cleaned_data.get('name')
                                             )

        # return render(self.request, "realapp/home.html")
        return super().form_valid(form)


class LoginUserView(FormView):
    template_name = "realapp/login.html"
    form_class = LoginUserForm
    success_url = ''

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        # try:
        print(email, password, "dddddddddddddd")
        user = authenticate(request, email=email, password=password)
        print("auth", str(authenticate(email=email, password=password)))

        if user is not None:
            login(request, user)

            return HttpResponseRedirect("home")

        else:
            return HttpResponse("wrong input")

class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        print (self.request.user.username)
        logout(request)
        return HttpResponseRedirect('/')


class AdPostingView(LoginRequiredMixin,FormView):

    # pass
    template_name = "realapp/adposting.html"
    form_class = AdPostingForm
    # success_url = '/home/'
    success_url = reverse_lazy('realapp:home')

    def form_valid(self, form):
        form.instance.creator_name=self.request.user
        form.save()
        return super(AdPostingView, self).form_valid(form)


class HomeUserView(generic.ListView):
    template_name = "realapp/home.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super(HomeUserView, self).get_context_data(**kwargs)
        print(context)
        return context


class DetailUserView(generic.DetailView):
    model = Item
    template_name = 'realapp/detail.html'
    context_object_name = 'estate'

    # def get_context_data(self, *kwargs):
    #     context = super(DetailUserView, self).get_context_data(**kwargs)
    #     pidd = self.kwargs['pid']
    #     q_obj = Item.objects.get(id=pidd)
    #     context['estate'] = q_obj
    #
    #     return context


class EditAdd(UpdateView):
    model = Item
    # form_class = AdPostingForm
    fields = '__all__'
    template_name= 'realapp/detail_edit.html'
    success_url = '/'


class DeleteAdd(DeleteView):
    model = Item
    success_url = reverse_lazy('realapp:home')


    # def get_object(self, queryset=None):
    #     queryset = Item.objects.all()[:1].get()
    #     return queryset
    # queryset = Item.objects.all()


    # def get_queryset(self):
    #     self.queryset = Item.objects.all()
    #     # return queryset

    # def get_object(self):
    #     return self.request.


# class PostDeleteView(DeleteView):
#     model = Item
#     success_url = reverse_lazy('realapp:home')
#
#     def get_queryset(self):
#         owner = self.request.user
#         return self.model.objects.filter(owner=owner)