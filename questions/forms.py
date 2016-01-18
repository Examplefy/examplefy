from django import forms
from questions.models import Question
errors = {
    'required': "Please fills required forms.",
    'invalid': "Invalid form entry. Please try again."
}

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_title', 'question_text')
        labels = {
            'question_title': 'Subject',
            'question_text': 'Question'
        }
        error_messages = {
            'question_title': errors,
            'question_text': errors
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(QuestionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        instance.author = self.author
        if commit:
            instance.save()