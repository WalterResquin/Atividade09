from django.views.generic import ListView

from .models import Post

class InicioView(ListView):
    model = Post
    template_name = 'inicio.html'

