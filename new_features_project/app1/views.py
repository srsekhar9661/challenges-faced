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


# views.py
import json
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import default_storage

class FileUploadView(View):
    def get(self, request):
        return render(request, 'pdf_processing.html')

    def post(self, request):
        uploaded_file = request.FILES['file']
        file_path = default_storage.save(uploaded_file.name, uploaded_file)

        # Process the file to find fillable widgets
        fillable_widgets = self.process_file(file_path)

        # Delete the file after processing if necessary
        default_storage.delete(file_path)

        return JsonResponse({'fillable_widgets': fillable_widgets})

    def process_file(self, file_path):
        # Replace this with your file processing logic
        # For example, parse the file and find fillable widgets
        # Return a list of widget names or IDs
        import pymupdf

        doc = pymupdf.open(file_path)
        widgets_list = []
        radio_button_group = {}

        json_data = {}
        for page in doc:
            widgets = page.widgets()
            if widgets:
                l = []
                
                for  widget in widgets:
                    # if widget.field_type
                    if widget.field_type_string == 'RadioButton':
                        # if widget.field_name 
                        print(f"Radio button group before {radio_button_group}")
                        same_radio_field_list = radio_button_group.get(widget.field_name, [])
                        print(f"getting the same radio field list before {same_radio_field_list}")
                        # import ipdb;ipdb.set_trace(context=5)
                        value = f"{widget.field_name}____{len(same_radio_field_list)+1}"
                        print(f"value genrating {value}")
                        
                        l.append(value)
                        same_radio_field_list.append(value)
                        radio_button_group[widget.field_name] = same_radio_field_list

                        print(f"Radio button group affter {radio_button_group}")
                        print(f"getting the same radio field list after {same_radio_field_list}")

                        json_data[value] = value
                        
                    else:
                        l.append(widget.field_name)
                        json_data[widget.field_name] = widget.field_name
                    print(f"widget type {widget.field_type}")
                    print(f"widget field type string {widget.field_type_string}")
                    print(f"widget label {widget.field_label}")
                    print(f"widget name {widget.field_name}")
                    print(f"widget value {widget.field_value}")
                    print(f"widget choice values {widget.choice_values}")
                    print(f"widget display {widget.field_display}")
                    print('*'*50)
                # widgets_list.extend([widget.field_name for widget in widgets])
                widgets_list.extend(l)

                import json
                with open('test_josn_data.json', 'w') as fp:
                    json.dump(json_data, fp, indent=4)
        return widgets_list
    

class Retrieve(View):
    def get(self, request):
        import json
        import re

        original_data = []
        # this test_json_adat is like the json file that is used for the matching field regarding the fillable fields in the pdf
        with open(r'C:\Users\sekhar\Desktop\Sekhar\challenges-faced\new_features_project\test_josn_data.json', 'r') as fp:
            data = json.load(fp)
            
            for k, v in data.items():
                # in the original file the format to find the RadioButton is it ends with ____[0-9]{0,3}
                match = re.search(r'__[0-9]{0,3}$', k)
                if match:
                    print(k[:-(len(match.group())  + 2)])
                    original_data.append(k[:-(len(match.group())  + 2)])
                    continue
                print(k)
                original_data.append(k)
        return JsonResponse({'fillable_widgets':original_data})

