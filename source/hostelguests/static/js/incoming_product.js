const barcodeBtn = document.getElementById('barcode-find');
const formProduct = document.getElementById('form-product');
var counter = 0


async function makeRequestBarcode(event) {
    event.preventDefault();
    try {
        var barcode = document.getElementById('barcode-find-value').value;
        var url = url_barcode.replace('123', barcode);
        let response = await fetch(url).then(response => {
            return response.json();
        });
        var table;
        counter +=1
        table = `<td><input type="text" class="form-control w-auto" 
                                id="product-${counter}-title" value= ${response.title}></td>`;
        table += `<td><input type="text" class="form-control w-auto" 
            id="product-${counter}-barcode" value= ${response.barcode}></td>`;
        table += `<td><input type="number" class="form-control w-auto"
            id="product-${counter}-qty"></td>`;
        table += `<td><input type="number" required name="product-purchase-price" 
            min="0" value="0" step=".10" class="form-control w-auto" id="product-${counter}-purchase-price value= ${response.purchase_price}"></td>`;
        formProduct.insertAdjacentHTML('afterend', table);
    } catch (e) {
        e = await e.response.json();
        response = await e;
    }
}

barcodeBtn.addEventListener('click', makeRequestBarcode)
