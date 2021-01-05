const barcodeBtn = document.getElementById('barcode-find');
const formProduct = document.getElementById('form-product');


async function makeRequestBarcode(event) {
    event.preventDefault();
    try {
        var barcode = document.getElementById('barcode-find-value').value;
        var url = url_barcode.replace('123', barcode);
        let response = await fetch(url).then(response => {
            return response.json();
        });
        var table;
        table = `<td><input type="text" class="form-control w-auto" 
                                id="product-id" value= ${response.title}></td>`;
        table += `<td><input type="text" class="form-control w-auto" 
            id="product-barcode" value= ${response.barcode}></td>`;
        table += `<td><input type="number" class="form-control w-auto"
            id="product-qty"></td>`;
        table += `<td><input type="number" required name="product-purchase-price" 
            min="0" value="0" step=".10" class="form-control w-auto" id="product-purchase-price value= ${response.purchase_price}"></td>`;
        formProduct.insertAdjacentHTML('afterend', table);
    } catch (e) {
        e = await e.response.json();
        response = await e;
    }
}

barcodeBtn.addEventListener('click', makeRequestBarcode)
