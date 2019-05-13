from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Index')


def add_book(request):
    pass


def import_book(request):
    pass
