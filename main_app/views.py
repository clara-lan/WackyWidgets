from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetNewForm
from django.views.generic.edit import DeleteView
from django.template import RequestContext
from django.db.models import Sum
def home(request):
  widgets = Widget.objects.all()
  widget_form = WidgetNewForm()
  total = widgets.aggregate(Sum('quantity'))
  print(total)
  if request.method == 'POST':
    widget_form = WidgetNewForm(request.POST)
    if widget_form.is_valid():
      new_widget = widget_form.save(commit=False)
      new_widget.save()
      return redirect('/')
  else:
    return render(request, 'index.html',{
      'widgets':widgets,
      'widget_form':widget_form,
      'total':total['quantity__sum']
    })

def delete_new(request, id):
  u = Widget.objects.get(id=id)
  u.delete()
  return redirect('/')