from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from .models import Follower
# from posts.forms import PostForm
# from posts.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
User = get_user_model()

#Аккаунт пользователя
@login_required(login_url = '/')
def user_account(request):
    if request.user.is_authenticated:
        email = request.user.email
        user = User.objects.get(email=email)
        # if request.method == 'POST':
        #     form = PostForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         new_post = form.save(commit=False)
        #         new_post.author = request.user
        #         new_post.post_time = timezone.now()
        #         new_post.save()
        #         return HttpResponseRedirect(request.path)
        # else:
        #     form = PostForm()

        # user_posts = Post.objects.filter(author = user).order_by("-post_time")
        # page = request.GET.get('page', 1)
        # paginator = Paginator(user_posts, 10)
        # try:
        #   post_list = paginator.page(page)
        # except PageNotAnInteger:
        #   post_list = paginator.page(1)
        # except EmptyPage:
        #   post_list = paginator.page(paginator.num_pages)
        #
        # followers = Follower.objects.filter(follower_for = request.user)
        # context = {'user': user, 'form':form, 'user_posts': post_list, 'followers': followers}
        return render(request, 'account/account.html')
    else:
        return HttpResponseRedirect(reverse('main'))