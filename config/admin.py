from django.contrib import admin
from .models import Configuration, Notic

admin.site.register(Configuration)
admin.site.register(Notic)

admin.site.site_title = "Voracious.ir"
admin.site.site_header = "Voracious Weblog Manager | Admin Panel"
admin.site.index_title = "Admin Panel"
admin.site.enable_nav_sidebar = True
