from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Population
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


class ChartView(View):

    def get(self,request):
        data = Population.objects.all()
        paginator = Paginator(data,5)
        page = request.GET.get('page')

        try:
            info = paginator.page(page)
        except PageNotAnInteger:
             info = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            info = paginator.page(paginator.num_pages)

        return render(request,'index.html',{'data':info})


def data_analysis(request):

    data = Population.objects.all()
    result = dict(labels=list(), data=list(), color=list())

    for item in data:
        r = lambda: random.randint(0,255)
        color = '#{0:X}{1:X}{2:X}'.format(r(),r(),r())
        result['labels'].append(item.country)
        result['data'].append(item.population)
        result['color'].append(color)


    return JsonResponse(result)