from django.shortcuts import render
from django.db.models import Sum, Avg
from django.http import JsonResponse
from .models import Population
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random


def index(request):
    # Group data and find
    data = Population.objects.values('country__name').annotate(total=Sum('population')).order_by('-total')
    paginator = Paginator(data,5)
    page = request.GET.get('page')

    # pagination
    try:
        page_content = paginator.page(page)
    except PageNotAnInteger:
         page_content = paginator.page(1)
    except EmptyPage:
        page_content = paginator.page(paginator.num_pages)

    return render(request,'index.html',{'data':page_content})



def data_analysis(request):
    # Group data by Country and return total population per country
    data = Population.objects.values('country__name').annotate(total=Sum('population')).order_by('-total')

    # Dictionary to hold graph data
    graph_data = {
        'title':'Population per country(M)',
		'labels': [],       # Holds  labels for the dataset
		'data': [],         # Holds the data point
		'color': []         #  Holds the auto generated color code for each data point
		}

    # Generate random Hex color code
    r = lambda: random.randint(0, 255)

    # Generate labels and data values for graph plotting
    for item in data:
        color = '#{:X}{:X}{:X}'.format(r(), r(), r())
        graph_data['labels'].append(item.get("country__name"))
        graph_data['data'].append(item.get("total"))
        graph_data['color'].append(color)
    # Return Json response
    return JsonResponse(graph_data)
