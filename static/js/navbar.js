const toggle = document.querySelector('.navbar_profile');
console.log(toggle)
// const menu = document.querySelector('.navbar_menu');
const logout = document.querySelector('.navbar_logout');

// 햄버거 눌러서
toggle.addEventListener('click', () => {
  // menu.classList.toggle('active');
  console.log(1)
  logout.classList.toggle('active');
});