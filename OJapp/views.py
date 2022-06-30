from django.shortcuts import render
import json
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from .models import question,testCase
from . import runcode1
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
def result(request):
    print(request.POST)
    
    
    if request.method == 'POST':
        code = request.POST['code']
        typecode = request.POST['type']
        print(typecode)
    # fdict=qdict.dict()
    # print(fdict)
    # for key,value in fdict:
    #     print(key,value)
    s,t=runcode1.run_py_code(typecode,[""],code) 
    print(s,t)
    data={'stdout':s,'stderr':t}
    return render(request,'OJapp/result.html',data)
def submitCode(request):
    data=json.load(request)
    typep=data.get('type')
    id=data.get('id')
    code=data.get('code')
    print(code)
    question1=question.objects.get(id=id)
    print(question1)
    testcases=list(testCase.objects.filter(questionTitle=question1))
    inputCases=[]
    expectedCases=[]
    for x in testcases:
        inputCases.append(x.Input.strip())
        expectedCases.append(x.ExpectedOutput)
    print(inputCases)
    print(expectedCases)  
    output,error=runcode1.run_py_code(typep,inputCases,code)
    result=[]
    if(not error):
        for x in range(0,len(expectedCases)):
            if(expectedCases[x].rstrip()==output[x].rstrip()):
                print("R")
                result.append("Right Answer")
            else:
                result.append("Wrong Answer") 
                print("W")            
            print(output[x])
    else:
        print(error)        
    tes = serializers.serialize("json", testcases)
    compmess={'compileMessage':result}
    ts=json.dumps(compmess)
    tes=tes[:len(tes)-1]+","+ts+"]"
    print(len(tes))
    return HttpResponse(tes, content_type='application/json')
def runCode(request):
    data=json.load(request)
    print(data)
    typep=data.get('type')
    id=data.get('id')
    code=data.get('code')
    customInput=data.get('custInpt')
    print(customInput)
    # question1=question.objects.get(id=id)
    # print(question1)
    # testcases=list(testCase.objects.filter(questionTitle=question1))
    inputCases=[]
    inputCases.append(customInput)
    # expectedCases=[]
    # for x in testcases:
    #     inputCases.append(x.Input)
    #     expectedCases.append(x.ExpectedOutput)
    # print(inputCases)
    # print(expectedCases)  
    output,error=runcode1.run_py_code(typep,inputCases,code)
    print(output,error)
    # result=[]
    # if(not error):
    #     for x in range(0,len(expectedCases)):
    #         if(expectedCases[x].rstrip()==output[x].rstrip()):
    #             print("R")
    #             result.append("Right Answer")
    #         else:
    #             result.append("Wrong Answer") 
    #             print("W")            
    #         print(output[x])
    # tes = serializers.serialize("json", testcases)
    # compmess={'compileMessage':result}
    # ts=json.dumps(compmess)
    # tes=tes[:len(tes)-1]+","+ts+"]"
    # print(len(tes))
    
    compileStatus="Successfull"
    if(error):
        compileStatus="Error"    
    datareturn={'compileStatus':compileStatus,'output':output,'Error':error}
    return JsonResponse(datareturn, content_type='application/json')