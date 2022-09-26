from django.contrib import admin
from .models import Profile, Post


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
    search_fields = ('user',)
    list_filter = ('create_at')
    empty_value_display = '-пусто'


admin.site.register(Profile)
admin.site.register(Post)
