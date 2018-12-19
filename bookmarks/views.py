# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render



def main_page(request):
    output='''
     <html>
       <head>%s</head>
       <body><h1>%s</h1><p>%s</p></body>
     </html>
    '''%('Django bookmarks','Welcome to Django Bookmarks','Where you can store and share bookmarks!')
    return HttpResponse(output)
# Create your views here.
