from django.shortcuts import render
from .models import Blog
# 모델파일에서 블로그 가져와라
from django.shortcuts import get_object_or_404, redirect

from django.utils import timezone

from django.core.paginator import Paginator
# 페이지네이션하귀 위해

# 어떤 데이터를 어떻게 처리할지 함수로 정의해야됨

def  home(request):
    # 홈이라는 함수를 선언한다 리퀘스트를 인자로 받는다.
    blogs = Blog.objects
    # 블로그의 객체를 블로그스에 담아준다

    blog_list = Blog.objects.all()
    # 블로그 객체를 세개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # 해당페이지로 이동하는

    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

    # 쿼리셋과 메소드의 형식
    # 모델, 쿼리셋(objects).메소드

def detail(req , blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'detail.html' , {'details' : detail})
    # 어떤 클래스, 검색조건(몇번데이터,pk)
    # pk = primary key 객체들의 이름표, 구분자, 데이터의 대표값

def new(req):
    return render(req, 'new.html')

def create(req):
    blog = Blog()
    blog.title = req.GET['title']
    blog.body = req.GET['body']
    blog.pub_date = timezone.datetime.now()
    # 작성한 시간 기록됨
    blog.save()
    # 데이터베이스에 저장함

    return redirect('/blog/'+str(blog.id))
    # 위에 함수 처리하고 여기로 이동해요~~ url은 문자열로 형변환!! 
    # render와 다르게 외부 url도 가능