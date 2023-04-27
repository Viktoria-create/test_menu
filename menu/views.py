from django.shortcuts import render


def menu(request):
    menu_items = [
        {'title': 'Главная', 'url': '/'},
        {'title': 'О нас', 'url': '/about/'},
        {'title': 'Контакты', 'url': '/contacts/'},
    ]
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)
