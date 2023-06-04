from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SinglePost

class SinglePostContent(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(SinglePost, SinglePostContent)
