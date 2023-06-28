from django.shortcuts import render
from django.http  import HttpResponse

projectsList = [
    {
        'id':'1',
        'title':'ecommerce websie',
        'description':'something like amazon'
    },
     {
        'id':'2',
        'title':'ecommerce websie2',
        'description':'something like amazon2'
    },
     {
        'id':'3',
        'title':'ecommerce websie3',
        'description':'something like amazon3'
    }
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page' : page,'number':number,'projects':projectsList}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = None
    for  i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request,'projects/single-project.html',{'project':projectObj})
