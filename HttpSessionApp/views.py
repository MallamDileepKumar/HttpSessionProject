from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'home.html')
def Calci(request):
    x = int(request.GET['n1'])
    y = int(request.GET['n2'])
    os = request.GET['cal']
    if os == 'ADD':
        z = x+y
    elif os == 'SUB':
        z = x-y
    elif os == 'MUL':
        z = x*y
    else:
        z = x/y
    request.session['z'] = z
    request.session.set_expiry(60)
    return HttpResponse(f"<center><h1 style='color:red'> Data was submitted successfully!😁😁 </center></h1>")

def Display(request):
    if request.session.has_key('z'):
        z = request.session['z']
        return HttpResponse(f"""<center><h1 style='color:red'> The result is {z} (❁´◡`❁) </center></h1>""")
    else:
        return render(request,'home.html')
