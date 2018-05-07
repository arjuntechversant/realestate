
from django.shortcuts import render

from django.contrib import messages
from django.views.generic import FormView
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth import *
from django.contrib.auth import get_user_model


# Create your views here.
class RegisterUserView(FormView):

        template_name = "realapp/register.html"
        form_class = RegisterUserForm
        success_url = 'realapp/home/'

        def form_valid(self, form):
            # form.save()
            # user.set_password(password)
            get_user_model().objects.create_user(form.cleaned_data.get('email'),
                                                 form.cleaned_data.get('password'),
                                                 form.cleaned_data.get('mobile_no'),
                                                 form.cleaned_data.get('name')
                                                 )

            # messages.success(self.request, "ok")

            return render(self.request,"realapp/home.html")
            # success_url = '/home/'


class LoginUserView(FormView):

        template_name = "realapp/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
                email = request.POST['email']
                password = request.POST['password']
                # try:
                print(email, password, "dddddddddddddd")
                user = authenticate(request, email=email, password=password)
                print("auth", str(authenticate(email=email, password=password)))


                if user is not None:
                        login(request, user)
                        return render(request, 'realapp/home.html')

                else:
                        return HttpResponse("invalid")

                # except auth.ObjectNotExist:
                #         print("invalid user")

                # return render(request,'login.html')


class AdPostingView(FormView):
        # pass
        template_name = "realapp/adposting.html"
        form_class = AdPostingForm
        success_url = '/thanks/'

        def form_valid(self, form):

                # form= AdPostingForm(self.request.POST,self.request.FILES)
                form.save()
                return render(self.request, "realapp/home.html")



class HomeUserView(FormView):
        # pass
        # template_name = "realapp/home.html"
        # form_class = LoginUserForm
        def form_valid(self, form):
                return render(self.request, 'realapp/home.html')
