# Autoattendance-Cognitive

This is our final year project which a non manual attendance system using face recognition.

We have used dlib for face detection and Microsoft cognitive face api for face recognition.

We have used our own phone camera to identify the faces and for test faces we have used our laptop camera.

Steps to install and run this project in your machine:

1. The machine which we are using is windows 10 with Python 3.6 7

2. Install the required library which are dlib, opencv-python, cognitive_face, openpyxl and numpy.

3. To install the above packages execute this command 
    python -m pip install <package-name>

4. Get the cognitive face api key from here
      https://azure.microsoft.com/en-in/services/cognitive-services/face/

5. Replace with existing key and existing regional api.

6. Python Add_student.py - for adding student into db.

7. Python Create_person.py <userXX> -  Here userXX , you will get this folder in dataset folder this will basically create personID and it will add this id into database.
  
8. Python Add_person_faces.py <userXX> - To train the model

9. Python train.py - To hit the cognitive face api

10. Python get_status.py - To check the status of training.

11. Python demo.py - Which is the process of Identifying the images and making the attendance based on the recognized faces.

If you have any query do let me know.

