from django.shortcuts import render
from django.http import HttpResponse

from plotly.offline import plot
import plotly.graph_objs as go



# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    ibd50 = {'gme' : 1, 'tsla' : 2, 'aapl' : 3}
    g250 = {'tme': 1, 'fslr': 2, 'lpx' : 3}
    indrank = {'autos':1, 'solar':2, 'ecom':3}

    context = {'ibd50' : ibd50, 'growth250' : g250, 'indrank' : indrank}
    return render(request, 'marketsmith/index.html', context)

def growth(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    fig = go.Figure()
    scatter = go.Scatter(x=[0,1,2,3], y=[0,1,2,3],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')
    fig.add_trace(scatter)
    plt_div = plot(fig, output_type='div')
    context = {"graph": plt_div}
    return render(request, 'marketsmith/thegrowthlist.html', context)

def industryrank(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # df = px.data.gapminder().query("country=='India'")
    fig = go.Figure()
    scatter = go.Scatter(x=[0,1,2,3], y=[0,1,2,3],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')
    fig.add_trace(scatter)
    plt_div = plot(fig, output_type='div')
    context = {"graph": plt_div}
    return render(request, 'marketsmith/industryrank.html', context)

def the50(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    fig = go.Figure()
    scatter = go.Scatter(x=[0,1,2,3], y=[0,1,2,3],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')
    fig.add_trace(scatter)
    plt_div = plot(fig, output_type='div')
    context = {"graph": plt_div}
    return render(request, 'marketsmith/the50.html', context)

def login(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'marketsmith/login.html', context)

def register(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'marketsmith/register.html', context)

def logout(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'marketsmith/logout.html', context)