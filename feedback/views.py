from django.shortcuts import render, redirect
from .models import Form, Questions, Answer
from .forms import AnswerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def feedform(request, slug):
	t_obj = Form.objects.get(form_slug_url=slug)
	t_name=f'{t_obj.Recipient.first_name} {t_obj.Recipient.last_name}'
	Questions_obj_list = Questions.objects.filter(forms=t_obj)
	formset = []
	flist = []
	i=0
	if request.method == 'POST':
		q1=Questions_obj_list[0]
		a1=Answer.objects.filter(Question=q1)
		for i in range(len(a1)):
			if a1[i].author == request.user:
				messages.success(request, f'You already filled {t_obj.Recipient.first_name} {t_obj.Recipient.last_name}\'s feedback form.')
				return redirect("home")
		descibe=dict(request.POST)['Descibe']
		rate=dict(request.POST)['Rate']
		print(rate)
		for i,Ques in enumerate(Questions_obj_list):
			ans_form =AnswerForm(request.POST)
			print(ans_form.is_valid())
			if ans_form.is_valid():
				obj=ans_form.save(commit=False)
				obj.Question = Ques
				obj.Descibe = descibe[i]
				obj.Rate = rate[i]
				obj.author = request.user
				formset.append((Ques, ans_form))
		for n, formsobj in formset:
			flist.append(formsobj)
		i=0
		for fobj in flist:
			if fobj.is_valid():
				fobj.save()
				i+=1
			if i == len(flist):
				messages.success(request, f'Your feedback form registered successfully.')
				return redirect("home")

	else:
		for Ques in Questions_obj_list:
			ans_form =AnswerForm()
			obj=ans_form.save(commit=False)
			obj.Question = Ques
			obj.author = request.user
			formset.append((Ques, ans_form))

	context = {
		'formset': formset,
		'Recipient': t_name
	}

	return render(request, 'form.html', context)
@login_required
def FormView(request, slug):
	t_obj = Form.objects.get(form_slug_url=slug)
	t_name=f'{t_obj.Recipient.first_name} {t_obj.Recipient.last_name}'
	Questions_obj_list = Questions.objects.filter(forms=t_obj)

	QA_set = []
	TotalRate = 0
	if request.user == t_obj.Recipient or request.user.is_superuser:
		try:
			for ques in Questions_obj_list:
				QuesRate = 0
				for obj in Answer.objects.filter(Question=ques):
					QuesRate += obj.Rate
				QuesRateAverage = float("{:.2f}".format(10*(QuesRate/(10*len(Answer.objects.filter(Question=ques))))))
				QA_set.append([ques,Answer.objects.filter(Question=ques), 
					QuesRateAverage])
				TotalRate += QuesRateAverage

			TotalRateAverage = float("{:.2f}".format(TotalRate/len(Questions_obj_list)))
		except ZeroDivisionError:
			for ques in Questions_obj_list:
				QuesRate = 0
				for obj in Answer.objects.filter(Question=ques):
					QuesRate += obj.Rate
				QuesRateAverage = 0
				QA_set.append([ques,Answer.objects.filter(Question=ques), 
					QuesRateAverage])
				TotalRate += QuesRateAverage

			TotalRateAverage = "NULL"
	else:
		TotalRateAverage = False
	context = {
		'QA_set': QA_set,
		'Recipient': t_name,
		'TotalRateAverage': TotalRateAverage,
	}

	return render(request, 'feedsview.html', context)