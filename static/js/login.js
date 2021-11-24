let input1 = document.querySelector('.id');
let input2 = document.querySelector('.pw');
let btn = document.querySelector('.btn');

input1.addEventListener('keyup', function() {
  if (input1.value == '' || input2.value == '') {
    btn.style.backgroundColor = '#999';
  } else {
    btn.style.backgroundColor = '#11f3a2';
  }
});
input2.addEventListener('keyup', function() {
  if (input1.value == '' || input2.value == '') {
    btn.style.backgroundColor = '#999';
  } else {
    btn.style.backgroundColor = '#11f3a2';
  }
});