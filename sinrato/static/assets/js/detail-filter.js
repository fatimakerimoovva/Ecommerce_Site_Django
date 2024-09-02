const color_detail = document.querySelectorAll('.color-filter-detail');

color_detail.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/products/${element.getAttribute('data-product')}/versions/${element.getAttribute('data-version')}/`;
        url += `?color=${element.getAttribute('id')}`;
        
        fetch(url)
        .then(response => response.json())
        .then(data => {
            const detailColorElement = document.getElementById('detail_color');
            detailColorElement.innerHTML = `
                <div class="col-lg-5" style="d-flex">
                    <div class="product-large-slider mb-20">
                        <div class="pro-large-img" style="width: 500px;">
                            <img id="product-cover-image" alt="" src="${data['cover_image']}" class="simpleLens-big-image custom-image-width">
                        </div>
                    </div>
                    <div class="d-flex">
                    ${data.image.map(element => `
                        <li><a data-bs-toggle="tab" href="${element.image}"><img style="height:100px;" alt="" src="${element.image}"></a>
                    `).join('')}
                    </div>
                </div>`;
            getBasket()
            getWishList()
        });
    });
});
