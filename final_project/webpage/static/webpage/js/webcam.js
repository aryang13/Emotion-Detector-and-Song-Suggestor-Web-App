'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
const errorMsgElement = document.getElementById('errorMsgElement');

const constraints = {
    audio: false,
    video: {
        width: 400, height: 400
    },
};

//access webcam
async function init() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
    } catch(e) {
        errorMsgElement.innerHTML = `navigator.getUserMedia.error:${e.toString()}`;
    }
}

//success 
function handleSuccess(stream) {
    window.stream = stream;
    video.srcObject = stream;
}

//init function
init();

var context = canvas.getContext('2d');
snap.addEventListener("click", function(){
    context.drawImage(video, 0, 0, 224, 224);
    var myImage = canvas.toDataURL("image/png");
    document.getElementById('imageData').value = myImage;
    // $.ajax({
    //     type: 'get',
    //     url: 'my_image/',
    //     data: {
    //         "taken_image": myImage,
    //     },
    //     dataType: "json",
    //     success: function (data) {
    //         // any process in data
    //         console.log("successful")
    //     },
    //     failure: function () {
    //         console.log("failure");
    //     }
    // });
});
