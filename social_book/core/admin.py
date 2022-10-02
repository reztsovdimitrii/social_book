from django.contrib import admin
from .models import Profile, Post, LikePost


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'id_user',
        'bio',
        'profileimg',
        'location'
    )
    search_fields = ('user',)
    empty_value_display = '-пусто'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'image',
        'caption',
        'create_at',
        'no_of_likes'
    )
    list_editable = ('user',)
    search_fields = ('user',)
    list_filter = ('create_at', 'user',)
    empty_value_display = '-пусто'


class LikePostAdmin(admin.ModelAdmin):
    list_display = (
        'post_id',
        'username'
    )
    empty_value_display = '-пусто'


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(LikePost, LikePostAdmin)
