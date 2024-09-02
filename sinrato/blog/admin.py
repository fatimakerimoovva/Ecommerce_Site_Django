from django.contrib import admin
from .models import Blogs, Author,Tags, BlogType
from django.utils.html import format_html
admin.site.site_header = 'Sinrato Admin Panel' 
admin.site.site_title = 'Sinrato'



class BlogAddVersion(admin.StackedInline):
    model = Blogs
    extra = 1
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','content','is_published','get_cover_image']
    list_filter = ['is_published']
    list_editable = ['is_published']
    search_fields = ['title']
    readonly_fields = ['created', 'updated'] 
    
    def get_cover_image(self, obj):
        if obj.cover_image:
            img = '<img src="{url}" width = 200 , heigt = 200/>'.format(url = obj.cover_image.url)
            return format_html(img)
        return format_html('<p style="color:red">No image<p/>')
            
class TagsAdmin(admin.ModelAdmin):
    search_fields = ['title']   

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    inlines = [BlogAddVersion]
    
class DescriptionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tags, TagsAdmin)
# admin.site.register(Comment)
admin.site.register(BlogType)

