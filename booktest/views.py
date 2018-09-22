from django.shortcuts import render
from booktest.models import BookInfo
# Create your views here.


def index(request):
    #查询所有图书
    booklist = BookInfo.objects.all()

    context = {'title':'图书列表', 'booklist': booklist}
    return render(request, 'booktest/index.html', context)

def detail(request, id):
    #根据图书编号对应图书
    herolist = BookInfo.objects.get(id=id).heroinfo_set.all()
    #将图书信息传递到模板，然后渲染模板
    return render(request, 'booktest/detail.html', {'herolist': herolist})


