import json
import csv
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import HttpResponse
from .utils import load_survey_definition, load_page_links
from .models import SurveySubmission, SurveyAnswer  # Use consistent models
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .utils import ask_llama3


@csrf_protect
def survey_form(request):
    # Load the survey definition and page links
    survey_data = load_survey_definition()
    page_links = load_page_links()
    survey_data_json = json.dumps(survey_data)

    if request.method == 'GET':
        return render(request, 'survey_app/survey_form.html', {
            'survey_data_json': survey_data_json
        })
    else:
        all_question_ids = [q['id'] for q in survey_data['questions']]
        open_ended_ids = [q['id'] for q in survey_data['openEndedQuestions']]
        all_ids = all_question_ids + open_ended_ids

        has_answers = any(q_id in request.POST for q_id in all_ids)
        if not has_answers:
            return render(request, 'survey_app/survey_form.html', {
                'survey_data_json': survey_data_json,
                'error_message': 'Please answer at least one question before submitting.'
            })

        submitted_time = now()
        submission = SurveySubmission.objects.create(submitted_time=submitted_time)
        tally = {}

        for q_id in all_ids:
            if q_id in request.POST:
                user_answer = request.POST[q_id]
                SurveyAnswer.objects.create(
                    submission=submission,
                    question_id=q_id,
                    answer_text=user_answer
                )
                matching_question = next(
                    (question for question in survey_data['questions'] if question['id'] == q_id), 
                    None
                )
                if matching_question and matching_question.get('type') == 'multiple-choice':
                    chosen_ans = next(
                        (ans for ans in matching_question['answers'] if ans['text'] == user_answer),
                        None
                    )
                    if chosen_ans:
                        for r_link in chosen_ans.get('pageIds', []):
                            tally[r_link] = tally.get(r_link, 0) + 1

        if tally:
            sorted_tally = sorted(tally.items(), key=lambda x: x[1], reverse=True)
            best_r_key, highest_count = sorted_tally[0]
            submission.chosen_redirection = best_r_key
            submission.save()
            chosen_url = page_links.get(best_r_key, '#')
        else:
            submission.chosen_redirection = None
            submission.save()
            chosen_url = None

        return render(request, 'survey_app/thank_you.html', {
            'chosen_r_link': submission.chosen_redirection,
            'chosen_url': chosen_url,
            'submitted_time': submitted_time,
        })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'survey_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    submissions = SurveySubmission.objects.all().order_by('-submitted_time')
    page_links = load_page_links()  # Load the pageLinks.json file
    current_time = now()

    data = []
    for submission in submissions:
        answers = SurveyAnswer.objects.filter(submission=submission).order_by('question_id')
        redirection_key = submission.chosen_redirection
        redirection_url = page_links.get(redirection_key, "None")  # Resolve the URL from the key

        # Fetch top 5 links for the submission
        tally = {}
        for answer in answers:
            matching_question = next(
                (q for q in load_survey_definition()['questions'] if q['id'] == answer.question_id),
                None
            )
            if matching_question and matching_question.get('type') == 'multiple-choice':
                chosen_ans = next(
                    (ans for ans in matching_question['answers'] if ans['text'] == answer.answer_text),
                    None
                )
                if chosen_ans:
                    for r_link in chosen_ans.get('pageIds', []):
                        tally[r_link] = tally.get(r_link, 0) + 1

        sorted_tally = sorted(tally.items(), key=lambda x: x[1], reverse=True)[:5]
        top_links = [
            {
                'rank': i + 1,
                'name': page_links.get(r_key, 'Unknown'),
                'url': page_links.get(r_key, '#'),
                'tally': count
            }
            for i, (r_key, count) in enumerate(sorted_tally)
        ]

        data.append({
            'id': submission.id,
            'submitted_time': submission.submitted_time,
            'chosen_redirection_key': redirection_key,  # Include the key (e.g., "R1")
            'chosen_redirection_url': redirection_url,  # Include the resolved URL
            'top_links': top_links,  # Include the top 5 links
            'answers': [
                {
                    'question_id': answer.question_id,
                    'answer_text': answer.answer_text
                }
                for answer in answers
            ]
        })

    return render(request, 'survey_app/dashboard.html', {
        'submissions': data,
        'current_time': current_time,
    })

