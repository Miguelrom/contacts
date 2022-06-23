const navigation = document.getElementById('navigation');

const contactsLink = document.getElementById('contacts');
const contactCreateLink = document.getElementById('contact-create');
const aboutLink = document.getElementById('about');

window.addEventListener('load', function(e) {
  const currentActive = navigation.getElementsByClassName('active-tab');

  if (currentActive.length !== 0){
    currentActive[0].classList.toggle('active-tab');
  }

  if (window.location.pathname === contactsLink.pathname){
    contactsLink.classList.toggle('active-tab');
  } else if (window.location.pathname === contactCreateLink.pathname) {
    contactCreateLink.classList.toggle('active-tab');
  } else if (window.location.pathname === aboutLink.pathname) {
    aboutLink.classList.toggle('active-tab');
  }

});


