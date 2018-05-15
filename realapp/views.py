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
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.core.signing import Signer

from django.contrib.auth.hashers import make_password

# Create your views here.
class RegisterUserView(FormView):

    template_name = "realapp/register.html"
    form_class = RegisterUserForm
    # success_url = '/login/'
    success_url = reverse_lazy('realapp:login')

    def form_valid(self, form):
            #obj = form.save()
            # obj.set_password(password)
            # get_user_model().objects.create_user(form.cleaned_data.get('email'),
            #                                       form.cleaned_data.get('password'),
            #                                       form.cleaned_data.get('mobile_no'),
            #                                       form.cleaned_data.get('name')
            #                                       )

            obj = form.save(commit=False)
            obj.password = make_password(obj.password)
            obj.is_active = False
            form.save()
            signer = Signer()
            signed_value = signer.sign(obj.email)
            key = ''.join(signed_value.split(':')[1:])
            reg_obj = Registration.objects.create(user=obj, key=key)
            msg_html = render_to_string('realapp/email-act.html', {'key': key})

            send_mail("123", "123", 'anjitha.test@gmail.com', [obj.email], html_message=msg_html, fail_silently=False)

            # return render(self.request, "realapp/home.html")
            return super().form_valid(form)


class LoginUserView(FormView):
    template_name = "realapp/login.html"
    form_class = LoginUserForm
    # success_url = '/home'
    # success_url = reverse_lazy('/home')

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        # try:
        print(email, password, "dddddddddddddd")
        user = authenticate(request, email=email, password=password)
        print("auth", str(authenticate(email=email, password=password)))

        if user is not None:
            login(request, user)

            return HttpResponseRedirect("/")

        else:
            return HttpResponse("wrong input")

class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        print (self.request.user.email)
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


class MyAds(generic.ListView):
    template_name = "realapp/myads.html"
    model = Item

    # def get_context_data(self, **kwargs):
    #     context = super(HomeUserView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self):
        return Item.objects.filter(creator_name=self.request.user)


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
    # fields = '__all__'
    fields = ['item_title','item_description','item_images','city','price']
    # exclude = ('creator_name_id',)
    template_name= 'realapp/detail_edit.html'
    success_url = '/'


class DeleteAdd(DeleteView):
    model = Item
    success_url = reverse_lazy('realapp:home')


class RegistrationSuccess(TemplateView):
    template_name = 'realapp/registration-success.html'

    def get(self, request, args, *kwargs):
        key = self.kwargs.get("key")
        try:
            reg_obj = Registration.objects.get(key=key)
            reg_obj.user.is_active = True
            reg_obj.save()
            context = {'user': reg_obj, 'status': True}
            return self.render_to_response(context)
        except Registration.DoesNotExist:
            return self.render_to_response({'status': False})

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