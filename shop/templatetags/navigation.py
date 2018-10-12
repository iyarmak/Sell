from django import template

register = template.Library()

CONTEXT_KEY = 'DJANGO_BREADCRUMB_LINKS'


@register.inclusion_tag('horizontal-menu.html', takes_context=True)
def horizontal_menu(context, items, current_category):
    return {'menu_items': items, 'current_category': current_category}


@register.inclusion_tag('vertical-menu.html', takes_context=True)
def vertical_menu(context, items, current_category, child=None):
    return {'menu_items': items, 'current_category': current_category, 'child': child}


@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def breadcrumb(context, path, token):
    breadcrumbs = [
        {'id': '', 'name': 'SELL', 'code': 'sell', 'url': '/'}
    ]

    if path:
        for item in path:
            breadcrumbs.append({
                'id': item['categoryId'],
                'name': item['categoryName'],
                'code': item['categoryCode'],
                'url': item['categoryCode'] + '/' if item['categoryCode'] else ''
            })

    if token and not path:
        breadcrumbs.append({
            'id': '',
            'name': token.category_name,
            'code': token.category_code,
            'url': token.category_code + '/' if token.category_code else ''})

    breadcrumbs[-1]['url'] = ''

    return {'breadcrumbs': breadcrumbs}