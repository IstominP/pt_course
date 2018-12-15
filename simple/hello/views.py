from django.shortcuts import render
from django.views.generic import TemplateView

from models import Foo

# Create your views here.


class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwags):
		context = super(IndexView, self).get_context_data(**kwags)
		context['custom'] = Foo.objects.all()

		return context