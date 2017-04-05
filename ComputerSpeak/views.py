from django.http import HttpResponse
from django.shortcuts import render
from .input_converters import *


def home(request):
    return render(request, 'index.html')


def translate(request):
    input_text = request.GET['inputText']
    input_type = request.GET['input_types']

    output_type = request.GET['output_types']
    output_text = convert_inputs(input_text, input_type, output_type)

    return render(request, 'index.html', {'output_text': output_text, 'input_text': input_text})
    # return HttpResponse("You're on the translate page. " + translation)
