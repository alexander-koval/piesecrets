from django import template
from ..models import BlogCategory as BlogCategory, Tag

register = template.Library()


@register.simple_tag()
def post_date_url(post, blog_page):
    post_date = post.date
    url = blog_page.url + blog_page.reverse_subpage('post_by_date_slug', args=(
        post_date.year, 
        '{0:02}'.format(post_date.month),
        '{0:02}'.format(post_date.day),
        post.slug,
        )
    )
    return url

@register.inclusion_tag('components/tags_list.html', 
                        takes_context=True)
def tags_list(context, limit=None):
    blog_page = context['blog_page']
    tags = Tag.objects.all()
    if limit:
        tags = tags[:limit]
    return {
        'blog_page': blog_page, 
        'request': context['request'],
        'tags': tags,
    }

@register.inclusion_tag('components/categories_list.html', 
                        takes_context=True)
def categories_list(context):
    blog_page = context['blog_page']
    categories = BlogCategory.objects.all()
    return {
        'blog_page': blog_page,
        'request': context['request'],
        'categories': categories,
    }

@register.inclusion_tag('components/categories_menu.html', 
                        takes_context=True)
def categories_menu(context):
    blog_page = context['blog_page']
    categories = BlogCategory.objects.all()
    return {
        'blog_page': blog_page,
        'request': context['request'],
        'categories': categories,
    }
