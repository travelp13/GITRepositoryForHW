from django.shortcuts import render
from django.http import HttpRequest, Http404
import requests
# Create your views here.

def main(request: HttpRequest):
    categories = [
        "music", "sport_and_leisure", "film_and_tv", "arts_and_literature",
        "history", "society_and_culture", "science", "geography",
        "food_and_drink", "general_knowledge"
    ]
    return render(request, 'trivia_app/index.html', {'categories': categories})

def category_question(request: HttpRequest, category: str):
    url = f"https://the-trivia-api.com/v2/questions?limit=1&categories={category}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Http404("Category not found")

    data = response.json()
    if not data:
        raise Http404("Question not found")

    question_data = data[0]
    question_text = question_data['question']['text']
    answers = question_data['incorrectAnswers'] + [question_data['correctAnswer']]
    context = {
        'category': category.replace('_', ' ').title(),
        'question_text': question_text,
        'answers': sorted(answers),
    }
    return render(request, 'trivia_app/question.html', context)
