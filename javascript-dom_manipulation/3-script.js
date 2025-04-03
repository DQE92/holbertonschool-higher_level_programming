// Alternative 3-script.js
document.getElementById('toggle_header').onclick = () => {
    const header = document.querySelector('header');
    header.classList.toggle('red');
    header.classList.toggle('green');
  };
