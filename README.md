# face-authen-api
**This API is a part of the project FaceIt**

Find the repo here: https://github.com/jaya-nanden/MyCamu-Clone


# FaceIt
This project is basically an idea of improving the existing website of online mode of classes with additional features which we felt its required and could bring an impact to 
the system.

A pre-recorded video of about 10 seconds is collected from the registered users(students in this case). This is used for creating image data and storing in it in database. When an api call is made with roll number or ID with the image captured from live webcam it is used for accessing the database for respective user and face recognition is done.
Once the user is recognized, the API returns a success message and can be redirects them to any third party app eg. Microsoft Teams, Google Meet, Zoom.

### How the API works
  
   Recognition of faces can be done in 4 steps:
   
   1) Find the face in the picture
     
   2) Unwrapping the picture
     
   3) Analyse the facial structure and find unique features
     
   4) Compare the faces with the people we already knew and if matched return true
            

**Face Detection:**

  In this library, Face detection will be done by Histogram of Oriented Gradients(HOG). At first we convert the image to black and white. We take every pixel of the image and compare it with the neighbour pixel. By comparing we will be able to say how much darker or brighter the pixel is when compared to the neighbouring pixels. Then we use an arrow to represent in which direction  the image gets darker. So we will endup having large amout of gradient arrows. Hence we split the images in 16x16 squares and draw a arrow in the direction where max amount of arrow is detected in a single square. Thus we get our HOG image and then we can easily find the pattern and thereby detecting faces.

**Posing and Projecting Faces:**
   
   Now we need to unwrap the picture so that the eyes and lips are on the same place. Using face landmark estimation we will train a machine learning algorithm to find 68 points that defines the face. After finding the landmarks we can scale, shear and rotate so that eyes and mouths are concentrate at best position.

**Encoding Face:**
  
  It is done uding a deep convolutional neural network to genarate 128 measurement on each face. This is a pretrained model. Any 10 different pictures of the same person will give the same measurements.

**Finding the person's name from the encoding:**
   
   We have created a dataset of known people, stored their images on separate folders with roll number as the folder name. When a student enter the roll number, we can use that roll number to acess his/her folder which has 5 images of him/her and compare the encoded values of the test image with the 5 images and thereby we will be able to authericate the student.



https://user-images.githubusercontent.com/65902731/126609469-dab0b730-55c8-4d1b-add6-d1ce1a0d2a3a.MP4


### Website Live: https://jaya-nanden.github.io/MyCamu-Clone/

### API: https://face-authen-api.herokuapp.com/predict

# Contributors
* [Jayananden M](https://github.com/jaya-nanden)
* [Sridhar](https://github.com/Sridhar0519)
* [Ashwin Pranaav K S](https://github.com/AshwinPranaav)
