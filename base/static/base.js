let bars = document.querySelector('.fa-bars')
let sidebar = document.querySelector('.sidebar')
let mainContent = document.querySelector('.main-content')
let openButton = document.querySelector('#open-button')
document.addEventListener('DOMContentLoaded',()=>{
    if(window.innerWidth <= '768px'){
        sidebar.style.display ='none'
        bars.style.display = 'block'
    }
    if(window.innerWidth >'768px'){
        bars.style.display ='none'
    }
},
bars.onclick = ()=>{
    
    if (sidebar.style.left === "-250px"){
    sidebar.style.left = "0px";
    
    } 
else {
sidebar.style.left = "-250px";

}})


    