def thank_you_view(request):
    return render(request, 'survey_app/thank_you.html')

@login_required
def download_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="survey_submissions.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(['Submission ID', 'Submitted Time', 'Question ID', 'Answer Text', 'Redirection'])

    # Fetch all submissions and their answers
    submissions = SurveySubmission.objects.all()
    for submission in submissions:
        answers = SurveyAnswer.objects.filter(submission=submission)
        for answer in answers:
            writer.writerow([
                submission.id,
                submission.submitted_time,
                answer.question_id,
                answer.answer_text,
                submission.chosen_redirection or "None"
            ])

    return response

def home(request):
    return render(request, 'survey_app/index.html')

@csrf_protect
def modal_survey_submit(request):
    if request.method == 'POST':
        try:
            # Load the survey definition and page links
            survey_data = load_survey_definition()
            page_links = load_page_links()  # Load the updated JSON file

            all_question_ids = [q['id'] for q in survey_data['questions']]
            open_ended_ids = [q['id'] for q in survey_data['openEndedQuestions']]
            all_ids = all_question_ids + open_ended_ids

            # Check if the form has answers
            has_answers = any(q_id in request.POST for q_id in all_ids)
            if not has_answers:
                return JsonResponse({'success': False, 'message': 'Please answer at least one question before submitting.'})

            # Save the user's responses
            submitted_time = now()
            submission = SurveySubmission.objects.create(submitted_time=submitted_time)
            tally = {}

            for q_id in all_ids:
                if q_id in request.POST:
                    user_answer = request.POST[q_id]
                    SurveyAnswer.objects.create(
                        submission=submission,
                        question_id=q_id,
                        answer_text=user_answer
                    )
                    matching_question = next(
                        (question for question in survey_data['questions'] if question['id'] == q_id),
                        None
                    )
                    if matching_question and matching_question.get('type') == 'multiple-choice':
                        chosen_ans = next(
                            (ans for ans in matching_question['answers'] if ans['text'] == user_answer),
                            None
                        )
                        if chosen_ans:
                            for r_key in chosen_ans.get('pageIds', []):
                                tally[r_key] = tally.get(r_key, 0) + 1

            # Determine the top 5 links
            top_links = []
            if tally:
                sorted_tally = sorted(tally.items(), key=lambda x: x[1], reverse=True)[:5]
                for i, (r_key, count) in enumerate(sorted_tally):
                    # Fetch data from the updated pageLinks.json
                    resource = page_links.get(r_key, {})
                    top_links.append({
                        'rank': i + 1,
                        'title': resource.get('title', 'Unknown Title'),
                        'description': resource.get('description', 'No description available.'),
                        'url': resource.get('url', '#')
                    })

            # Return a JSON response with the top 5 links
            return JsonResponse({
                'success': True,
                'top_links': top_links  # Pass the top 5 links to the frontend
            })
        except Exception as e:
            # Log the error for debugging
            print(f"Error processing survey submission: {e}")
            return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def aboutus(request):
    return render(request, 'survey_app/aboutus.html')

def assess(request):
    return render(request, 'survey_app/assess.html')

def case2(request):
    return render(request, 'survey_app/case2.html')

def case3(request):
    return render(request, 'survey_app/case3.html')

def case4(request):
    return render(request, 'survey_app/case4.html')

def case5(request):           
    return render(request, 'survey_app/case5.html')

def casestudies(request):
    return render(request, 'survey_app/casestudies.html')

def explore(request):
    return render(request, 'survey_app/explore.html')

def fundingStrategy(request):
    return render(request, 'survey_app/fundingStrategy.html')

def implementSolution(request):
    return render(request, 'survey_app/implementSolution.html')

def index(request):
    return render(request, 'survey_app/index.html')

def methuen(request):
    return render(request, 'survey_app/methuen.html')

def selectSolution(request):
    return render(request, 'survey_app/selectSolution.html')

def stakeholder(request):
    return render(request, 'survey_app/stakeholder.html')

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_msg = data.get("message", "")
            reply = ask_llama3(user_msg)
            return JsonResponse({"reply": reply})
        except Exception as e:
            return JsonResponse({"reply": "Oops! Something went wrong."}, status=500)
    return JsonResponse({"error": "Only POST allowed."}, status=405)