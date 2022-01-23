from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_home', 'category')
    readonly_fields = ('slug',)
    list_editable = ('is_home',)
    list_filter = ('category','is_home')
    search_fields = ('title',)

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


