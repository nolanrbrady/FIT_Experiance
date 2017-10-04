import account.views
import portal.forms


class SignupView(account.views.SignupView):

    form_class = portal.forms.SignupForm

    def generate_username(self, form):
        username = form.cleaned_data['email']
        return username
