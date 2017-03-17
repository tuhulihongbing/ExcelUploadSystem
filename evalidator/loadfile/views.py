# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import forms
from loadfile.models import User, Folder, Excelfile
# Create your views here.
def treat(request):
    return redirect(folder)

class UserForm(forms.Form):
    headImg = forms.FileField()
def upload(request):
    print 1
    if request.method == "POST":
        print 2
        uf = UserForm(request.POST,request.FILES)
        print uf
        if uf.is_valid():
            print 3
            headImg = uf.cleaned_data['headImg']
            user = User()
            user.headImg = headImg
            user.save()
            return HttpResponse("upload ok!")
    else:
        print 4
        uf = UserForm()
        # print('uf...%s' ) % str(uf)
    return render(request , 'index.html',{'uf':uf})

def getinfo(ItemPath, type, request):
    file ,item = None, None
    isfolder = True if type=="folder" else False
    currentfolder = {"id": 0, "name": "主目录"}
    level = []
    res = {     "currentpage": currentfolder,
                "folder"      : None,
                "file"        : file,
                "level"       : level,
                "isfolder"    : isfolder}
    info = {    "template"   :None,        "res":res    }
    try:
        ItemPath=int(ItemPath)
    except:
        ItemPath=None
    if type != 'folder':
        if Excelfile.objects.filter(id=ItemPath).count()==0:
            info["res"]["currentpage"]["name"]="404"
            info["template"]= "NoFound.html"
            return info
        else:
            name = Excelfile.objects.filter(id=ItemPath).values( "name")[0]
            level = [{"id":ItemPath,"name":name["name"]}]
            cfolder = Excelfile.objects.filter(id=ItemPath).values("folder_id", "folder__name")[0]
            ItemPath = cfolder["folder_id"]
    if Folder.objects.filter(id=ItemPath).count() == 0:
        item = Folder.objects.filter(parent__isnull=True).values("id", "name")
    else:
        item = Folder.objects.filter(parent_id=ItemPath).values("id", "name")
        file = Excelfile.objects.filter(folder__id=ItemPath).values("id", "name")
        current = Folder.objects.filter(id=ItemPath).values("name", "id")
        # print current
        currentfolder = {
            "id": current[0]["id"],
            "name": current[0]["name"]   }
        level= [currentfolder]+level
        parents = Folder.objects.filter(id=(current[0]["id"])).values("parent__name", "parent_id")
        while len(parents) > 0:
            if parents[0]["parent__name"]:
                level = [{
                    "id": parents[0]["parent_id"],
                    "name": parents[0]["parent__name"]
                }] + level
            parents = Folder.objects.filter(id=parents[0]["parent_id"]).values("parent__name", "parent_id")
    level = [{"id": 0, "name": "主目录", }] + level
    currentpagename=currentfolder if type == "folder" else level[-1]
    info["res"] = {
        "currentpage": currentpagename,
        "folder": item,
        "file": file,
        "level": level,
        "isfolder": isfolder    }
    return info


def folder(request):
    ItemPath=request.GET.get("path",None)
    # ViewMode=request.GET.get("ViewMode",None)
    info = getinfo(ItemPath, 'folder', request)
    # print info
    return render(request, info["template"] or 'index.html', {'res': info["res"]})

def file(request):
    ItemPath = request.GET.get("path", None)
    info = getinfo(ItemPath, 'file', request)
    return render(request, info["template"] or 'ExcelDetail.html', {'res': info["res"]})



def disk(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            headImg = uf.cleaned_data['headImg']
            user = User()
            user.headImg = headImg
            user.save()
            return HttpResponse("upload ok!")
    else:
        uf = UserForm()
        # print('uf...%s' ) % str(uf)
    return render(request , 'index.html',{'uf':uf})