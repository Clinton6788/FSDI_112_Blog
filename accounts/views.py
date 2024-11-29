from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class LogoutConfirmView(TemplateView):
    template_name = "registration/logout_confirm.html"

    def get(self, request):
        return self.render_to_response(self.get_context_data())

    def post(self, request):
        logout(request)
        return redirect('home')