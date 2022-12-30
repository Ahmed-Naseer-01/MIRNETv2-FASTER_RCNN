var fr; // Variable to store the file reader
var is_img_ready = false;

//Function to load the image from local path to img and canvas
function loadImage() {
    img_src = document.getElementById('img_src');
    if(!img_src.files[0]) {
        alert('Please select an Image first!')
        return;
    }
    fr = new FileReader();
    fr.onload = updateImage;
    fr.readAsDataURL(img_src.files[0])
}

function updateImage() {
    img = new Image();
    img.onload = function() {
        var canvas = document.getElementById("local_canvas")
        canvas.width = img.width;
        canvas.height = img.height;
        var ctx = canvas.getContext("2d");
        ctx.drawImage(img,0,0);
    };
    img.src = fr.result;
    is_img_ready = true;
}

function loadProcessedImage(data) {
    img = new Image();
    img.onload = function() {
        var processedCanvas = document.getElementById('processed_canvas');
        var localCanvas = document.getElementById('local_canvas');
        processedCanvas.width = localCanvas.width;
        processedCanvas.height = localCanvas.height;
        ctx = processedCanvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
    };
//    console.log(data.slice(0, 100));
//    console.log(data.slice(data.length - 100, data.length));
    img.src = data;
//    img.src = 'data:image/jpeg;base64,' + data;
}

function processImage() {
    let TAG = '[processImage]';
    console.log(TAG, '[starts]');
    if (is_img_ready == false) {
        alert('No image to process!');
        return;
    }
    //Send the image to the server and wait for a response
    canvas = document.getElementById('local_canvas');
    image_data = canvas.toDataURL('image/jpeg');
    img_op = document.getElementById('image_op');
    op = img_op.options[img_op.selectedIndex].value;
//    console.log(TAG, 'image_data -> ');
//    console.log(image_data.slice(0, 100));
//    console.log(image_data.slice(image_data.length - 100, image_data.length));
    $.ajax({
        url:"http://172.30.75.24:5000/process_image",
        method: "POST",
        contentType: 'application/json',
        crossDomain: true,
        data: JSON.stringify({
            image_data: image_data,
            msg: 'This is image data',
            operation: op
        }),
        success: function(data){
//            console.log(TAG + '[ajax][success]');
//            console.log(data);
            loadProcessedImage(data['image_data']);
        },
        error: function(err) {
            console.log(err)
        }
    });
}

