from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .input_converters import *


def home(request):
    return render(request, 'index.html')


def translate(request):
    print(request)
    input_text = request.GET['inputText']
    print(input_text)
    input_type = request.GET['input_types']

    output_type = request.GET['output_types']
    output_text = convert_inputs(input_text, input_type, output_type)

    data = {'output_text': output_text, 'input_text': input_text}
    print(data)
    #return render(request, 'index.html', data)
    #return HttpResponse(data)
    return JsonResponse(data)
