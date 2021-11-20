from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from movies.models import Movie
from .forms import ReviewForm


# Create your views here.
@login_required
@require_http_methods(['GET', 'POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('reviews:detail_review', review.pk)
    else:
        review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form,
    }
    return render(request, 'reviews/create_review.html', context)



@require_safe
def detail_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail_review.html', context)



@login_required
@require_http_methods(['GET', 'POST'])
def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        review_update_form = ReviewForm(request.POST, instance=review)
        if review_update_form.is_valid():
            review.save()
            return redirect('reviews:detail_review', review.pk)
    else:
        review_update_form = ReviewForm(instance=review)
    context = {
        'review': review,
        'review_update_form': review_update_form,
    }
    return render(request, 'reviews/update_review.html', context)


@require_POST
def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail_movie', review.movie.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def create_comment(request, review_pk):
    pass


@require_POST
def delete_comment(request, review_pk, comment_pk):
    pass