// Example: Show an alert when the brand is clicked
document.addEventListener('DOMContentLoaded', function() {
    var brand = document.querySelector('.navbar-brand');
    if (brand) {
        brand.addEventListener('click', function(e) {
            // e.preventDefault(); // Uncomment to prevent navigation
            console.log('Brand clicked!');
        });
    }
});