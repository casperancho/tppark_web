from django.shortcuts import render

def base(request):
    args = {}
    args['questions']=[1,2,3,4]
    return render(request,'ask_app/index.html', args)