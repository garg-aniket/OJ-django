from django.shortcuts import render
from django.http import HttpResponse
from .models import question

def index(request):
    ques=question.objects.all()
    data={'ques':ques}
    return render(request,'OJapp/index.html',data)
def test(request):
    qdict=request.GET
    fdict=qdict.dict()
    for key in fdict:
        questionno=key
    #print(fdict)
    data={'query':question.objects.get(id=questionno)}

    # for key, value in request.GET.items():
    #     print("%s %s" % (key, value))
    # ques=question.objects.all()
    # data={'ques':ques}
    return render(request,'OJapp/question.html',data)  
