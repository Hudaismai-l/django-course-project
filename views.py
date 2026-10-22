from django.shortcuts import render

def submit(request):
    # Placeholder logic for submitting an exam
    return render(request, 'onlinecourse/exam_result_bootstrap.html')

def show_exam_result(request):
    # Placeholder logic for showing the exam result
    context = {
        'score': 100,
        'message': 'Congratulations!'
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)