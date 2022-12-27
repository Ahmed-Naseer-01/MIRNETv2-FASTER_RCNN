<a href="https://colab.research.google.com/drive/1HN9Sd8UEqB1k_O8RpdRLL8ZUKcxh5LP8?usp=sharing" rel="nofollow"  target="_blank"><img src="https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg" style="max-width: 100%;"></a>

<h1><b>Multi-stage Image Restortion and Enhancement</h1>

<h2> <b>Introduction</h2>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>This project is about image restoration and enhancement in multiple stages. As image restoration is very important for deep learning as computer vision models is approximately based on images and videos, and your input images and videos are not clear so your DP model will never give you an efficient output. So, to remove this barrier, I made high performance image restoration model. Basically, there are four main stages which restore image like blur, noise, low-lightening and low-resolution. Basically, I used MIRNETv2 model for this project which help in restoration. The architecture followed in this project is given below:</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'><img width="562" src="https://www.waqaszamir.com/publication/zamir-2022-mirnetv2/featured_hu22f323d7da81118b42deb42bedc3b270_473795_720x2500_fit_q75_h2_lanczos_3.webp" alt="image" height="258"></p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>There are approximately Six datasets are used in it:</p>
<ul style="list-style-type: undefined;margin-left:0in;">
    <li>DPDD for deblurring</li>
    <li>DND and SIDD for image denoising</li>
    <li>Real SR for super resolution</li>
    <li>LOL and MIT-Adobe Five-K for image enhancement</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Main libraries used for restoration are:</p>
<ul style="list-style-type: disc;margin-left:0.25in;">
    <li>Pytorch</li>
    <li>Torchvision</li>
    <li>Matplot</li>
    <li>Numpy</li>
</ul>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.5in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>Additionally, this project will run for both images and videos. For video each frame will be restore one by one until model reach to the final frame of video.</p>
<h2> <b>FASTER-RCNN</h2>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>In addition of image restoration, I also used an object detection model named FASTER-RCNN. Which help us to detect object in the given environment. Detection model will also work for both images and videos. I used COCO dataset used in it.</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>The approach I used here is that given input first restore from MIRNETv2 and then this restore output will be given to faster-RCNN which will detect objects in restore image as well as in degraded image which asset us to analysis outputs.</p>
<h2> <b>Web Application</h2>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>I made a complete web application for this project by using flask framework. For front-end I used as usual HTML and CSS. And for the sake of responsive interaction, I also include bootstrap in it. I also used JAVA-Script for interconnection between front-end and back-end. &nbsp;</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;Note:</p>
<p style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:.25in;line-height:107%;font-size:15px;font-family:"Calibri",sans-serif;'>I explain whole code on colab notebook by adding comments on each cell that everyone can easily understand it. Same thing I used for web application. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>

