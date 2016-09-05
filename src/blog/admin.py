from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    # class Meta:
    #     model=Post
    # date_hierarchy = 'timestamp'
    # list_display_links = ['timestamp']
    # list_editable = ('title') #same list cant be a form and a link
    list_display = ('title', 'timestamp','tag')
    list_filter = ('timestamp','tag')
    search_fields = ['title', 'content']
    list_per_page = 20


admin.site.register(Post, PostAdmin)
