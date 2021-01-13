const barcodeBtn = document.getElementById('barcode-find');
const formProduct = document.getElementById('form-product');
const mainProductForm = document.getElementById('form-incoming')

let counter = 0


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequestBarcode(event) {
    event.preventDefault();
    try {
        counter += 1

        let barcode = document.getElementById('barcode-find-value').value;
        let url = url_barcode.replace('123', barcode);
        let response = await fetch(url).then(response => {
            return response.json();
        });
        let table;
        table = `<td><input required type="text" name="title-${counter}" class="form-control w-auto" 
                                id="product-${counter}-title" value= ${response.title}></td>`;
        table += `<td><input required readonly type="text" name="barcode-${counter}" class="form-control w-auto" 
            id="product-${counter}-barcode" value= ${response.barcode}></td>`;
        table += `<td><input required type="number" name="qty-${counter}" class="form-control w-auto"
            id="product-${counter}-qty"></td>`;
        table += `<td><input required type="number" name="purchase-price-${counter}" required name="product-purchase-price" 
            min="0" step=".10" class="form-control w-auto" id="product-${counter}-purchase-price" value= ${response.purchase_price}></td>`;
        table += `<td><input required disabled type="text" name="total" class="form-control w-auto" 
            id="total-${counter}" value="" ></td>`;
        table += `<td><button type="button" id="del-${counter}" class="btn btn-outline-danger">Удалить</button></td>`;
        formProduct.insertAdjacentHTML('afterend', table);
        const counterThis = counter
        document.getElementById(`product-${counter}-purchase-price`).onblur = ()=> total(counterThis);
        document.getElementById(`product-${counter}-qty`).onblur = ()=> total(counterThis);
        let delBtn = document.getElementById(`del-${counter}`)
        delBtn.addEventListener('click',function (){
            delBtn.parentElement.parentNode.remove();
        })
    }
    catch (e) {
        alert("Проверьте штрихкод");
    }
}

async function makeRequest(url, method = 'GET', data = undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

function total(con) {
    let qty = document.getElementById(`product-${con}-qty`).value;
    let price = document.getElementById(`product-${con}-purchase-price`).value;
    document.getElementById(`total-${con}`).value = qty*price;
    }



barcodeBtn.addEventListener('click', makeRequestBarcode)
mainProductForm.addEventListener('submit', async function (event) {
    event.preventDefault();
    try {
        let data = $(this).serializeJSON();
        let response = await makeRequest(url_incoming_product, "POST", data);
        window.location.href = urlRedirect.replace('123', response.success);
    } catch (e) {
        alert("Заполните все поля");
    }
});