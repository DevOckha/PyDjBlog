from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Category
from django.db.models import Q 


class HomePageView(TemplateView):
    template_name = 'dblog/home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_home=True).order_by('-created_time')
        context['categories'] = Category.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'dblog/about.html'


    
class CategoryListView(ListView):
    template_name = 'dblog/home.html'
    model = Category
    paginate_by = 10
    ordering = ['-post']

    def get_context_data(self, **kwargs):
        context =  super(CategoryListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_home = True, category__slug=self.kwargs.get('slug'))
        context['categories'] = Category.objects.all()
        return context



class PostDeailView(DetailView):
    template_name = 'dblog/partials/_post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDeailView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug = self.kwargs.get('slug'))
        return context

#for forms    category = forms.ModelChoiceField(queryset=ProgrammingCategory.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

class SearcListView(ListView):
    template_name = 'dblog/partials/_search.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

    
    def get_queryset(self):
        result =  super(SearcListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            postresult = Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query)).order_by('-created_time')
            result = postresult
        else:
            result = None
        return result