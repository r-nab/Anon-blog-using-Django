from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model=Post
    # date_hierarchy = 'timestamp'
    # list_editable = ('title') #same list cant be a form and a link
    exclude = ('uid','myurl')
    list_display_links = ['title']
    list_display = ('uid','title', 'timestamp','tag','myurl')
    list_filter = ('timestamp','tag')
    search_fields = ['title', 'content']
    list_per_page = 10


admin.site.register(Post, PostAdmin)
