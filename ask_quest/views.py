from django.shortcuts import render
 
from django.http.response import HttpResponse
from . forms import UserForm
from .models import Chapter, Question, Response
from django.http import HttpResponseRedirect

def question(request,question_id):
     response_list = Response.objects.filter(question=question_id )
     chapter_name=Question.objects.get(id=question_id).chapter.chapter_name
     question_text=Question.objects.get(id=question_id).question_text
     data = {
            'chapter_name':chapter_name,
            'response_list': response_list ,
            'question_text':question_text
            }
     return render(request, "ask_quest/question.html", context=data)

def detail(request, chapter_id):
    if request.method == "POST":
        question=Question()
        question.question_text = request.POST.get("question_text")
        question.quote_text = request.POST.get("quote_text")
        chapter = Chapter.objects.get(id=chapter_id)
        question.chapter=chapter
        question.save()
        print(question .question_text)
        return HttpResponseRedirect("")
        pass
    else:
        question_list = Question.objects.filter(chapter=chapter_id )
        #question_text_list=[xx.question_text for xx in question_list]
        userform = UserForm()
        data = {
            'chapter_name':Chapter.objects.get(id=chapter_id ).chapter_name,  #filter(id=chapter_id )[0].chapter_name,
            'question_list': question_list ,
            "form": userform
            }
        return render(request, "ask_quest/detail.html", context=data)



def index(request):
    chapter_list = Chapter.objects.order_by('-pub_date')
    userform = UserForm()
    data = {
        'chapter_list': chapter_list,
                    }
    return render(request, "ask_quest/index.html", context=data)


