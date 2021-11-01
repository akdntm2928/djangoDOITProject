from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect,resolve_url
from django.utils import timezone

from ..forms import AnswerForm,Question
from ..models import Answer

@login_required(login_url="common:login")
def answer_create(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.method =="POST":
        form =AnswerForm(request.POST)
        if form.is_valid():
            answer= form.save(commit=False)
            answer.author =request.user
            answer.create_date =timezone.now()
            answer.question =question
            answer.save()
            # return redirect('pybo:detail', question_id=question.id)
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail',question_id=question.id),answer.id))   
    else:
        form =AnswerForm()
    context = { 'question': question, "form": form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request,answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    
    if answer.author != request.user:
        messages.error(request,'수정권한이 없습니다!')
        return redirect('pybo:detail', question_id = answer.question.id)

    if(request.method =="POST"):
        form = AnswerForm(request.POST,instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            # return redirect('pybo:detail', question_id = answer.question.id)
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail',question_id=answer.question.id),answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer':answer,"form":form}
    return render(request,'pybo/answer_form.html',context)

@login_required(login_url='common:login')

def answer_delete(request,answer_id):
    answer= get_object_or_404(Answer,pk=answer_id)

    if answer.author != request.user :
        messages.error(request,'수정권한이 없습니다!')
        return redirect('pybo:detail', question_id = answer.question.id)
        
    answer.delete()
    return redirect('pybo:detail', question_id = answer.question.id)


@login_required(login_url="common:login")
def vote_answer(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)

    if(answer.author == request.user):
        messages.error(request,'본인글에 추천이 불가능합니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail',question_id =answer.question.id)