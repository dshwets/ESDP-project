const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');
const snapSoundElement = document.getElementById('snapSound');
const webcam = new Webcam(webcamElement, 'user', canvasElement, snapSoundElement);
const photo_btn = document.getElementById('make_photo')

webcam.start()
  .then(result =>{
    console.log("webcam started");
  })
  .catch(err => {
    console.log(err);
});

let picture = webcam.snap();
document.querySelector('#id_photo').href = picture;

    $('#cameraFlip').click(function() {
      webcam.flip();
      webcam.start();
    });

// function b64toBlob(b64Data, contentType, sliceSize) {
//         contentType = contentType || '';
//         sliceSize = sliceSize || 512;
//         let byteCharacters = atob(b64Data);
//         let byteArrays = [];
//         for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
//             let slice = byteCharacters.slice(offset, offset + sliceSize);
//             let byteNumbers = new Array(slice.length);
//             for (let i = 0; i < slice.length; i++) {
//                 byteNumbers[i] = slice.charCodeAt(i);
//             }
//             let byteArray = new Uint8Array(byteNumbers);
//             byteArrays.push(byteArray);
//         }
//       let blob = new Blob(byteArrays, {type: contentType});
//       return blob;
// }

// async function appendFileAndSubmit(photo){
//     let form = document.getElementsByTagName('form')[0];
//     let ImageURL = photo;
//     let block = ImageURL.split(";");
//     let contentType = block[0].split(":")[1];// In this case "image/gif"
//     let realData = block[1].split(",")[1];// In this case "iVBORw0KGg...."
//     let blob = b64toBlob(realData, contentType);
//     let fd = new FormData(form);
//     fd.append("image", blob);
// }

function save_photo(event){
    event.preventDefault();
    let photo_data = webcam.snap()
    let hidden_input = document.getElementById('id_hidden_base64')
    hidden_input.value = webcam.snap()
}


window.addEventListener('load', function() {
    photo_btn.onclick = save_photo;
    console.log('1111')
});
