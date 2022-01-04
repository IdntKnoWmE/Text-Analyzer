from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,"contact.html")

def analyze(request):
    analyze_data = request.POST.get('texti')
    sym = request.POST.get('remove_symbols')
    cap = request.POST.get('capitalize')
    up = request.POST.get('uppercase')
    lo = request.POST.get('lowercase')
    co = request.POST.get('count_words')

    res=analyze_data.strip("/n")
    res_arr=[]
    count_word=0
    analyze_data=""
    new_line=-1
    i=0
    while i<len(res):
        if res[i]=="\n":
            if new_line!=i-2 and res[i-2]!=".":
                res_arr.append(analyze_data.strip())
                analyze_data=""
            #print(i,new_line)
            new_line=i
            i+=1
                
        elif res[i]==".":
            if i>0 and res[i-1]!=".":
                res_arr.append((analyze_data+".").strip())
                count_word+=1
                analyze_data=""
            i+=1
        else:
            if len(analyze_data)==0 and res[i]==" ":
                i+=1
                continue
            if sym=="true":
                symbol = '''`~!@#$%^&*()_+-={}[];:'"<>,/?/]'''
                if res[i] not in symbol:
                    analyze_data+=res[i]
                    count_word+=1
            else:
                #print(ord(res[i]))
                analyze_data+=res[i]
                count_word+=1
            i+=1

    if len(analyze_data)>0:
        res_arr.append(analyze_data)
    
    if cap=="true":
        for i in range(len(res_arr)):
            #print(res_arr[i][0],res_arr[i][1])
            res_arr[i]=res_arr[i].capitalize()
    if up=="true":
        for i in range(len(res_arr)):
            res_arr[i]=res_arr[i].upper()
    if lo=="true":
        for i in range(len(res_arr)):
            res_arr[i]=res_arr[i].lower()
    if co!="true":
        count_word=None
    
    #print(new_line)
    
    return render(request,'analyze.html',{'result':res_arr,'count':count_word})