# I have created this file - Astro

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'astro','place':'galaxy'}
    return render(request, 'index.html', params)

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    # print(djtext)
    # print(removepunc)
    # check which checkbox is on
    if removepunc == 'on':
        # analyze text
        # analyzed = djtext
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcounter == 'on':
        analyzed = " The character count is: "
        charcount = 0
        for char in djtext:
            charcount += 1
        analyzed = djtext + analyzed + str(charcount)
        params = {'purpose': 'Count Number of Characters', 'analyzed_text': analyzed}


    if removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcounter!='on':
        return HttpResponse("Error!")

    return render(request, 'analyze.html', params)
