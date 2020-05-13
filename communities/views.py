from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView,ListView,DetailView
from .models import post,community
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
import datetime
#this will assure that only admin can update or delete
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.

class community_list_view(LoginRequiredMixin,ListView):
    model = community
    context_object_name = 'communities'
    template_name = "communities/community/community_list.html"
    
class community_detail_view(LoginRequiredMixin,DetailView):
    model = community
    context_object_name = 'community'
    template_name = "communities/community/community_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        community_name = get_object_or_404(community,slug = self.kwargs['slug'])
        posts = post.objects.filter(community = community_name)
        context['posts'] = posts
        return context

class community_create_view(LoginRequiredMixin, CreateView):
    model = community
    fields = ('name', 'desc')
    success_url = reverse_lazy('community:all')
    template_name = "communities/community/community_create_form.html"

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class community_update_view(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = community
    fields = ('name', 'desc')
    template_name = "communities/community/community_update_form.html"
    
    success_url = reverse_lazy('community:all')
    #this ensure that only admin can update or delete
    def test_func(self):
        return self.request.user == (community.objects.filter(slug = self.kwargs['slug']))[0].admin 
    
       
 
            

    


class community_delete_view(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = community
    template_name = "communities/community/community_check_delete.html"
    success_url = reverse_lazy('community:all')
    #this ensure that only admin can update or delete
    def test_func(self):
        return self.request.user == (community.objects.filter(slug = self.kwargs['slug']))[0].admin 






# class post_list_view(LoginRequiredMixin,ListView):
#     model = post

class post_create_view(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = post
    fields = ('post_img', 'post_desc')
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