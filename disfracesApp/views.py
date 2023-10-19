from django.shortcuts import render
def indexTemplate(request): 
    return render(request, 'index.html') #

def fantasmaTemplate1(request):
    data = {'check': 'True'}
    return render(request, 'Home.html', data)

def calabazaTemplate1(request):
    data = {'calabaza' : 'true'}
    return render(request, 'Home.html', data)
def loboTemplate1(request):
    data = {'lobo' : 'true'}
    return render(request, 'Home.html', data)

def fantasmaTemplate2(request):
    data = {'False': 'False'}
    return render(request, 'Home.html', data)

def app2Template1(request):
    data = {'check': 'True'}
    return render(request, 'Home.html', data)

def app2Template2(request):
    data = {'check': 'True'}
    return render(request, 'app2.html', data)