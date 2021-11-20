const toggle = document.querySelector('.navbar_profile_image');
const menu = document.querySelector('.navbar_dropdown_content');

// 햄버거 눌러서
toggle.addEventListener('click', () => {
  menu.classList.toggle('active');
});