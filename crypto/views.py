from django.shortcuts import render
from .parsers import coingecko, cryptorank

def index(request):
    return render(request, 'crypto/index.html', { 'title': 'Тестовое задание Web3Space' })

def cryptorank_view(request):
    data = cryptorank.find_target_data()
    return render(request, 'crypto/data_table.html', { 'title': 'Cryptorank', 'table_headers': ['Наименование', 'Тег', 'Timestamp'], 'data': data })

def coingecko_view(request):
    data = coingecko.find_target_data()
    sort = request.GET.get('sort')
    descending = request.GET.get('descending')
    if sort is not None:
        data = sorted(data, key=lambda d: d['title'].lower(), reverse=bool(descending))
    return render(request, 'crypto/data_table_with_sort.html', { 'title': 'Coingecko', 'table_headers': ['Наименование', 'Цена', 'Timestamp'], 'data': data })