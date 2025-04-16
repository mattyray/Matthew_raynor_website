from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review here...'
            }),
        }

    rating = forms.ChoiceField(
        label='Rating',
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(5, 0, -1)],
        widget=forms.RadioSelect(attrs={'class': 'star-rating'}),
        initial=5
    )
