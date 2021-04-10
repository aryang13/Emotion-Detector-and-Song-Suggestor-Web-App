'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
const errorMsgElement = document.getElementById('errorMsgElement');

const constraints = {
    audio: false,
    video: {
        width: 300, height: 300
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
    context.drawImage(video, 0, 0, 150, 150);
    var myImage = canvas.toDataURL("image/png");
    // document.getElementById('hidden_form').value = myImage;
    console.log(myImage);
    $.ajax({
        type: 'get',
        url: 'my_image/',
        data: {
            "taken_image": myImage,
        },
        dataType: "json",
        success: function (data) {
            // any process in data
            console.log("successfull")
        },
        failure: function () {
            console.log("failure");
        }
    });
});