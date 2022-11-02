# Control System

## Introduction

In order to facilitate a self-driving vehicle numerous physical and software components will be needed alongside the chassis and drivetrain of the vehicle itself. This research document will outline what components will be needed, outline available options and support decisions made on what components to use.

## Control system requirements

The control system for the vehicle must be able to do the following:

* Control the acceleration and turning of the vehicle
* Detect a lane of an athletics track
* Detect obstacles that are in the way of the vehicle
* Process accelerometer, magnetometer and distance sensor data
* Determine steering based on sensor inputs

The above is the base functionality that the control system will need, the following will be features that are a plus and will improve the vehicle control system:

* Live data dashboard
* Tuning of parameters on the fly
* Live video feed

## Processing unit

In order to compute sensor data and make driving decisions a form of processing unit will be needed. Its main task will be interpreting sensor data, this can come in different forms including video. We evaluated 3 different options for this function, these were an Arduino, Raspberry Pi and Nvidia Jetson. Below are the evaluations for each option.

### Comparison

<table>
  <tr>
   <td>Spec</td>
   <td>Arduino Uno</td>
   <td>Raspberry Pi 4</td>
   <td>Nvidia Jetson</td>
  </tr>
  <tr>
   <td>CPU</td>
   <td>6MHz</td>
   <td>1.5GHz Quad Core</td>
   <td>1.9GHz + Dedicated GPU</td>
  </tr>
  <tr>
   <td>Storage</td>
   <td>32KB</td>
   <td>16GB (sd card)</td>
   <td>16GB</td>
  </tr>
  <tr>
   <td>RAM</td>
   <td>2KB</td>
   <td>4GB</td>
   <td>8GB</td>
  </tr>
  <tr>
   <td>Digital I/O</td>
   <td>14</td>
   <td>26</td>
   <td>40</td>
  </tr>
  <tr>
   <td>Analog Inputs</td>
   <td>6</td>
   <td>0</td>
   <td>0</td>
  </tr>
  <tr>
   <td>Price</td>
   <td>€20</td>
   <td>€80</td>
   <td>€500+</td>
  </tr>
</table>

#### Arduino Uno

While the Arduino has a good amount of analog inputs and comes in at a low price, the processing power of the cpu is not powerful enough to do image detection. Another key factor is that Arduino uses scripts written in c++, this means we would lose access to many powerful python libraries that are key to this project. For these reasons an Arduino would not be good enough for this project.


#### Raspberry Pi 4

The Raspberry Pi is a well known small form factor computer which excels at IoT and other projects. The current latest model the Pi 4 comes with a range of RAM options, the only one we can get due to shortages comes with 4gb of RAM. The Pi 4 also has a 1.5GHz quad core cpu which gives us much better performance for doing more complicated image processing and potentially machine learning. Budget wise the Pi is not cheap but we can borrow one for free so this looks like a great option.


#### Nvidia Jetson

These small computers are great for machine learning or any other AI applications, however they are much harder to come by at the moment and can be extremely expensive. While the performance of the Jetson would serve our project well, we cannot justify the costs for it.


### Decision

We have decided to use the Raspberry Pi 4 for this project, it comes out the best on a price to performance standpoint. The Pi also has all the Digital I/O we could need for connecting different sensors. The Pi also allows us to run linux which means we can easily make use of python for our development.


## Programming language

There are two main options when it comes to choosing a programming language for creating applications on a Raspberry Pi. These languages are Python and C++, they offer the most feature wise and support from the community. Because these languages are feature rich and community supported you can often get libraries to make use of useful programs developed by others.

### Python vs C++

When it comes to performance C++ is the best choice for developing on a system like a Raspberry Pi, it is fast and efficient. However the main downside to C++ is its coding complexity. Python on the other hand is used for many projects where hardware like sensors have to be used. There is a massive amount of public code for python for different sensors and also machine learning algorithms. Python is also much easier to develop and has greater code readability.

The choice for this project will be to move forward with Python, the main reasons for this choice are:

* Availability of open source libraries
* Ease of development
* Prior language experience

## Self driving



## Links
|Description|Source|
|---|---|
|OpenCV Lane Detection|https://medium.com/analytics-vidhya/lane-detection-for-a-self-driving-car-using-opencv-e2aa95105b89|
|Image Processing in Python|https://neptune.ai/blog/image-processing-python|
|Slamtec RPLIDAR SDK|https://github.com/Slamtec/rplidar_sdk|
|Slamtec RPLIDAR Python Library|https://github.com/Roboticia/RPLidar|
|Driving and ESC with Pi|https://www.instructables.com/Driving-an-ESCBrushless-Motor-Using-Raspberry-Pi/|
|Controlling I2C with Pi and Python|https://www.abelectronics.co.uk/kb/article/1090/i2c-part-1---introducing-i2c|
|Building a lane detection system|https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/|
|Self Driving RC Car|https://zhengludwig.wordpress.com/projects/self-driving-rc-car/|
|Self Driving Car with Lane Detection using Raspberry Pi - OpenCV|https://www.youtube.com/watch?v=aXqoPiMPhDw|
|Python Installation of PCA9685|https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython|