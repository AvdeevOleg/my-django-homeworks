from django.contrib import admin
from .models import Article, Category, Tag, Scope

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('categories',)
    inlines = [ScopeInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

