from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from tasks.forms import GradeForm
from tasks.models import Grade, Candidate


class CandidateList(View):
    def get(self, request):
        return JsonResponse({
            "data":
                [{'pk': candidate.pk, 'full_name': candidate.full_name(),
                  'avg_grade': candidate.get_avg_grade, 'grades': candidate.get_grade_list} for candidate in
                 Candidate.objects.all()]
        }, safe=False)


class AddMarkView(View):
    def get(self, request):
        form = GradeForm()
        return render(request, 'grade_form.html', {
            'form': form
        })

    def post(self, request):
        form = GradeForm(data=request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, 'Invalid form')
            return redirect('add-mark')
        if Grade.objects.filter(task=form.cleaned_data['task'], candidate=form.cleaned_data['candidate']):
            messages.add_message(request, messages.WARNING, 'The task has already been graded')
            return redirect('add-mark')
        form.save()
        messages.add_message(request, messages.SUCCESS, 'The task was graded successfully')
        return redirect('add-mark')
