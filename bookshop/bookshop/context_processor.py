from shop.forms import LoginForm, RegisterForm, AddBookForm, UpdateUserForm, UpdateProfileForm


def get_context_data(request):
    context = {
        'loginform': LoginForm(),
        'registerform': RegisterForm(),
        'addbookform': AddBookForm(),
        'updateUserForm': UpdateUserForm(),
        'updateProfileForm': UpdateProfileForm()
        # 'passwdChangeForm': PasswordChangingForm()
    }
    return context