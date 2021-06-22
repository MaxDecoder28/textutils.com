# I have created this file - Manas
from django.http import HttpResponse
from django.shortcuts import render
         
def index(request):
        return render(request, 'index.html')
        # return HttpResponse('Home')
        
def ex1(request):
        s = '''<h2>Navigation Bar<br></h1>
        <a href = "https://www.amazon.in/s?k=lap+top&hvadid=72774002481786&hvbmt=bb&hvdev=c&hvqmt=p&tag=msndeskstdin-21&ref=pd_sl_4q7348m1ev_b"> Amazon Laptops</a><br>
        
        <a href = "https://Facebook.com">Facebook</a><br>
        <a href = "https://github.com">Github</a><br>
        <a href = "https://Flipkart.com">Flipkart</a><br>
        <a href = "https://Google.com">Google</a><br>'''
        
        return HttpResponse(s)

def analyze(request):
        # Get the Text
        djtext = request.POST.get('text','default')

        #Check Checkbox value
        removepunc = request.POST.get('removepunc','off')
        fullcaps = request.POST.get('fullcaps','off')
        newlineremover = request.POST.get('newlineremover','off')
        extraspaceremover = request.POST.get('extraspaceremover','off')
        charactercounter = request.POST.get('charactercounter','off')

        #Check with Checkbox is on
        if removepunc == "on":
                punctuations = '''!()-[]{};:'"\,<>.?@#$%^&*_-~'''
                analyzed = "" 
                for char in djtext:
                        if char not in punctuations:
                                analyzed = analyzed + char
                params = {'purpose':'Removed Punctuatations', 'analyzed_text': analyzed}
                djtext = analyzed
                return render(request, 'analyze.html', params)

        #Full Caps Checkbox is on
        elif(fullcaps=="on"):
                analyzed = ""
                for char in djtext:
                        analyzed = analyzed + char.upper()        
                        params = {'purpose':'Change to UpperCase', 'analyzed_text': analyzed}
                djtext = analyzed
                return render(request, 'analyze.html', params)
                

        elif(extraspaceremover=="on"):
                analyzed = ""
                for index, char in enumerate(djtext):
                        if not (djtext[index]==" " and djtext[index+1]==" "):   
                            analyzed = analyzed + char        
                        params = {'purpose':'extra space remover', 'analyzed_text': analyzed}
                djtext = analyzed
                return render(request, 'analyze.html', params)



        elif(newlineremover=="on"):
                analyzed = ""
                for char in djtext:
                        if char!="\n" and char!="\r":
                                analyzed = analyzed + char        
                        else:
                                print("no")
                                print("pre",analyzed)
                                params = {'purpose':'Removed New Line', 'analyzed_text': analyzed}
                djtext = analyzed
                return render(request, 'analyze.html', params)

        
        elif(charactercounter=="on"):
                analyzed = 0
                for char in djtext:
                                analyzed = analyzed + 1     
                                params = {'purpose':'Count the Character', 'analyzed_text': analyzed}
                djtext = analyzed
                return render(request, 'analyze.html', params)

                