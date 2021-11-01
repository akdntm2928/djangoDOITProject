import markdown
from django import template
from django.utils.safestring import mark_safe

register =template.Library()

#  전체게시판갯수 - 시작 index - 현재 인데스 +1
@register.filter()
def mark(value):
    extensions =['nl2br',"fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

@register.filter
def sub(value,arg):
    return value - arg

    