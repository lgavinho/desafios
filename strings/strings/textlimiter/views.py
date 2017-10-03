from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import TextForm
from .service import TextFormatter

def index(request):
    template = loader.get_template('textlimiter/index.html')

    result = ''
    quantity_lines = 20
    if request.method == "POST":
        form = TextForm(data=request.POST)
        if form.is_valid():
            text_source = form.cleaned_data['source']
            line_size = form.cleaned_data['line_size']
            justify = form.cleaned_data['justify']
            service = TextFormatter(text=text_source)
            if justify:
                result = service.limiter_and_justify(line_size_chars=line_size)
            else:
                result = service.limiter(line_size_chars=line_size)
            quantity_lines = service.count_lines(text=result)
    else:
        form = TextForm()

    context = {
        'form': form,
        'result': result,
        'quantity_lines': quantity_lines,
    }
    return HttpResponse(template.render(context, request))


