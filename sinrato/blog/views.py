from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import CommentForm
from  django.views.generic import ListView , DetailView
from django.shortcuts import render,redirect
class BlogListView(ListView):
    model = Blogs
    template_name = 'blog.html'
    context_object_name = 'allblogs'

    def get_queryset(self):
        queryset = super().get_queryset()
    
        author_id = self.request.GET.get('author_id')
        type_id = self.request.GET.get('type_id')
        tag_id = self.request.GET.get('tag_id')  # Handle tag filtering
    
        if author_id:
            queryset = queryset.filter(author_id=author_id)
    
        elif type_id:
            queryset = queryset.filter(types_id=type_id)
    
        elif tag_id:
            queryset = queryset.filter(tags__id=tag_id)


        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['blog_types'] = BlogType.objects.all()
        context['tags'] = Tags.objects.all()
        context['recent'] = Blogs.objects.order_by('created')[:5]
        
        return context

class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = BlogForm()
        context['authors'] = Author.objects.all()
        context['blog_types'] = BlogType.objects.all()
        context['recent'] = Blogs.objects.order_by('created')[:5]
        comments = Comment.objects.filter(blog=self.object)
        context['form'] = CommentForm()
        context['comments'] = comments
        context['comment_count'] = comments.count()
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object
            comment.save()
            return redirect('blog-detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))
        
# class BlogDetailView(DetailView):
#     model = Blogs
#     template_name = 'blog-details.html'
#     context_object_name = 'blog'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         comments = Comment.objects.filter(blog=self.object)
#         context['form'] = CommentForm()
#         context['comments'] = comments
#         context['comment_count'] = comments.count()
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = self.object
#             comment.save()
#             return redirect('blog_details', pk=self.object.pk)
#         return self.render_to_response(self.get_context_data(form=form))


