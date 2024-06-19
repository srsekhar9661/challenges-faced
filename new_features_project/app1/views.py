from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from .models import Template
from .forms import TemplateForm


def index(request):
    return render(request, 'index.html')


def view1(request):

    return render(request, 'pdf_working.html')


def view2(request):
    # import ipdb;ipdb.set_trace()
    return JsonResponse(json.loads(request.POST.get('dataObject')))


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


def new(request):
    return render(request, 'new.html')


# views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import Narrative
from .forms import NarrativeForm


class NarrativeView(View):
    template_name = 'narrative_crud.html'

    def get(self, request, pk=None):
        if pk:
            narrative = get_object_or_404(Narrative, pk=pk)
            form = NarrativeForm(instance=narrative)
        else:
            narrative = None
            form = NarrativeForm()

        narratives = Narrative.objects.all()
        context = {
            'form': form,
            'narrative': narrative,
            'narratives': narratives,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk=None):
        if pk:
            narrative = get_object_or_404(Narrative, pk=pk)
            form = NarrativeForm(request.POST, instance=narrative)
            _method = request.POST.get('_method',None)
            # import ipdb;ipdb.set_trace(context=5)
            if _method and _method.lower() == 'delete':
                self.delete(request, pk=pk)

        else:
            form = NarrativeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('narrative-crud')

        narratives = Narrative.objects.all()
        context = {
            'form': form,
            'narratives': narratives,
        }
        return render(request, self.template_name, context)

    def delete(self, request, pk):
        narrative = get_object_or_404(Narrative, pk=pk)
        narrative.delete()
        return redirect('narrative-crud')


