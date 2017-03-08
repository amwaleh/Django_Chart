from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .data.data_json import DATA
import random


class ChartView(View):

    def get(self,request):
        return render(request,'index.html',{'data':DATA})


def data_analysis(request):


    result = dict(labels=list(), data=list(), color=list())

    for item in DATA:
        r = lambda: random.randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())
        result['labels'].append(item['country'])
        result['data'].append(item['population'])
        result['color'].append(color)


    return JsonResponse(result)