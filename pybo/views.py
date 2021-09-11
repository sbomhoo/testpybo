from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .models import Answer
from django.utils import timezone

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)  #템플릿으로 렌더링
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

#답변등록
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'),create_date=timezone.now())
    # question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)
