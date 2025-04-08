# survey_app/models.py

from django.db import models
from django.utils.timezone import now

class SurveySubmission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    chosen_redirection = models.CharField(max_length=10, blank=True, null=True)
    submitted_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"Submission {self.id} - {self.created_at}"

class SurveyAnswer(models.Model):
    submission = models.ForeignKey(SurveySubmission, on_delete=models.CASCADE, related_name='answers')
    question_id = models.CharField(max_length=10)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.submission.id}, Q:{self.question_id}, A:{self.answer_text}"