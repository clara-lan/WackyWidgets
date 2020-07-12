from django.shortcuts import render
from .models import Widget
from .forms import WidgetNewForm
from django.views.generic.edit import CreateView, DeleteView
from django.template import RequestContext
def home(request):
  widgets = Widget.objects.all()
  widget_form = WidgetNewForm()
  return render(request, 'index.html',{
    'widgets':widgets,
    'widget_form':widget_form
  })

class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
    # def form_valid(self, form):
    # form.instance.user = self.request.user 
    # return super().form_valid(form)
class WidgetDelete(DeleteView):
  model = Widget
  success_url = ''