from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Widget
from .forms import WidgetForm

def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'base.html', {
        'widget_form': widget_form, 'widgets': widgets
    })

def create_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    new_widget = form.save(commit=False)
    new_widget.save()
  return redirect('/')

def delete(request, id):
    Widget.objects.get(id=id).delete()
    return redirect('/')