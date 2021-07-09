from django.contrib import admin
from .models import Post, Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_display_links = ('title', 'slug')
    list_filter = ('publish', 'status', 'author')
    # list_editable = ('author', 'status')
    search_fields = ('title', 'body')
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name', )}
