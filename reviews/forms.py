from django import forms
from reviews.models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=20,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'review-title input_area',
            'autofocus': True,
            })
    )

    content = forms.CharField(
        label='내용',
        min_length=1,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'review-content input_area',
            })
    )

    # rate = forms.CharField(
    #     label='평점',
    #     required=True,
    #     widget=forms.(attrs={
    #         'class': 'review-rate input_area',
    #     })
    # )

    class Meta:
        model = Review
        fields = ('title', 'content', 'rate',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        min_length=1,
        widget=forms.TextInput(attrs={
            'class': 'review-comment input_area',
            })
    )

    class Meta:
        model = Comment
        fields = ('content',)