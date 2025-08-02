document.addEventListener('DOMContentLoaded', function () {
  const fileInputs = document.querySelectorAll('input[type="file"]');

  fileInputs.forEach(input => {
    input.addEventListener('change', function () {
      const preview = input.closest('.inline-related').querySelector('.field-image img');

      if (preview && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function (e) {
          preview.src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
      }
    });
  });
});