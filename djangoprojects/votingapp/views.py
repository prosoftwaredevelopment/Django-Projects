from django.shortcuts import render
# Create your views here.
def index(request):
    arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby', 'Delphi', 'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']
    mydictionary = {
        "arr" : arr
    }
    return render(request,'index.html',context=mydictionary)

