from django import forms
from reviews.models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        max_length=20,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'review-title input_area',
            'placeholder': '제목을 입력해주세요.',
            'autofocus': True,
            })
    )

    content = forms.CharField(
        label='',
        min_length=1,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'review-content input_area',
            'placeholder': '본문을 입력해주세요.',
            })
    )

    rate = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'review-rate input_area',
            'placeholder': '0',
        })
    )

    class Meta:
        model = Review
        fields = ('title', 'content', 'rate',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        min_length=1,
        widget=forms.TextInput(attrs={
            'class': 'review-comment input_area',
            'placeholder': '200자 이하의 댓글을 입력해주세요.'
            })
    )

    class Meta:
        model = Comment
        fields = ('content',)