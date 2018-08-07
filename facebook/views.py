from django.shortcuts import render, redirect
# render는 페이지를 보여줘라, redirect는 페이지로 연결해라
from facebook.models import Article, Comment

# Create your views here.

def play(request):
    return render(request, 'play.html')


count=0
def play2(request):
    psy='박시용'
    age=15

    global count
    count = count+1

    if age > 18:
        status = '성인입니다.'
    else:
        status = '미성년자입니다.'


    if count==7:
        apple = "당첨!입니다."
    else:
        apple = "꽝..입니다."


    diary = ['안녕하세요(월요일)', '맑음(화요일)', '흐림(수요일)']

    return render(request, 'play2.html', {'name':psy, 'count':count, 'status':status, 'diary':diary, 'apple':apple })


def play3(request):
    return render(request, 'play3.html')


def fail(request):
    return render(request, 'fail.html')


def newsfeed(request):
    # DB에서 (Article)에서 글을 꺼내오는 작업
    # 만든 DB, 꺼내와라, 전부 (실행)
    articles = Article.objects.all()
    return render (request, 'newsfeed.html', { 'articles': articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    # pk는 글번호
    # 코멘트 쓰기를 했다면, 코멘트를 등록해라
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['author'],
            text=request.POST['text'],
            password=request.POST['password']
        )
        return redirect(f'/feed/{article.pk}')

    return render(request, 'detail_feed.html', {'post':article })

def new_feed(request):
    # 받은 데이터를 등록해라
    if request.method == 'POST':
        # post라는게 활성화 되면..
        # 여기에 코드작성예정
        post = Article.objects.create(
            author=request.POST['writer'],
            title=request.POST['title'],
            text=request.POST['content'],
            # text=f'{request.POST['content']} - 추신~~~~',
            # text=request.POST['content'] + '- 추신~~~~',
            password=request.POST['pw']
        )

        #방금쓴 글의 자세히 보기 페이지로 이동을 해라
        return redirect(f'/feed/{post.pk}')
    # ''앞에 f를 넣고 중괄호로 닫늗다. f는 변수를 출력하라는 의미(중괄호 안에 있는걸 꺼내서)따옴표''안에 있는걸. pk는 primary key

    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    # 수정해주세요 관련 로직
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        if request.POST['pw'] == article.password:
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.author = request.POST['writer']
            article.save()

        #방금쓴 글의 자세히 보기 페이지로 이동을 해라
        return redirect(f'/feed/{article.pk}')

    return render(request, 'edit_feed.html', {'feed':article})

def remove_feed(request, pk):
    # 삭제해주세요
    if request.method == 'POST':
        # post라는게 활성화 되면..
        article = Article.objects.get(pk=pk)
        if request.POST['pw'] == article.password:
            article.delete()
            return redirect('/')
        #방금쓴 글의 자세히 보기 페이지로 이동을 해라

    return render(request, 'remove_feed.html')