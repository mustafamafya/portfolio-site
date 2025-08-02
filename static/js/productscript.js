// static/js/productscript.js
  const mainImage = document.getElementById('main-image');
  const thumbnails = document.querySelectorAll('.thumb-img');

  thumbnails.forEach(thumb => {
    thumb.addEventListener('click', () => {
      mainImage.src = thumb.src;
    });
  });
