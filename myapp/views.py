from django.shortcuts import render
import PyPDF2
from .forms import StudyPlanForm
from .models import StudyPlan

def upload_study_plan(request):
    if request.method == 'POST':
        form = StudyPlanForm(request.POST, request.FILES)
        if form.is_valid():
            study_plan = form.save(commit=False)
            # calculate score here
            with study_plan.file.open('rb') as f:
                reader = PyPDF2.PdfFileReader(f)
                # extract information from PDF here
                study_plan.score = 4.0 # replace with your own score calculation
            study_plan.save()
            return render(request, 'score.html', {'score': study_plan.score})
    else:
        form = StudyPlanForm()
    return render(request, 'upload.html', {'form': form})

def study_plan_list(request):
    study_plans = StudyPlan.objects.all()
    context = {'study_plans': study_plans}
    return render(request, 'study_plan_list.html', context)
