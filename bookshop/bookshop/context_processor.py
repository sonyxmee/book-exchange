from shop.forms import LoginForm, RegisterForm


def get_context_data(request):
    context = {
        'loginform': LoginForm(),
        'registerform': RegisterForm(),
    }
    return context