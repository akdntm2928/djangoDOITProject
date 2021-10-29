from django import template

register =template.Library()

#  전체게시판갯수 - 시작 index - 현재 인데스 +1
@register.filter
def sub(value,arg):
    return value - arg

    