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
        var barcode = document.getElementById('barcode-find-value').value;
        var url = url_barcode.replace('123', barcode);
        let response = await fetch(url).then(response => {
            return response.json();
        });
        var table;
        counter += 1
        table = `<td><input required type="text" name="title-${counter}" class="form-control w-auto" 
                                id="product-${counter}-title" value= ${response.title}></td>`;
        table += `<td><input required readonly type="text" name="barcode-${counter}" class="form-control w-auto" 
            id="product-${counter}-barcode" value= ${response.barcode}></td>`;
        table += `<td><input required type="number" name="qty-${counter}" class="form-control w-auto"
            id="product-${counter}-qty"></td>`;
        table += `<td><input required type="number" name="purchase-price-${counter}" required name="product-purchase-price" 
            min="0" value="0" step=".10" class="form-control w-auto" id="product-${counter}-purchase-price value= ${response.purchase_price}"></td>`;
        formProduct.insertAdjacentHTML('afterend', table);
    } catch (e) {
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


barcodeBtn.addEventListener('click', makeRequestBarcode)
mainProductForm.addEventListener('submit',async function(event){
     event.preventDefault();
    let data = $(this).serializeJSON();
    let response = await makeRequest(url_incoming_product, "POST", data);
    window.open(urlRedirect);
    // console.log(response) todo надо сделать редирект на детальный просмотр incomes
});