from django.shortcuts import render,get_object_or_404,HttpResponse,HttpResponseRedirect,redirect
from django.views.generic import CreateView, UpdateView, DeleteView,ListView,DetailView,TemplateView
from .models import post,community
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
import datetime
from user.models import user_profile
#this will assure that only admin can update or delete
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.

@login_required
def join_community(request,slug):
    community_to_follow = get_object_or_404(community,slug = slug)
    community_to_follow.followed_by.add(request.user)
    logged_in_user = get_object_or_404(user_profile,user = request.user)
    logged_in_user.following.add(community_to_follow)
    return HttpResponseRedirect(reverse('community:detail', kwargs={'slug': slug}))
    
@login_required
def leave_community(request,slug):
    community_to_leave = get_object_or_404(community,slug = slug)
    community_to_leave.followed_by.remove(request.user)
    logged_in_user = get_object_or_404(user_profile,user = request.user)
    logged_in_user.following.remove(community_to_leave)
    return HttpResponseRedirect(reverse('community:detail', kwargs={'slug': slug}))

@login_required
def community_theme(request,slug,theme_num):
    community_object = get_object_or_404(community,slug = slug)
    # may be used later
    # themes=[
    #     "background-image: linear-gradient(147deg, #FFE53B 0%, #FF2525 74%);",
    #     "background-image: linear-gradient(19deg, #21D4FD 0%, #B721FF 100%);",
    #     "background-image: linear-gradient(0deg, #08AEEA 0%, #2AF598 100%);",
    #     "background-image: linear-gradient(90deg, #FEE140 0%, #FA709A 100%);"

    # ]
    if request.user == community_object.admin:
        # currently we are offering only four themes excluding white
            if theme_num<5:
                community_object.theme = theme_num
                community_object.save()
                print('changing theme')
                return HttpResponseRedirect(reverse('community:detail', kwargs={'slug': slug}))
            return HttpResponse('please click on an actual theme box')
            
    return HttpResponse('only admin can change theme')

    

class community_list_view(LoginRequiredMixin,ListView):
    model = community
    context_object_name = 'communities'
    template_name = "communities/community/community_list.html"

    def get_queryset(self):
        type = self.kwargs['type']
        if type == "followed":
            queryset =  community.objects.filter(followed_by = self.request.user)
            
        if type =="my":
            queryset = community.objects.filter(admin = self.request.user)
            
        if type =="all":
            queryset = community.objects.all

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = self.kwargs['type']
        context['type'] = type
        return context


    
class community_detail_view(LoginRequiredMixin,DetailView):
    model = community
    context_object_name = 'community'
    template_name = "communities/community/community_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #this will provide post data
        community_name =  get_object_or_404(community,slug = self.kwargs['slug'])
        posts = post.objects.filter(community = community_name)
        #this will provide followers detail
        context['posts'] = posts
        return context
    
class community_member_list(TemplateView):
    context_object_name = 'community'
    template_name = "communities/community/community_members.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #this will provide post data
        community_name =  get_object_or_404(community,slug = self.kwargs['slug'])
        community_members = user_profile.objects.filter(following = community_name)
        #this will provide followers detail
        context['members'] = community_members
        return context


class community_create_view(LoginRequiredMixin, CreateView):
    model = community
    fields = ('name', 'desc','community_img')
    success_url = reverse_lazy('community:all',kwargs={'type':"my"})
    template_name = "communities/community/community_create_form.html"

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class community_update_view(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = community
    fields = ('name', 'desc','community_img')
    template_name = "communities/community/community_update_form.html"
    
    success_url = reverse_lazy('community:all',kwargs={'type':"my"})
    #this ensure that only admin can update or delete
    def test_func(self):
        return self.request.user == (community.objects.filter(slug = self.kwargs['slug']))[0].admin 
    
       
 
            

    


class community_delete_view(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = community
    template_name = "communities/community/community_check_delete.html"
    success_url = reverse_lazy('community:all',kwargs={'type':"my"})
    #this ensure that only admin can update or delete
    def test_func(self):
        return self.request.user == (community.objects.filter(slug = self.kwargs['slug']))[0].admin 






# class post_list_view(LoginRequiredMixin,ListView):
#     model = post

class post_create_view(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = post
    fields = ('post_title','post_img', 'post_desc')
    template_name = "communities/post/post_create_form.html"

    def test_func(self):
        return self.request.user == (community.objects.filter(slug = self.kwargs['slug']))[0].admin 
    

    def get_success_url(self):
        community_slug = self.kwargs['slug']
        return reverse('community:detail', kwargs={'slug': community_slug})

    def form_valid(self, form):
        community_slug =  self.kwargs['slug']
        form.instance.community = get_object_or_404(community,slug = community_slug)
        form.instance.created_at = datetime.datetime.now()
        return super().form_valid(form)


class post_update_view(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ('post_img', 'post_desc')
    template_name = "communities/post/post_update_form.html"

    def get_success_url(self):
        post_object = post.objects.get(id = self.kwargs['pk'])
        slug = post_object.community.slug
        return reverse('community:detail',kwargs={'slug':slug})
    
    # here we are passing community slug name for back button in template to work
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_object = post.objects.get(id = self.kwargs['pk'])
        slug = post_object.community.slug
        context['community_name'] = slug
        return context
       

    #this ensure that only admin can update or delete
    def test_func(self):
        post_to_update = post.objects.get(id = self.kwargs['pk'])
        community_admin = post_to_update.community.admin
        return self.request.user == community_admin


class post_delete_view(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = post
    template_name = "communities/post/post_check_delete.html"
    
    def get_success_url(self):
        post_object = post.objects.get(id = self.kwargs['pk'])
        slug = post_object.community.slug
        return reverse('community:detail',kwargs={'slug':slug})
    # here we are passing community slug name for back button in template to work
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_object = post.objects.get(id = self.kwargs['pk'])
        slug = post_object.community.slug
        context['community_name'] = slug
        return context

    #this ensure that only admin can update or delete
    def test_func(self):
        post_to_update = post.objects.get(id = self.kwargs['pk'])
        community_admin = post_to_update.community.admin
        return self.request.user == community_admin