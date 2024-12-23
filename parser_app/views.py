from django.shortcuts import render
from . import models, forms
from django.views import generic
from django.http import HttpResponse

class JutsuListView(generic.ListView):
    template_name = 'parser/jutsu_list.html'
    context_object_name = 'jutsu'
    model = models.JutsuModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
class JutsuFormView(generic.FormView):
    template_name = 'parser/jutsu_form.html'
    from_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(JutsuFormView, self).post(request, *args, **kwargs)

    
