document.addEventListener('DOMContentLoaded', () => {
    const colorItems = document.querySelectorAll('.color-item');
    const showMoreButton = document.getElementById('show-more-colors');
    const showLessButton = document.getElementById('show-less-colors');

    // İlk 5 rengi göster, diğerlerini gizle
    colorItems.forEach((element, index) => {
        if (index >= 5) {
            element.style.display = 'none';
        }
    });

    // Daha fazla butonuna tıklanınca diğer renkleri göster
    showMoreButton.addEventListener('click', () => {
        colorItems.forEach((element, index) => {
            if (index >= 5) {
                element.style.display = 'inline-block';
            }
        });
        showMoreButton.style.display = 'none';
        showLessButton.style.display = 'inline-block';
    });

    // Daha az butonuna tıklanınca fazla renkleri gizle
    showLessButton.addEventListener('click', () => {
        colorItems.forEach((element, index) => {
            if (index >= 5) {
                element.style.display = 'none';
            }
        });
        showMoreButton.style.display = 'inline-block';
        showLessButton.style.display = 'none';
    });
});


