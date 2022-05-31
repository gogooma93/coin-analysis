from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .models import BitcoinER


# Create your views here.
def index(request):
    return render(request, 'coinanalysis/index.html')

def home(request):
    return render(request, 'coinanalysis/home.html')

def coins(request):
    return render(request, 'coinanalysis/coins.html')

def chart(request):
    return render(request, 'coinanalysis/chart.html')

def qna(request):
    return render(request, 'coinanalysis/qna.html')

def bitcoiner_graph(request):
    data = BitcoinER.objects.filter(date__range=["2021-01-01", "2021-12-31"])
    bitcoin_exchange_rate = pd.DataFrame(list(data.all().values('close', 'date', 'high', 'id', 'low', 'open', 'value', 'volume', 'won')))

    x = bitcoin_exchange_rate.date
    y1 = bitcoin_exchange_rate.open
    y2 = bitcoin_exchange_rate.high
    y3 = bitcoin_exchange_rate.low
    y4 = bitcoin_exchange_rate.close
    y5= bitcoin_exchange_rate.won

    plt.rcParams['figure.figsize'] = (35, 15)
    fig, ax1 = plt.subplots()
    ax1.plot(x, y1, color='#FFD4AB', label='open')
    ax1.plot(x, y2, color='#B72E16', label='high')
    ax1.plot(x, y3, color='#FF692D', label='low')
    ax1.plot(x, y4, color='#FFB681', label='close')
    ax1.tick_params(axis='x', labelsize=20)
    ax1.tick_params(axis='y', labelsize=20)
    ax1.set_xlabel('date', fontsize=30) 
    #ax1.set_ylabel(['open', 'high', 'low', 'close'], fontsize=25) 
    ax1.set_title('bitcoin_exchange_rate', fontsize=40)
    ax1.legend(loc=2, fontsize=20)
    ax1_ylabels = ["", 30000000, 40000000, 50000000, 60000000, 70000000, 80000000]
    ax1.set_yticklabels(ax1_ylabels)

    ax2= ax1.twinx()
    ax2.plot(x, y5, color='#1973DF', linewidth=2.0, label='exchange_rate')
    ax2.tick_params(axis='y',labelsize=20)
    ax2.legend(loc=1, fontsize=20)
    #ax2.set_ylim([1083.10, 1199.10 ]) #수정필요
    plt.savefig("C:/bit/source/project/django/coinRoot/static/images/bitcoin_exchange_rate.png")
    

    return render(request, 'coinanalysis/chart.html', {'data':bitcoin_exchange_rate})