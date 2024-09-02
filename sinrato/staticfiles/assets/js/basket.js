function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



function getWishlist() {
    const wishlists = document.querySelectorAll('.wishlist');
    
    
    wishlists.forEach((element) => {
        
        element.addEventListener('click', (event) => {
           
            const product_id = event.target.dataset.id
            console.log(product_id);
            
            
            return fetch(`${location.origin}/api/wishlist/`, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': product_id,
                })
            })
            .then((response) => response.json()).then((data) => {
                   console.log(data);
                   
            })
        })
    })
}
getWishlist()

function getRemovewishlist() {
    const removewishlist = document.querySelectorAll('.th-delete');
    removewishlist.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/wishlist/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
                .then((response) => {
                    if (response.status === 200) {
                        console.log(response.status);
                        fetch(`${location.origin}/api/wishlist/`).then(response => response.json()).then(data => {
                            document.getElementById("wishlist-products").innerHTML = ''
                            data['product'].forEach((element) => {
                                document.getElementById('wishlist-products').innerHTML +=`
                                     <tr>
                                <td class = 'th-delete' class="sop-icon"  data-id="${element['id']}" style="cursor: pointer;">
                                    <i class="fa fa-times"></i>
                                </td>
                                <td class="sop-cart">
                                    <a href="${element['detail_url']}"><img width="150px" class="primary-image" alt="" src="${element['cover_image']}"></a>
                                </td>
                                <td class="sop-cart"><a href="${element['detail_url']}">${element['product']['title']}  ${element['color']['name']}</a></td>
                                <td class="sop-cart">${element['product']['price']}$</td>
                                <td><input class="input-text qty" type="text" name="qty" maxlength="12" value="1" title="Qty"></td>
                                <td data-id="${element['id']}"><button class="button2  notice elit" title="" type="button">
                                    Add to cart
                                    </button>
                                </td>
                            </tr>
                                `;
                            })
                            getRemovewishlist()
                        })

                    }
                })
        })
    })
}

getRemovewishlist()

function getBasket() {
    const baskets = document.querySelectorAll('.basket')
    baskets.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/basket/`, {
                method: 'POST',
                headers: {
                    'content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                    'quantity': 1,
                })
            })
                .then((response) => {
                    console.log(response);
                    if (response.status === 201) {
                        alert('Added to Basket!');
                    }
                })
        })
    })
}
getBasket()

function getRemoveBasketItem() {
    const removeBasketItems = document.querySelectorAll('.th-basket-delete');
    removeBasketItems.forEach((element) => {
        element.addEventListener('click', () => {
            return fetch(`${location.origin}/api/basket/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({
                    'product': element.dataset.id,
                })
            })
                .then((response) => {
                    if (response.status === 200) {
                        console.log(response.status);
                        fetch(`${location.origin}/api/basket/`).then(response => response.json()).then(data => {
                            document.getElementById("shopping_basket").innerHTML = ''
                            data['items'].forEach((element) => {
                                document.getElementById('shopping_basket').innerHTML += `
                                    <tr>
                                        <td class="sop-icon th-basket-delete" style="cursor: pointer;" data-id = '${element['id']}'>
                                            <i data-id = "${element['id']}" class="fa fa-times"></i>
                                        </td>
                                        <td>
                                            <a href="${element['detail_url']}"><img src="${element['cover_image']}" alt="Cart Image" title="Compete Track Tote" class="img-thumbnail"></a>
                                        </td>
                                        <td>
                                            <a href="${element['detail_url']}">${element['product']['title']}</a>
                                        </td>
                                        <td>
                                            <div class="input-group btn-block">
                                                <div class="product-qty me-3">
                                                    <input type="text" value="${element['quantity']}">
                                                </div>
                                            </div>
                                        </td>
                                        <td>${element['product']['price'] }/td>
                                            <td>${element['subtotal']}</td>
                                        </tr>
                                `})
                                getRemoveBasketItem()
                            })
    
                        }
                    })
            })
        })
    }
    
    getRemoveBasketItem()