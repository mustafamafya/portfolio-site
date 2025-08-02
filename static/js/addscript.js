
  const adContainer = document.getElementById('ad-container');
  const adItems = Array.from(document.querySelectorAll('.ad-item'));

  let cloneCount = 0;

  adContainer.addEventListener('scroll', () => {
    const scrollBottom = adContainer.scrollTop + adContainer.clientHeight;
    const containerHeight = adContainer.scrollHeight;

    if (scrollBottom >= containerHeight - 10) {
      // Clone ads and append to container
      adItems.forEach(item => {
        const clone = item.cloneNode(true);
        adContainer.appendChild(clone);
      });
      cloneCount++;
    }
  });
