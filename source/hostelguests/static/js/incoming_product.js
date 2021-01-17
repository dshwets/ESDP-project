const barcodeBtn = document.getElementById('barcode-find');
const formProduct = document.getElementById('form-product');
const mainProductForm = document.getElementById('form-incoming')
const allTotal = document.getElementById('tr-all-total')
const allTotalValue = document.getElementById('all-total')
let counter = 0
let barcodeList = [];

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
        let barcode = document.getElementById('barcode-find-value').value;
        let url = url_barcode.replace('123', barcode);
        let response = await fetch(url).then(response => {
            return response.json();
        });
        let check = checkBarcodeAndPushIfNotIncludeInBarcodeList(response)
        if (check === false){
            return alert("Проверьте штрихкод он уже есть в списке");
        }
        counter += 1
        let table;
        table = `<td class="col-sm-6"><input required type="text" name="title-${counter}" class="form-control w-auto" 
                                id="product-${counter}-title" value= ${response.title}></td>`;
        table += `<td class="col-sm-6"><input required readonly type="text" name="barcode-${counter}" class="form-control w-auto" 
            id="product-${counter}-barcode" value= ${response.barcode}></td>`;
        table += `<td class="col-sm-6"><input required type="number" name="qty-${counter}" class="form-control w-auto"
            id="product-${counter}-qty"></td>`;
        table += `<td class="col-sm-6"><input required type="number" name="purchase-price-${counter}" required name="product-purchase-price" 
            min="0" step=".10" class="form-control w-auto" id="product-${counter}-purchase-price" value= ${response.purchase_price}></td>`;
        table += `<td class="col-sm-6"><input required disabled type="text" name="total" class="form-control w-auto" 
            id="total-${counter}" value="" ></td>`;
        table += `<td class="col-sm-6"><button type="button" id="del-${counter}" class="btn btn-outline-danger">Удалить</button></td>`;
        allTotal.insertAdjacentHTML('beforebegin', table);
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
    allTotalValue.value = allTotalFunc()
}

function allTotalFunc(){
    let total = 0
    let i = counter;
    while (i > 0) {
        let qty = document.getElementById(`product-${i}-qty`).value;
        let price = document.getElementById(`product-${i}-purchase-price`).value;
        total += qty*price;
        i--;
    }
    return total
}

function checkBarcodeAndPushIfNotIncludeInBarcodeList(response){
    if (!barcodeList.includes(response.barcode)){
        barcodeList.push(response.barcode)
        return true
    }
    return false
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
