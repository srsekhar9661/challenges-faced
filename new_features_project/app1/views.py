from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
from .models import Template
from .forms import TemplateForm


def view1(request):

    return render(request, 'pdf_working.html')

def view2(request):
    # import ipdb;ipdb.set_trace()
    return HttpResponse(str(json.loads(request.POST.get('dataObject'))))


def create_template(request):
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template_list')
    else:
        form = TemplateForm()
    return render(request, 'template_form.html', {'form':form})

def update_template(request, pk):
    template = get_object_or_404(Template, pk=pk)
    if request.method == 'POST':
        form = TemplateForm(request.POST,  instance=template)
        if form.is_valid():
            form.save()
            return redirect('template_detail', pk=template.pk)
    else:
        form = TemplateForm(instance=template)
    return render(request, 'template_form.html', {'form':form})
