from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # data= 생략 가능
        if form.is_valid():
            form.save()
            ## add_message
            # messages.add_message(request, messages.INFO, '게시글이 성공적으로 작성되었습니다.')
            ## shortcut
            messages.info(request, '게시글 작성 완료!')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = { 
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # messages.add_message(request, messages.WARNING, '게시글이 삭제되었습니다.')
    messages.warning(request, '게시글이 삭제되었습니다.')
    return redirect('articles:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, '게시글이 수정되었습니다.')
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
