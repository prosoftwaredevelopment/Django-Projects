from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
def index(request):
    arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby', 'Delphi', 'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']
    mydictionary = {
        "arr" : arr
    }
    return render(request,'index.html',context=mydictionary)

def getquery(request):
    q = request.GET['languages']
    return HttpResponse(q)
