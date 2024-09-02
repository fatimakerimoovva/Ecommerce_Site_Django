function loadProducts(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                return Promise.reject('Failed to load products');
            }
            return response.json();
        })
        .then(data => {
            const shopProductElement = document.getElementById('shop-product');
            shopProductElement.innerHTML = '';
            data.forEach(product => {
                const productVersions = product['product_version'];
                const manufacturerName = product['manufacturer'] ? product['manufacturer']['name'] : 'Unknown Manufacturer';
                
                productVersions.forEach(version => {
                    shopProductElement.innerHTML += `
                        <div class="col-lg-3 col-md-4 col-sm-6">
                            <div class="product-thumb">
                                <a href="/product-detail/${version.id}">
                                    <img src="${version['cover_image']}" style="width: 150px; height:150px;" class="pri-img" alt="">
                                </a>
                                <div class="box-label">
                                    ${product.new ? '<div class="label-product label_new"><span>new</span></div>' : ''}
                                </div>
                            </div>
                            <div class="product-caption">
                                <div class="manufacture-product">
                                    <p><a href="/product-detail/${version.id}">${manufacturerName}</a></p>
                                </div>
                                <div class="product-name">
                                    <h4><a href="/product-detail/${version.id}">${product['title']}</a></h4>
                                </div>
                                <div class="ratings">
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span><i class="lnr lnr-star"></i></span>
                                </div>
                                <div class="price-box">
                                    <p>${product.in_sale ? `<span class="old-price" style="font-size: 15px;"><del>$${product.old_price}</del></span><span style="font-size: 15px; color: red; margin-left:3px;" class="special-price">$${product.price}</span>` : `$${product.price}`}</p>
                                </div>
                                <div class="product-icon">
                                    <ul class='d-flex'>
                                        <button type="button" style="border-radius: 5px;">add to cart</button>
                                        <li class='wishlist' data-id='${product.id}'><i class="fa fa-heart" data-id='${product.id}'></i></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    `;
                });
            });
            getWishlist();
            getBasket() // Yeni ürünlere event listener eklemek için çağırılıyor
        })
        .catch(error => console.error('Error loading products:', error));
}

// Sayfa yüklendiğinde ürünleri getir
loadProducts(`${location.origin}/api/products`);

const categories = document.querySelectorAll('.category-filter');
categories.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/products`;
        url += `?category=${element.getAttribute('data-id')}`;
        loadProducts(url);
    });
});


function loadProducts(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                return Promise.reject('Failed to load products');
            }
            return response.json();
        })
        .then(data => {
            const shopProductElement = document.getElementById('shop-product');
            shopProductElement.innerHTML = '';
            data.forEach(product => {
                const productVersions = product['product_version'];
                const manufacturerName = product['manufacturer'] ? product['manufacturer']['name'] : 'Unknown Manufacturer';
                
                productVersions.forEach(version => {
                    shopProductElement.innerHTML += `
                        <div class="col-lg-3 col-md-4 col-sm-6">
                            <div class="product-thumb">
                                <a href="/product-detail/${version.id}">
                                    <img src="${version['cover_image']}" style="width: 150px; height:150px;" class="pri-img" alt="">
                                </a>
                                <div class="box-label">
                                    ${product.new ? '<div class="label-product label_new"><span>new</span></div>' : ''}
                                </div>
                            </div>
                            <div class="product-caption">
                                <div class="manufacture-product">
                                    <p><a href="/product-detail/${version.id}">${manufacturerName}</a></p>
                                </div>
                                <div class="product-name">
                                    <h4><a href="/product-detail/${version.id}">${product['title']}</a></h4>
                                </div>
                                <div class="ratings">
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span class="yellow"><i class="lnr lnr-star"></i></span>
                                    <span><i class="lnr lnr-star"></i></span>
                                </div>
                                <div class="price-box">
                                    <p>${product.in_sale ? `<span class="old-price" style="font-size: 15px;"><del>$${product.old_price}</del></span><span style="font-size: 15px; color: red; margin-left:3px;" class="special-price">$${product.price}</span>` : `$${product.price}`}</p>
                                </div>
                                <div class="product-icon">
                                    <ul class='d-flex'>
                                        <button type="button" style="border-radius: 5px;">add to cart</button>
                                        <li class='wishlist' data-id='${product.id}'><i class="fa fa-heart" data-id='${product.id}' ></i></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    `;
                });
            });
            getWishlist();
            getBasket() // Yeni ürünlere event listener eklemek için çağırılıyor
        })
        .catch(error => console.error('Error loading products:', error));
}

// Sayfa yüklendiğinde ürünleri getir
loadProducts(`${location.origin}/api/products`);

const manufacturers = document.querySelectorAll('.active');
manufacturers.forEach((element) => {
    element.addEventListener('click', () => {
        let url = `${location.origin}/api/products`;
        url += `?manufacturer=${element.getAttribute('data-id')}`;
        loadProducts(url);
    });
});


    
    

        const color = document.querySelectorAll('.color-filter');
        color.forEach((element) => {
            element.addEventListener('click', () => {
                let url = `${location.origin}/api/product_color/`;
                url += `?color=${element.getAttribute('data-id')}`;
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('shop-product').innerHTML =''
                        for(let i in data){
                        document.getElementById('shop-product').innerHTML += `
                        
                                <div class="col-lg-3 col-md-4 col-sm-6">
                                    <div class="product-thumb">
                                        <a href="">
                                            <img src="${data[i]['cover_image']}" style="width: 150px; height:150px;" class="pri-img" alt="">
                                        </a>
                                    </div>
                                    <div class="product-caption">
                                        <div class="manufacture-product">
                                            <p><a href="">${data[i]['product']['manufacturer']['name']}</a></p>
                                        </div>
                                        <div class="product-name">
                                            <h4><a href="">${data[i]["product"]['title']}</a></h4>
                                        </div>
                                        <div class="ratings">
                                            <span class="yellow"><i class="lnr lnr-star"></i></span>
                                            <span class="yellow"><i class="lnr lnr-star"></i></span>
                                            <span class="yellow"><i class="lnr lnr-star"></i></span>
                                            <span class="yellow"><i class="lnr lnr-star"></i></span>
                                            <span><i class="lnr lnr-star"></i></span>
                                        </div>
                                        <div class="price-box">
                                            <p>${data[i]['product']['in_sale'] ? `<span class="old-price" style="font-size: 15px;"><del>$${data[i]["product"]['old_price']}</del></span><span style="font-size: 15px; color: red; margin-left:3px;" class="special-price">$${data[i]["product"]['price']}</span>` : `$${data[i]["product"]["price"]}`}</p>
                                        </div>
                                        <div class="product-icon">
                                            <ul class='d-flex'>
                                                <button type="button" style="border-radius: 5px;">add to cart</button>
                                                <li class='wishlist' data-id='${data[i]['id']}'><i class="fa fa-heart" data-id='${data[i]['id']}' ></i></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            `;
                        }
                            getWishlist();
                            getBasket()
                        });
                    });
            });




        

