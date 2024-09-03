from django.db import models

from sinrato.utils.base import BaseModel

class Author(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Title of the author', help_text='max 100 character')
    description = models.TextField(max_length=100, verbose_name='Description of the author', help_text='max 100 character')
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        
    def __str__(self):
        return self.title
            
class Tags(BaseModel):
    title = models.CharField(verbose_name='tag of blog', help_text='max 100 character')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        

class BlogType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    
    def __str__(self):
        return self.name       

class Blogs(BaseModel):
    
    title = models.CharField(max_length=100,verbose_name= 'Title of the blog', help_text='max 100 character')
    author = models.ForeignKey(Author,max_length=100, on_delete=models.CASCADE,related_name='author_of_blog',verbose_name='Author of the blog', help_text='max 100 character')
    content = models.TextField(verbose_name='Content of the blog')
    types = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, max_length=10, related_name='tag_of_blog')
    is_published = models.BooleanField(default=False, verbose_name='Is published?')
    cover_image = models.ImageField(upload_to='blog/cover_image', verbose_name='Cover image of the blog', help_text='Upload a cover image for the blog', null=True, blank=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
    def __str__(self):
        return self.title


class Comment(BaseModel):
    coments = models.TextField(verbose_name= 'Bloga comment elave et: ')   
    name = models.CharField(max_length=255,verbose_name='Name: ') 
    email = models.EmailField(verbose_name='Email: ') 
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return self.name
    
    
    

        