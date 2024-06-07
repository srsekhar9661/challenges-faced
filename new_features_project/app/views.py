from django.shortcuts import render, get_object_or_404, redirect
from .models import Template

def template_list(request):
    templates = Template.objects.all()
    return render(request, 'app/template_list.html', {'templates': templates})

def template_detail(request, pk):
    template = get_object_or_404(Template, pk=pk)
    return render(request, 'app/template_detail.html', {'template': template})

def create_template(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        dependent_template_ids = request.POST.getlist('dependent_templates')
        
        template = Template.objects.create(name=name, content=content)
        if dependent_template_ids:
            template.dependent_templates.set(dependent_template_ids)
        return redirect('template_list')
    
    templates = Template.objects.all()
    return render(request, 'app/template_form.html', {'templates': templates, 'action': 'Create'})

def update_template(request, pk):
    template = get_object_or_404(Template, pk=pk)
    
    if request.method == 'POST':
        template.name = request.POST.get('name')
        template.content = request.POST.get('content')
        dependent_template_ids = request.POST.getlist('dependent_templates')
        
        template.save()
        if dependent_template_ids:
            template.dependent_templates.set(dependent_template_ids)
        else:
            template.dependent_templates.clear()
        
        return redirect('template_detail', pk=template.pk)
    
    templates = Template.objects.exclude(pk=pk)
    return render(request, 'app/template_form.html', {'template': template, 'templates': templates, 'action': 'Update'})
