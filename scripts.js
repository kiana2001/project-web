let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-container');
let formclose = document.querySelector('#form-close');



window.onscroll = ( ) =>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
}
searchBtn.addEventListener('click', () =>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active'); 
});
formBtn.addEventListener('click', () =>{
  
    loginForm.classList.add('active'); 
});

formclose.addEventListener('click', () =>{
  
    loginForm.classList.remove('active'); 
});
