from django.shortcuts import render
from django.views.generic import ListView
from .models import Search
import json


class List(ListView):
    model = Search
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(Search.objects.values()))
        return context


