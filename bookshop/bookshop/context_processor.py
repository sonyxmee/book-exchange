from shop.forms import LoginForm, RegisterForm, AddBookForm


def get_context_data(request):
    context = {
        'loginform': LoginForm(),
        'registerform': RegisterForm(),
        'addbookform': AddBookForm()
    }
    return context