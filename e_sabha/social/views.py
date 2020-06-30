from django.shortcuts import render,HttpResponseRedirect
from .models import MyPost,MyProfile,PostComment,PostLike,FollowUser,Contact
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.db.models import Q
from datetime import datetime
from django.contrib import messages
# Create your views here.

@method_decorator(login_required,name = 'dispatch')
class HomeView(TemplateView):
    template_name = 'social/home.html'
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self,**kwargs)
        followedlist = FollowUser.objects.filter(followed_by = self.request.user.myprofile)
        followedlist2 = []
        for e in followedlist:
            followedlist2.append(e.profile)
        si = self.request.GET.get('si')
        if si == None:
            si = ""
        postList = MyPost.objects.filter(Q(uploaded_by__in = followedlist2)).filter(Q(subject__icontains = si))
        for p1 in postList:
            p1.liked = False
            ob = PostLike.objects.filter(post = p1,liked_by = self.request.user.myprofile)
            if ob:
                p1.liked = True
        ob = PostLike.objects.filter(post = p1)
        p1.likecount = ob.count()
        context["mypost_list"] = postList 
        return context
    

class AboutView(TemplateView):
    template_name = 'social/about.html'

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('pno')
        msg = request.POST.get('msg')
        contact = Contact(name=name, email=email, phone=phone, msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent.')
    return render(request, 'social/contact.html')


class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ['name','age','gender','status','pno','discription','profile_pic']

class MyPostCreateView(CreateView):
    model = MyPost
    fields = ['msg','subject','pic']
    def form_valid(self,form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
class MyPostListView(ListView):
    model = MyPost
    template_name = 'social/mypost_list.html'
    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by = self.request.user.myprofile))

class MyPostDetailView(DetailView):
    model = MyPost
    
class MyPostDeleteView(DeleteView):
    model = MyPost
class MyProfileListView(ListView):
    model = MyProfile
    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ""
        profilelist = MyProfile.objects.filter(Q(name__icontains = si)| Q(gender__icontains = si))
        for p1 in profilelist:
            p1.followed = False
            ob = FollowUser.objects.filter(profile = p1 ,followed_by = self.request.user.myprofile)
            if ob:
                p1.followed = True
        return profilelist
   
class MyProfileDetailView(DetailView):
    model = MyProfile

def follow(request,pk):
    user = MyProfile.objects.get(pk = pk)
    FollowUser.objects.create(profile = user,followed_by = request.user.myprofile)
    return HttpResponseRedirect(redirect_to = '/social/myprofile/list')     

def unfollow(request,pk):
    user = MyProfile.objects.get(pk = pk)
    FollowUser.objects.filter(profile = user,followed_by = request.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to = '/social/myprofile/list')     
def like(request,pk):
    post = MyPost.objects.get(pk = pk)
    PostLike.objects.create(post = post,liked_by = request.user.myprofile)
    return HttpResponseRedirect(redirect_to = '/social/home')

def unlike(request,pk):
    post = MyPost.objects.get(pk = pk)
    PostLike.objects.filter(post = post,liked_by = request.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to = '/social/home')
