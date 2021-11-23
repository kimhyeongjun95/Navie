let myLike = document.querySelector('.my_like');
let myReview = document.querySelector('.my_review');
let lifeMovie = document.querySelector('.recommended');

let button1 = document.querySelector('#button1');
let button2 = document.querySelector('#button2');
let button3 = document.querySelector('#button3');

button1.addEventListener('click', () => {
  if (!myLike.classList.contains('active')) {
    myLike.classList.toggle('active');
    if (myReview.classList.contains('active')) {
      myReview.classList.toggle('active');
    } else if (lifeMovie.classList.contains('active')) {
      lifeMovie.classList.toggle('active')
    }
  }
});

button2.addEventListener('click', () => {
  if (!myReview.classList.contains('active')) {
    myReview.classList.toggle('active');
    if (myLike.classList.contains('active')) {
      myLike.classList.toggle('active');
    } else if (lifeMovie.classList.contains('active')) {
      lifeMovie.classList.toggle('active')
    }
  }
});

button3.addEventListener('click', () => {
  if (!lifeMovie.classList.contains('active')) {
    lifeMovie.classList.toggle('active');
    if (myLike.classList.contains('active')) {
      myLike.classList.toggle('active');
    } else if (myReview.classList.contains('active')) {
      myReview.classList.toggle('active')
    }
  }
});