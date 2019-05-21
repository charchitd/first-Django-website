# my file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    me = {'name':'charchit', 'place':'saturn'}
    return render(request, 'index2.html', me )#HttpResponse("Home")

def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    remove = request.GET.get('remove', 'default')
    fullcaps = request.GET.get('fullcaps', 'default')
    print(remove)

    # Ananlyze text
    #
    if remove == "on":
        punc = '''!()[]-{};:'"\,<>./?@#$%^&*_~`'''
        analyzed = ""

        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = { 'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if remove != 'on' and fullcaps != 'on':
        return HttpResponse(" Error 404! <br><a href ='/'>Back</a>")
       # return render(request, 'analyze2.html', params)
    return render(request,'analyze2.html', params)
    # else:
    #     return HttpResponse(" Error 404! <br><a href ='/'>Back</a>")
# def removefunc(request):
#     return HttpResponse("remove <a href = '/'>Back</a>")
#
# def newlineremove(request):
#     return HttpResponse("remove newline  <a href = '/' >Back</a>")
#
# def charcount(request):
#    return HttpResponse("count <a href = '/'>Back</a>")
def about(request):
    return render(request,'about.html')
