from django.shortcuts import render
from django.core import serializers
from .models import *
from .form import QuestionForm, SpotForm
from django.http import JsonResponse
from django.http import HttpResponse
import json
import requests as r
import ast
import time

url='http://vps400202.ovh.net'


def authentification():
	res = r.post(url+"/superapi/auth/",
		{'username': 'mtsgo', 'password': 'mtsgoisfun'})
	auth_data = ast.literal_eval(res.text)
	token = auth_data["token"]
	user_id =auth_data["user_id"]
	auth ={'token' : token, 'user_id' : user_id}
	return(auth)

def string_to_list(string):
	list=string.split(',')
	int_list=[]
	for i in list:
		int_list.append(int(i))
	return int_list

"""def afficher_stats(request):
	auth=authentification()
    data = serializers.serialize("json", Stats.objects.all()) #sérialise les stats en json
    json_data = json.loads(data)
    return render(request, 'admini/stats.html', locals())"""

def afficher_stats(request):
	auth=authentification()
	res =r.get(url+"/superapi/stats/", auth)
	json_data=res.json()
	print(json_data)
	if res.status_code == 200:
		return render(request, 'admini/stats.html', locals())
	else:
		return("error state")


"""def afficher_questions(request):
    data = serializers.serialize("json", Question.objects.all()) #sérialise les questions en json
    #questjson=JsonResponse(data, status=200, safe=False)
    json_data = json.loads(data)
    print(json_data)
    return render(request, 'admini/questions.html', locals())"""

def afficher_questions(request):
	auth=authentification()

	res=r.get(url+"/superapi/questions/", auth)
	data = res.json()
	json_data = data['questions']
	return render(request, 'admini/questions.html', locals())

#def view_question(request, id_question):

        #return HttpResponse(

        #"Vous avez demandé la question #{0} !".format(id_question)

"""def ajout_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
	    question=Question()
	    question.identification = form.cleaned_data['identification']
	    question.questionText = form.cleaned_data['questionText']
	    question.answer1 = form.cleaned_data['answer1']
	    question.answer2 = form.cleaned_data['answer2']
	    question.answer3 = form.cleaned_data['answer3']
	    question.answer4 = form.cleaned_data['answer4']
	    question.rightAnswer = form.cleaned_data['rightAnswer']
	    question.difficulty = form.cleaned_data['difficulty']
	    question.topic = form.cleaned_data['topic']
	    question.score = form.cleaned_data['score']
	    envoi=True
	    question.save()
    return render(request, 'admini/ajout_question.html', locals())"""

def ajout_question(request):
	auth=authentification()
	form = QuestionForm(request.POST or None)
	data={}
	if form.is_valid():
		data = {'question':
			{'questionText': form.cleaned_data['questionText'],
					'answer1' : form.cleaned_data['answer1'],
					'answer2' : form.cleaned_data['answer2'],
					'answer3' : form.cleaned_data['answer3'],
					'answer4' : form.cleaned_data['answer4'],
					'rightAnswer' : form.cleaned_data['rightAnswer'],
					'difficulty' : form.cleaned_data['difficulty'],
					'score' : form.cleaned_data['score'],
					'topic' : form.cleaned_data['topic']}
				}
		envoie=True
	data.update(auth)
	print(data)
	res = r.post(url+"/superapi/questions/", json.dumps(data))
	print(res.status_code)
	print(res.text)
	return render(request, 'admini/ajout_question.html', locals())


def ajout_spot(request):
	auth=authentification()
	form = SpotForm(request.POST or None)
	if form.is_valid():
		res = r.post(url+"/superapi/spots/", json.dumps({'token' : auth['token'], 'user_id' : auth['user_id'],
                                                           'spot':{'centrex' : form.cleaned_data['centrex'], 'centrey': form.cleaned_data['centrey'], 'centrez':form.cleaned_data['centrez'], 'rayon':form.cleaned_data['rayon'],
                                                                   'currentQuestion' : form.cleaned_data['currentQuestion'],
                                                                   'questionList': string_to_list(form.cleaned_data['questionList']),
                                                                   'startTime' : time.time(),
                                                                   'delay' : form.cleaned_data['delay']}}))
		envoi=True
	return render(request, 'admini/ajout_spot.html', locals())

def afficher_carte(request):
	auth=authentification()
	res = r.get(url+"/superapi/spots/", auth)
	spots=ast.literal_eval(res.text)['spots']
	spotsList={}
	for spot in spots:
		print(spot['centrex'])
	print(spots)
	return render(request, 'admini/carte.html', locals())