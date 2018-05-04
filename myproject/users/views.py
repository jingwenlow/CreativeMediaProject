from django.shortcuts import render, redirect

# Create your views here.
# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
# from django.views.generic.edit  import CreateView

from django.http import HttpResponse
from .forms import CustomUserCreationForm, AddPost
from .models import Post

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def addPost(request):
#     return render(request, 'addPost.html', addPost)
#

class addPost(TemplateView):
    success_url = reverse_lazy('login')
    template_name = 'addPost.html'

    def get(self, request):
        form = AddPost()
        posts = Post.objects.all()
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = addPost()
            return redirect('addPost')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


class addFriend(TemplateView):
    success_url = reverse_lazy('login')
    template_name = 'addFriend.html'


# class JointLoginSignupView(CreateView):
#     form_class = CustomAuthenticationForm
#     signup_form  = CustomUserCreationForm
#     template_name = 'login.html'
#     def __init__(self, **kwargs):
#         super(JointLoginSignupView, self).__init__(*kwargs)
#
#     def get_context_data(self, **kwargs):
#         ret = super(JointLoginSignupView, self).get_context_data(**kwargs)
#         ret['signupform'] = get_form_class(app_settings.FORMS, 'CustomUserCreationForm', self.signup_form)
#         return ret
#
#
# login = JointLoginSignupView.as_view()
