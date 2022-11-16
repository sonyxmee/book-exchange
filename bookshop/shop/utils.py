menu = [
    {"title": "Главная страница", "url_name": "home"},
    {"title": "Добавить книгу", "url_name": "addbook"},
    # {'title': 'Корзина', 'url_name' = 'shopbag'},
    # {'title': 'Контакты', 'url_name' = 'contacts'},
]


class DataMixin:
    def get_user_context(selfself, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context