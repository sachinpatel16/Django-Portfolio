from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Servies,ContectUs

from django.contrib.auth.decorators import login_required

# # Create your views here.
def index(request):
    serviesData=Servies.objects.all()
    data ={
        'serviesData':serviesData
    }
    
    if request.method == "POST":
            
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')
            
        user = ContectUs.objects.get_or_create(user_name=name ,user_mobile=mobile ,user_email=email, user_message=message)

    return render(request,'index.html',data)

def pa(request):
    if request.method == 'POST':
        pic = request.FILES.get('pic')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        url = request.POST.get('url')
        project = Servies.objects.get_or_create(servies_icon=pic,servies_title=title,servies_des=desc,servies_git_url=url)
        return redirect('/')
    return render(request,'pa.html')

def pd(request,pk):
    data = get_object_or_404(Servies, id=pk)
    if request.method == 'POST':
        pic = request.FILES.get('pic')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        url = request.POST.get('url')
            
        data.servies_icon=pic
        data.servies_title=title
        data.servies_des=desc
        data.servies_git_url=url
        data.save()
            
        return redirect('/')
        
    return render(request,'pd.html',{'data':data})

def delete(request,pk):
    data = get_object_or_404(Servies,id = pk)
    
    data.delete()
    return redirect('/')