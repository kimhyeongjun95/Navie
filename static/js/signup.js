let input1 = document.querySelector('.accounts-name');
let input2 = document.querySelector('.accounts-id');
let input3 = document.querySelector('.accounts-password');
let input4 = document.querySelector('.accounts-passwordconfirm');
let input5 = document.querySelector('.accounts-email');

let btn = document.querySelector('.btn');
// console.log(input2.value)

input5.addEventListener('keyup', function() {
  if (input1.value == '' && input2.value == '' && input3.value == '' &&
  input4.value == '' && input5.value == '') {
    btn.style.backgroundColor = '#999';
  } else {
    btn.style.backgroundColor = '#11f3a2';
  }
})
// input2.addEventListener('keyup', function() {
//   if (input1.value == '' && input2.value == '' && input3.value == '' &&
//   input4.value == '' && input5.value == '') {
//     btn.style.backgroundColor = '#999';
//   } else {
//     btn.style.backgroundColor = '#11f3a2';
//   }
// })
// input3.addEventListener('keyup', function() {
//   if (input1.value == '' && input2.value == '' && input3.value == '' &&
//   input4.value == null && input5.value == '') {
//     btn.style.backgroundColor = '#999';
//   } else {
//     btn.style.backgroundColor = '#11f3a2';
//   }
// })
// input4.addEventListener('keyup', function() {
//   if (input1.value == '' && input2.value == '' && input3.value == '' &&
//   input4.value == '' && input5.value == '') {
//     btn.style.backgroundColor = '#999';
//   } else {
//     btn.style.backgroundColor = '#11f3a2';
//   }
// })
// input5.addEventListener('keyup', function() {
//   if (input1.value == '' && input2.value == '' && input3.value == '' &&
//   input4.value == '' && input5.value == '') {
//     btn.style.backgroundColor = '#999';
//   } else {
//     btn.style.backgroundColor = '#11f3a2';
//   }
// })