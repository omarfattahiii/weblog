from django.contrib import admin
from .models import Configuration, Notic, Reference, Contact, News

admin.site.register(Configuration)
admin.site.register(Notic)
admin.site.register(Reference)
admin.site.register(Contact)
admin.site.register(News)

admin.site.site_title = "WeBlog"
admin.site.site_header = "WeBlog Manager | Admin Panel"
admin.site.index_title = "Admin Panel"
admin.site.enable_nav_sidebar = True
