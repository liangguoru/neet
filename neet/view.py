# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.staticfiles import storage
import os
import time
import ast
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
baozhendir = os.path.join(BASE_DIR, 'static/goods/baozhen/')
lipaidir = os.path.join(BASE_DIR, 'static/goods/lipai/')
shubiaodiandir = os.path.join(BASE_DIR, 'static/goods/shubiaodian/')
yaoshikoudir = os.path.join(BASE_DIR, 'static/goods/yaoshikou/')
otherdir = os.path.join(BASE_DIR, 'static/goods/other/')

def get_all_subdir(path):
    dirlist = []
    root = []
    dirs = []
    files = []
    for root, dirs, files in os.walk(path, topdown=False):
        pass
    return dirs

def get_all_files(path,exceptfilelist):
    filelist = []
    for root, dirs, files in os.walk(path, topdown=False):
        pass
    for f in files:
        hitflag = False
        for _ in exceptfilelist:
            if _ in f:
                hitflag = True
                break;
        if not hitflag:
            filelist.append(f)
    return filelist


def index(request):
    print ("index was called!!\n")
    context = {}
    return render(request,'index.html',context)

def goods_panel(request):
    context = {}
    goodstype = request.path.replace("/","").replace("Pannel_","")
    context['name'] = goodstype
    goods_type_dir = os.path.join(BASE_DIR, 'static/goods/'+ goodstype + "/")
    gamelist = get_all_subdir(goods_type_dir)
    datalist = []
    for game in gamelist:
        data = {}
        gamedir = goods_type_dir + game + "/"
        gameicon = '/static/goods/'+ goodstype + "/" + game + "/icon.png"
        data["name"] = game
        data["link"] = "/" + "Detail_" + goodstype + "_" + game + "/"
        data["iconpath"] = gameicon
        datalist.append(data)
    context["datalist"] = datalist
    print ("++++++++++++++LGR Debug++++++++++++++\n", context)
    return render(request,'goodspannel.html',context)

def goods_detail(request):
    context = {}
    goodstype = request.path.split("_")[1]
    game = request.path.split("_")[2]
    context['name'] = game
    os_game_dir = os.path.join(BASE_DIR, 'static/goods/'+ goodstype + "/"  + game)
    game_dir = '/static/goods/'+ goodstype + "/" + game
    print("----------------------",os_game_dir)
    piclist = get_all_files(os_game_dir, ["icon.png","_Detail.png"])
    datalist = []
    for pic in piclist:
        data = {}
        data["name"] = pic.replace(".png","")
        data["picpath"] = game_dir + pic
        data["detail_picpath"] = game_dir + pic.replace(".png","") + "_Detail.png"
        datalist.append(data)
    context["datalist"] = datalist
    print ("++++++++++++++LGR Debug++++++++++++++\n", context)
    return render(request,'detailpage.html',context)

# def yaoshikou(request):
#     return JsonResponse({'success':1})

# def lipai(request):
#     return JsonResponse({'success':1})

# def shubiaodian(request):
#     return JsonResponse({'success':1})

# def other(request):
#     return JsonResponse({'success':1})





'''
def test(request):
    print ("test was called!!\n")
    concat = request.POST
    postBody = request.body
    #print(concat)
    _result = request.POST.get('result','[]')
    _msg = request.POST.get('msg','[]')
    print ("==============_result is :", _result)
    print ("==============_msg is :", _msg)
    return JsonResponse({'success':1})

def test2(request):
    print ("test2 was called!!\n")
    concat = request.POST
    postBody = request.body
    #print(concat)
    _files = request.POST.get('files','[]')
    _changelist = request.POST.get('changelist','')
    _author = request.POST.get('author','')
    _log = request.POST.get('log','')
    print ("_files is :", _files)
    print ("_changelist is:", _changelist)
    print ("_author is :", _author)
    print ("_log is :", _log)
    # print(type(postBody))
    # print(postBody)
    # _data = json.loads(postBody)
    # print ("request data is ", _data)
    #context = {}
    #context['hello'] = 'liangguoru'
    # return render(request,'index.html',context)
    return JsonResponse({'success':1})

def test3(request):
    print ("test3 was called!!\n")
    concat = request.POST
    postBody = request.body
    # print(concat)
    print ("POST is :", concat)
    # print ("==============body is :", postBody)
    return JsonResponse({'success':1})

def test4(request):
    print ("test4 was called!!\n")
    # concat = request.POST
    # postBody = request.body
    _data = eval( str(request.body,encoding = "utf-8") )
    print(type(_data),_data)
    # print ("==============POST is :", concat)
    # print ("==============body is :", postBody)
    return JsonResponse({'success':1})

def test5(request):
    print ("★★★★★★★★★★★★★★★test5 was called!!★★★★★★★★★★★★★★★★★★★★★★★★★★★\n")
    concat = request.POST
    #postBody = request.body
    # print(concat)
    #print ("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆POST is :", concat)
    # print ("==============body is :", postBody)
    msg = request.POST.get('msg','')
    clist = request.POST.get('clist','')
    saveerror = request.POST.get('saveerror','')
    tempfilelist = request.POST.get('tempfilelist','')
    diffcontent = request.POST.get('diffcontent','')
    diff_lines = request.POST.get('diff_lines','')
    files_change_lines = request.POST.get('files_change_lines','')
    makuroset = request.POST.get('makuroset','')
    check = request.POST.get('check','')
    print ("diff_lines = ",diff_lines)
    print ("files_change_lines = ",files_change_lines)
    print ("diffcontent = ",diffcontent)
    print ("makuroset = ",makuroset)
    print ("check = ",check)
    fname = str(int(time.time()*1000000))+".txt"
    if int(check) == 1:
        with open(fname,"w") as fd:
            fd.write("diff_lines = " + str(diff_lines) + '\n')
            fd.write("files_change_lines = " + str(files_change_lines) +'\n' )
            fd.write("diffcontent = " + str(diffcontent) + '\n')
            fd.write("makuroset = " + str(makuroset) + '\n')
            fd.write("check = " + str(check) + '\n')
    return JsonResponse({'success':1})

def qapost(request):
    print ("qapost is called!!")
    data = request.POST.get('svn_commit', '[]')
    data = ast.literal_eval(data)
    author = data.get('author', '[]')
    au_name = author.split('@')[0]
    paths = data.get('files', '[]')
    rev = data.get('rev','[]')
    log = data.get('log','[]')
    print ("=================================\nhere is the commit info:\nreversion = %s\nauthor = %s\nfiles = %s\n====================================\n"%(rev,author,str(paths)))
    return JsonResponse({'success':1})

def uassetcheck(request):
    print ("receiving postdata...\n")
    data = request.POST.get('svn_commit', '[]')
    data = ast.literal_eval(data)
    author = data.get('author', '[]')
    au_name = author.split('@')[0]
    files = data.get('files', '[]')
    rev = data.get('rev','[]')
    log = data.get('log','[]')  
    print ("=================================\nhere is the commit info:\nreversion = %s\nauthor = %s\nfiles = %s\n====================================\n"%(rev,author,str(files)))
    return JsonResponse({'success':1})
'''
