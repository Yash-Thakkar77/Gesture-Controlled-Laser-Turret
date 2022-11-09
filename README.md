# Gesture-Controlled-Laser-Turret

This the code for gesture controlled laser turret. The comments in main.py are pretty self explanatory. I stole the idea from Michael Reeves' video - https://www.youtube.com/watch?v=Q8zC3-ZQFJI. Had to change the idea into a laser turret that shines laser at your hand because it is apparently unsafe to shine laser in people's eyes.

Originally the plan was to make the laser track hands and move but for that the webcam/camera must be close to the turret and we didn't have an external one. Now the laser turret basically moves with the position of the index finger.

The hand tracking program is written in python with openCV and mediapipe and sends the coordinates of the hand to the board using the pySerial library.
