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
