from django.shortcuts import render,redirect
from.models import items
from.forms import todoform
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# View for creating items
def createview(requests):
    form=todoform()
    if requests.method == 'POST':
        form=todoform(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(requests,'todocreate.html',{'forms':form})

# View for rendering base html
def todview(requests):
    item=items.objects.all()
    return render(requests,'base.html',{'items':item})

# View for deleting items
def deleteview(requests,todo_id):
    itemdelete=items.objects.get(id=todo_id)
    itemdelete.delete()
    return redirect('/')

#View for updating items
def updateview(request,todo_id):
    item_update=items.objects.get(id=todo_id)
    form=todoform(instance=item_update)
    if request.method =='POST':
        form=todoform(request.POST,instance=item_update)
        if form.is_valid():
            form.save()

            
        
            return redirect('/')
    
        
    return render(request,'updateform.html',{'forms':form})






        