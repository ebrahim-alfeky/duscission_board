from django.contrib import admin
from django.contrib.auth.models import Group
from boards.models import *
# Register your models here.

#! admin.site.unregister(Group)
#! remove Group from admin pannel
#! admin.site.unregister(model name) 
#! don't show in admin pannel

#! admin.site.site_header='name'
#! change site_header from Django administration to name
# admin.site.site_header='hema'

#! admin.site.site_title='name'
#! change name of tab from admin site admin to name

