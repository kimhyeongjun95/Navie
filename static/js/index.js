  // 최신 영화
  let slides = document.querySelector('#recent_slides');
  let slide = document.querySelectorAll('#recent_slides li');
  let currentIdx = 0;
  let slideCount = slide.length;
  let prevBtn = document.querySelector('#recent_prev');
  let nextBtn = document.querySelector('#recent_next');
  let slideWidth = 200;
  let slideMargin = 0;

  slides.style.width = (slideWidth + slideMargin) * slideCount - slideMargin + 'px';
  function moveSlide(num) {
    slides.style.left = -num * 200 +  'px';
    currentIdx = num;
  }
  nextBtn.addEventListener('click', function() {
    // slide count에서 몇개를 보여줄지를 기준으로 빼줘야한다.
    if(currentIdx < slideCount - 6){
      moveSlide(currentIdx + 1);
    } else {
      moveSlide(0);
    }
  });
  prevBtn.addEventListener('click', function() {
    if(currentIdx > 0){
      moveSlide(currentIdx - 1);
    } else {
      moveSlide(slideCount-6);
    }
  });

  // 액션 영화
  let action_slides = document.querySelector('#action_slides');
  let action_slide = document.querySelectorAll('#action_slides li');
  let action_currentIdx = 0;
  let action_slideCount = slide.length;
  let action_prevBtn = document.querySelector('#action_prev')
  let action_nextBtn = document.querySelector('#action_next')
  let action_slideWidth = 200;
  let action_slideMargin = 0;

  action_slides.style.width = (action_slideWidth + action_slideMargin) * action_slideCount - action_slideMargin + 'px';
  function action_moveSlide(num) {
    action_slides.style.left = -num * 200 +  'px';
    action_currentIdx = num;
  }
  action_nextBtn.addEventListener('click', function() {
    // slide count에서 몇개를 보여줄지를 기준으로 빼줘야한다.
    if(action_currentIdx < action_slideCount - 6){
      action_moveSlide(action_currentIdx + 1);
    } else {
      action_moveSlide(0);
    }
  });
  action_prevBtn.addEventListener('click', function() {
    if(action_currentIdx > 0){
      action_moveSlide(action_currentIdx - 1);
    } else {
      action_moveSlide(action_slideCount-6);
    }
  });

// 로맨스 영화
let romance_slides = document.querySelector('#romance_slides');
let romance_slide = document.querySelectorAll('#romance_slides li');
let romance_currentIdx = 0;
let romance_slideCount = slide.length;
let romance_prevBtn = document.querySelector('#romance_prev')
let romance_nextBtn = document.querySelector('#romance_next')
let romance_slideWidth = 200;
let romance_slideMargin = 0;

romance_slides.style.width = (romance_slideWidth + romance_slideMargin) * romance_slideCount - romance_slideMargin + 'px';
function romance_moveSlide(num) {
romance_slides.style.left = -num * 200 +  'px';
romance_currentIdx = num;
}
romance_nextBtn.addEventListener('click', function() {
// slide count에서 몇개를 보여줄지를 기준으로 빼줘야한다.
if(romance_currentIdx < romance_slideCount - 6){
  romance_moveSlide(romance_currentIdx + 1);
} else {
  romance_moveSlide(0);
}
});
romance_prevBtn.addEventListener('click', function() {
if(romance_currentIdx > 0){
  romance_moveSlide(romance_currentIdx - 1);
} else {
  romance_moveSlide(romance_slideCount-6);
}
});

// 범죄영화
let crime_slides = document.querySelector('#crime_slides');
let crime_slide = document.querySelectorAll('#crime_slides li');
let crime_currentIdx = 0;
let crime_slideCount = slide.length;
let crime_prevBtn = document.querySelector('#crime_prev')
let crime_nextBtn = document.querySelector('#crime_next')
let crime_slideWidth = 200;
let crime_slideMargin = 0;

crime_slides.style.width = (crime_slideWidth + crime_slideMargin) * crime_slideCount - crime_slideMargin + 'px';
function crime_moveSlide(num) {
  crime_slides.style.left = -num * 200 +  'px';
  crime_currentIdx = num;
}
crime_nextBtn.addEventListener('click', function() {
  // slide count에서 몇개를 보여줄지를 기준으로 빼줘야한다.
  if(crime_currentIdx < crime_slideCount - 6){
    crime_moveSlide(crime_currentIdx + 1);
  } else {
    crime_moveSlide(0);
  }
});
crime_prevBtn.addEventListener('click', function() {
  if(crime_currentIdx > 0){
    crime_moveSlide(crime_currentIdx - 1);
  } else {
    crime_moveSlide(crime_slideCount-6);
  }
});

// 공포 영화
let horror_slides = document.querySelector('#horror_slides');
let horror_slide = document.querySelectorAll('#horror_slides li');
let horror_currentIdx = 0;
let horror_slideCount = slide.length;
let horror_prevBtn = document.querySelector('#horror_prev')
let horror_nextBtn = document.querySelector('#horror_next')
let horror_slideWidth = 200;
let horror_slideMargin = 0;

horror_slides.style.width = (horror_slideWidth + horror_slideMargin) * horror_slideCount - horror_slideMargin + 'px';
function horror_moveSlide(num) {
  horror_slides.style.left = -num * 200 +  'px';
  horror_currentIdx = num;
}
horror_nextBtn.addEventListener('click', function() {
  // slide count에서 몇개를 보여줄지를 기준으로 빼줘야한다.
  if(horror_currentIdx < horror_slideCount - 6){
    horror_moveSlide(horror_currentIdx + 1);
  } else {
    horror_moveSlide(0);
  }
});
horror_prevBtn.addEventListener('click', function() {
  if(horror_currentIdx > 0){
    horror_moveSlide(horror_currentIdx - 1);
  } else {
    horror_moveSlide(horror_slideCount-6);
  }
});

let comedy_slides = document.querySelector('#comedy_slides');
let comedy_slide = document.querySelectorAll('#comedy_slides li');
let comedy_currentIdx = 0;
let comedy_slideCount = slide.length;
let comedy_prevBtn = document.querySelector('#comedy_prev')
let comedy_nextBtn = document.querySelector('#comedy_next')
let comedy_slideWidth = 200;
let comedy_slideMargin = 0;

comedy_slides.style.width = (comedy_slideWidth + comedy_slideMargin) * comedy_slideCount - comedy_slideMargin + 'px';
function comedy_moveSlide(num) {
  comedy_slides.style.left = -num * 200 +  'px';
  comedy_currentIdx = num;
}
comedy_nextBtn.addEventListener('click', function() {
  // slide count에서 몇개를 보여줄지를 기준으로 빼줘야한다.
  if(comedy_currentIdx < comedy_slideCount - 6){
    comedy_moveSlide(comedy_currentIdx + 1);
  } else {
    comedy_moveSlide(0);
  }
});
comedy_prevBtn.addEventListener('click', function() {
  if(comedy_currentIdx > 0){
    comedy_moveSlide(comedy_currentIdx - 1);
  } else {
    comedy_moveSlide(comedy_slideCount-6);
  }
});