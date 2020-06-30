from django.contrib import admin
from .models import MyProfile,MyPost,PostComment,PostLike,FollowUser,Contact
from django.contrib.admin.options import ModelAdmin
# Register your models here.
class MyProfileAdmin(ModelAdmin):
    search_fields = ['name','status','pno']
    list_filter = ['status','gender']
admin.site.register(MyProfile,MyProfileAdmin)


class MyPostAdmin(ModelAdmin):
    list_display = ['subject','cr_date','uploaded_by']
    search_fields = ['subject','msg','uploaded_by']
    list_filter = ['cr_date','uploaded_by']
admin.site.register(MyPost,MyPostAdmin)


class PostCommentAdmin(ModelAdmin):
    list_display = ['post','msg']
    search_fields = ['msg','post','commented_by']
    list_filter = ['cr_date']
admin.site.register(PostComment,PostCommentAdmin)


class FollowUserAdmin(ModelAdmin):
    list_display = ['profile','followed_by']
    search_fields = ['profile','followed_by']
    list_filter = ['profile','followed_by']
admin.site.register(FollowUser,FollowUserAdmin)


class PostLikeAdmin(ModelAdmin):
    list_display = ['post','liked_by']
    search_fields = ['post','liked_by']
    list_filter = ['cr_date']
admin.site.register(PostLike,PostLikeAdmin)

admin.site.register(Contact)