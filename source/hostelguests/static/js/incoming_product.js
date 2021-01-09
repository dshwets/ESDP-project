const barcodeBtn = document.getElementById('barcode-find');
const formProduct = document.getElementById('form-product');
const finalFormBtn = document.getElementById('final-form-submit')
var finalForm = document.getElementById('form-incoming');
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
        table = `<td><input required type="text" name="title-${counter}" class="form-control w-auto" 
                                id="product-${counter}-title" value= ${response.title}></td>`;
        table += `<td><input required disabled type="text" name="barcode-${counter}" class="form-control w-auto" 
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

function makeRequestFinalForm (event) {
        event.preventDefault();

        console.log($(this).serializeArray());

        // $.ajax({
        //     // type: finalForm.attr('method'),
        //     // url: finalForm.attr('action'),
        //     data: finalForm.serializeArray(),
        //     success: function (data) {
        //         console.log('Submission was successful.');
        //         console.log(data);
        //     },
        //     error: function (data) {
        //         console.log('An error occurred.');
        //         console.log(data);
        //     },
        // });
    };

//
$('form').submit(function(event) {
    event.preventDefault();
    var data = $(this).serializeArray();
    console.log(data)
    jQuery.ajax({
        url:     url_incoming_product,
        type:     "POST",
        dataType: "html",
        data: data,  // Сеарилизуем объект
        success: function(response) { //Данные отправлены успешно
            result = jQuery.parseJSON(response);
        },
        error: function(response) { // Данные не отправлены
        }
    });
//     $.ajax({
//             type: 'Post',
//             url: url_incoming_product,
//             data: data,
//             success: function (data) {
//                 console.log('Submission was successful.');
//                 console.log(data);
//             },
//             error: function (data) {
//                 console.log('An error occurred.');
//                 console.log(data);
//             },
//         });
//     return false;
});

    // function makeRequestFinalForm (event) {
    //     event.preventDefault();
    //     console.log(finalForm.serializeArray());

        // $.ajax({
        //     // type: finalForm.attr('method'),
        //     // url: finalForm.attr('action'),
        //     data: finalForm.serializeArray(),
        //     success: function (data) {
        //         console.log('Submission was successful.');
        //         console.log(data);
        //     },
        //     error: function (data) {
        //         console.log('An error occurred.');
        //         console.log(data);
        //     },
        // });
    // };


// finalFormBtn.addEventListener('click',makeRequestFinalForm)
barcodeBtn.addEventListener('click', makeRequestBarcode)
