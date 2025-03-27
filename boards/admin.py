from django.contrib import admin
from .models import Board, Topic, Post   
from django.contrib.auth.models import Group,User

# class topic(admin.ModelAdmin):
#     fields=['subject','board']
#     #! fields show when i enter topic
#     list_display=['combine_new_columen','created_date','created_by','subject','board']
#     #! fields show before i enter topic
#     def combine_new_columen(self,obj):
#         return f'topic is : {obj.subject}  and board is : {obj.board}'
#     list_display_links=['combine_new_columen','created_by']
#     #! make created_by is link like combine_new_columen
#     list_editable=['subject','board']
#     #! update fields show before i enter topic
#     #! The value of 'field name' cannot be in both 'list_editable' and 'list_display_links'.
    # list_filter=['created_by','board']
    # search_fields=['created_by','board']
admin.site.register(Board)
admin.site.register(Topic,)
admin.site.register(Post)
