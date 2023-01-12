<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.684 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Sun Jan 08 2023 10:51:53 GMT-0800 (PST)
* Source doc: Sensors
* Tables are currently converted to HTML tables.
----->

# Sensors

## 1 - Object detection

This chapter is dedicated to sensors, which make detecting objects possible.

### Sonar

Self-driving cars can use sonar (sound navigation and ranging) to detect and communicate with objects, and to navigate. Sonar can be passive or active. Passive sonar systems passively listen for sounds made by nearby objects. Active sonar systems emit sound pulses and read echoes returned from physical surfaces.

Self-driving cars can use sonar to detect large objects made of solid, liquid, granular materials, or materials in powder form, at short distances. Sonar sensors don’t require light to operate. However, sonar sensors are constrained by the speed of sound (which is slower than the speed of light) and sometimes falsely detect non-existing objects. This allows the use of low speed signal processing in ultrasonic systems. However, pressure based atmospheric conditions can debilitate the overall performance of ultrasonic sensors, which promotes the use of SRRs and other technologies instead.

Ultrasonic sensors rely on sonic transducers to transmit sonic waves in the range of 40 kHz to 70 kHz for automotive applications. This frequency range is beyond the audible range for humans, which makes it safe for human ears. This is an important factor given that a cars’ parking system can generate more than 100 dB of sound pressure to assure clear reception, which is equivalent to the audible sound pressure from a jet engine.

### Radar

Radar (radio detection and ranging) is useful in many contexts such as weather forecasting, astronomy, communications, ocean navigation, military operations, and autonomous driving.

Autonomous cars can emit radio waves in known directions with radar transmitters. Reflected waves that return to a car’s radar receiver help the car derive information about environmental objects like the objects’ angles, ranges, and velocities.

Radar typically operates well over long distances and in most weather types. However, it isn’t particularly useful for object identification and may falsely identify objects.

#### SRR

The SSR applications are essentially designed to replace ultrasonic sensors and to support highly automated driving. SRR is, for example, used for parking assistance or side view detection.

#### MRR & LRR

An MRR or LRR can be implemented to detect far targets or objects in front of the ego car.

### Lidar

Lidar (light detection and ranging), also known as 3D laser scanning, is a tool that self-driving cars use to scan their environments with lasers. A typical lidar sensor pulses thousands of beams of infrared laser light into its surroundings and waits for the beams to reflect off environmental features. Many pulses create point clouds (sets of points representing 3D forms in space) of light.

Lidar systems measure the amount of time it takes to emit a laser signal and sense the same light beam reflected from a physical surface onto its photodetectors. Lidar uses the speed of light to calculate distances to objects. The longer it takes for a lidar photodetector to receive a return light signal, the farther away an object is.

Lidar systems enable self-driving cars to detect small objects with high precision. However, lidar is often unreliable at nighttime or in inclement weather.

Since rare earth metals are needed in order to produce adequate lidar sensors, these sensors are much more expensive than radar sensors used in autonomous vehicles. Yet another problem is that snow or fog can sometimes block lidar sensors and negatively affect their ability to detect objects in the road.

Today, anyone can buy a distance meter using this principle from almost any home and building supply store to accurately determine distances up to a few yards. The challenge for a driver assistance system is to ensure that it will function under all possible environmental conditions (temperature, solar radiation, darkness, rain, snow), and above all, recognize objects up to 300 yards away. And of course, all this in large-scale production at the lowest possible cost and smallest dimensions.

Lidar systems are not new and have been in use in industry and the military for many years. However, these are complex mechanical mirror systems with a 360° all-round visibility that capture spatial images of objects. At costs of several tens of thousands of dollars, these mechanical systems are not suitable for large-scale deployment in the automotive sector.

### Camera

Cameras are one of the most adopted technologies for perceiving the surroundings. A camera works on the principle of detecting lights emitted from the surroundings on a photosensitive surface (image plane) through a camera lens (mounted in front of the sensor) to produce clear images of the surroundings. Cameras are relatively inexpensive and with appropriate software, can detect both moving and static obstacles within their field of view and provide high-resolution images of the surroundings. These capabilities allow the perception system of the vehicle to identify road signs, traffic lights, road lane markings and barriers in the case of road traffic vehicles and a host of other articles in the case of off-road vehicles.

Given the above, cameras are a ubiquitous technology that provides high-resolution videos and images, including color and texture information of the perceived surroundings. Common uses of the camera data on AVs include traffic signs recognition, traffic lights recognition, and road lane marking detection. As the camera’s performance and the creation of high-fidelity images are highly dependent on the environmental conditions and illumination, image data are often fused with other sensor data such as radar and LiDAR data, to generate reliable and accurate environment perception in AD.

Autonomous cars often have video cameras and sensors in order to see and interpret the objects in the road just like human drivers do with their eyes. By equipping cars with these cameras at every angle, the vehicles are capable of maintaining a 360° view of their external environment, thereby providing a broader picture of the traffic conditions around them.

Like other sensor systems, cameras have strengths and limitations. Cameras offer advantages associated with high-resolution imagery but do not work well in all weather types. Also, cameras only capture visible visual data.

#### Vis Camera

VIS cameras capture wavelengths that range from 400 to 780 nm, similar to human eyes. They are mostly used due to their low cost, high resolution, and their capability to differentiate between colors.

##### Monocular vision

The monocular camera system utilizes a single camera to create a series of images. The conventional RGB monocular cameras are fundamentally more limited than stereo cameras in that they lack native depth information, although in some applications or more advanced monocular cameras using the dual-pixel autofocus hardware, depth information may be calculated using complex algorithms. As a result, two cameras are often installed side-by-side to form a binocular came-ra system in autonomous vehicles.

##### Stereo vision

Combining two VIS cameras with a predetermined focal distance allows stereo vision to be performed; hence, a 3D representation of the scene around the vehicle is possible.Today, 3D cameras are available and utilized for displaying highly detailed and realistic images. These image sensors automatically detect objects, classify them, and determine the distances between them and the vehicle. For example, the cameras can easily identify other cars, pedestrians, cyclists, traffic signs and signals, road markings, bridges, and guardrails.

However, even in a stereoscopic vision camera system, the estimated depth accuracies are lower than the ones obtained from active range finders such as RADARs and LiDARs. Poor weather conditions such as rain, fog, or snow can prevent cameras from clearly seeing the obstacles in the roadway, which can increase the likelihood of accidents. Additionally, there are often situations where the images from the cameras simply aren’t good enough for a computer to make a good decision about what the car should do. For example, in situations where the colors of objects are very similar to the background or the contrast between them is low, the driving algorithms can fail.

#### NIR Camera

NIR cameras can be used for range detection by using the ToF principle and the phase difference between the transmitted and the received light pulses. Depending on the number of light emitting diodes (LEDs) utilized in the LED array, the distance ranges from 10 m for interior scenes to roughly 4 m for outdoor scenes.

#### IR Camera

IR cameras work with infrared wavelengths ranging between 780 nm and 1 mm. They can be extended to the near-infrared and the mid-infrared for certain applications. IR cameras are less susceptible to weather or lighting conditions, and it can overcome some of the VIS cameras shortcomings in situations where there are peaks of illumination. In addition, they can be used for warm body detection, such as pedestrians and animals.

### Conclusion

<table>
  <tr>
   <td><strong>Feature</strong>
   </td>
   <td><strong>LiDAR</strong>
   </td>
   <td><strong>RADAR</strong>
   </td>
   <td><strong>Camera</strong>
   </td>
   <td><strong>Ultrasonic</strong>
   </td>
  </tr>
  <tr>
   <td>Primary Technology
   </td>
   <td>Laser Beam
   </td>
   <td>Radio Wave
   </td>
   <td>Light
   </td>
   <td>Soundwave
   </td>
  </tr>
  <tr>
   <td>Range
   </td>
   <td>~200 m
   </td>
   <td>~250 m
   </td>
   <td>~200 m
   </td>
   <td>~5 m
   </td>
  </tr>
  <tr>
   <td>Resolution
   </td>
   <td>Good
   </td>
   <td>Average
   </td>
   <td>Very good
   </td>
   <td>Poor
   </td>
  </tr>
  <tr>
   <td>Affected by weather conditions
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
  </tr>
  <tr>
   <td>Affected by lighting conditions
   </td>
   <td>No
   </td>
   <td>No
   </td>
   <td>Yes
   </td>
   <td>No
   </td>
  </tr>
  <tr>
   <td>Detects speed
   </td>
   <td>Good 
   </td>
   <td>Very good
   </td>
   <td>Poor
   </td>
   <td>Poor
   </td>
  </tr>
  <tr>
   <td>Detects distance
   </td>
   <td>Good
   </td>
   <td>Very good
   </td>
   <td>Poor
   </td>
   <td>Good
   </td>
  </tr>
  <tr>
   <td>Interference susceptibility
   </td>
   <td>Good
   </td>
   <td>Poor
   </td>
   <td>Very Good
   </td>
   <td>Good
   </td>
  </tr>
  <tr>
   <td>Size 
   </td>
   <td>Bulky
   </td>
   <td>Small
   </td>
   <td>Small
   </td>
   <td>Small
   </td>
  </tr>
</table>

## 2 - Motion detection

Inertial navigation systems like inertial measurement units (IMUs) (e.g. accelerometers, gyroscopes) detect a car’s physical movements. These navigation devices help self-driving cars stabilize themselves and also help cars determine whether they should take any kind of protective safety actions.

## 3 - Location detection

Self-driving cars can use GPS to geolocate with numerical coordinates (e.g. latitude, longitude) representing their physical locations in space. They can also navigate by combining real-time GPS coordinates with other digital map data (e.g. via Google Maps).

GPS data often varies around a five-meter radius. To compensate for imprecise GPS data, self-driving cars can use unique data-processing techniques like particle filtering to improve location accuracy.

The operating principle of the GPS is based on the ability of the receiver to locate at

least four satellites, to calculate the distance to every single one of them, and then uses this

information to identify its own location by using a process called trilateration. It is worth

mentioning that GPS signals suffer from several errors that degrade the accuracy of the

system, such as the following:

- timing errors due to differences between the satellite atomic clock and the receiver quartz clock
- signal delays due to propagating through the ionosphere and troposphere
- multipath effect
- satellite orbit uncertainties.

In order to improve the accuracy of current positioning systems on vehicles, data from satellites are merged with data from other vehicle sensors (e.g., inertial measurement unit

(IMU), LiDARs, RADARs, and cameras) to achieve reliable position information.

## 4 - Links

### Sonar

- [DFRobot A02YYUW Waterdichte Ultrasonische Sensor - UART](https://www.tinytronics.nl/shop/nl/sensoren/afstand/dfrobot-a02yyuw-waterdichte-ultrasonische-sensor-uart)
- [Ultrasonische Sensor - US-100 - UART - Met Temperatuursensor](https://www.tinytronics.nl/shop/nl/sensoren/temperatuur/ultrasonische-sensor-us-100-uart-met-temperatuursensor)
- [Ultrasonische Sensor - HC-SR04](https://www.tinytronics.nl/shop/nl/sensoren/afstand/ultrasonische-sensor-hc-sr04)
- [Waterdichte Ultrasonische Sensor - JSN-SR04T](https://www.tinytronics.nl/shop/nl/sensoren/afstand/waterdichte-ultrasonische-sensor-jsn-sr04t)

### Radar

- [SparkFun Pulsed Radar Breakout - A111 - SEN-16826](https://www.sparkfun.com/products/16826)

### Lidar (ToF)

- [DFRobot ToF IR Afstandssensor - 0.2-12m - Time-of-Flight](https://www.tinytronics.nl/shop/nl/sensoren/afstand/dfrobot-tof-ir-afstandssensor-0.2-12m-time-of-flight)
- [Sharp Optische Afstandsensor GP2Y0A02YK0F](https://www.tinytronics.nl/shop/nl/sensoren/afstand/sharp-optische-afstandsensor-gp2y0a02yk0f)
- [Time-of-Flight Afstandssensor - TOF10120](https://www.tinytronics.nl/shop/nl/sensoren/afstand/time-of-flight-afstandssensor-tof10120)
- [LDROBOT D300 LiDAR Kit](https://www.elektor.nl/new/new-in-the-store/ldrobot-d300-lidar-kit-360-degree-laser-range-scanner-12-m)

### Camera

- [Raspberry Pi Compatible Camera 5MP met IR Verlichting](https://www.tinytronics.nl/shop/nl/sensoren/optisch/camera%27s-en-scanners/raspberry-pi-compatible-camera-5mp-met-ir-verlichting)
- [Raspberry Pi Camera V2 - 8MP - RPICAMV2](https://www.tinytronics.nl/shop/nl/sensoren/optisch/camera's-en-scanners/raspberry-pi-camera-v2-8mp)

### Motion Detection

- [MPU-9255 Accelerometer - Gyroscope - Magnetometer 9DOF Module 3.3V-5V - MPU9255](https://www.tinytronics.nl/shop/nl/sensoren/magnetisch-veld/mpu-9255-accelerometer-gyroscope-magnetometer-9dof-module-3.3v-5v)

### Location Detection

- [ATGM336H GPS Module](https://www.tinytronics.nl/shop/nl/communicatie-en-signalen/draadloos/gps/modules/atgm336h-gps-module)
- [GSM / GPRS / Bluetooth HAT voor Raspberry Pi](https://www.sossolutions.nl/gsm-gprs-bluetooth-hat-voor-raspberry-pi)

## 5 - Chosen Sensors

[Slamtec](https://www.slamtec.com/en/Lidar/A1): The main reasons we chose this one are because it is of high quality and we could borrow it for free. THis lidar sensor will be used for object detection.

[Sensor Module](https://www.tinytronics.nl/shop/nl/sensoren/magnetisch-veld/mpu-9255-accelerometer-gyroscope-magnetometer-9dof-module-3.3v-5v): This board was chosen because it has an accelerometer, gyroscope and magnetometer for a low price. Also a lot of information about it can be found online about how to use it.

[Temp Probe](https://www.tinytronics.nl/shop/nl/3d-printen/extrusie/hotends-en-extruders/ntc-100k-3950-met-kabel): These sensors are used for detecting the temperature of vital components which are expected to get hot.It is easy to use.

##

## 6 - Sources

<table>
  <tr>
   <td><strong>Title</strong>
   </td>
   <td><strong>Date Accessed</strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.udacity.com/blog/2021/03/how-self-driving-cars-work-sensor-systems.html">How Self-driving Cars Work: Sensor Systems | Udacity</a>
   </td>
   <td>
   15 Spet 2022
   </td>
  </tr>
  <tr>
   <td><a href="https://www.itransition.com/blog/autonomous-vehicle-sensors">3 types of autonomous vehicle sensors | Itransition</a>
   </td>
   <td>
   19 Spet 2022
   </td>
  </tr>
  <tr>
   <td><a href="https://www.fierceelectronics.com/components/three-sensor-types-drive-autonomous-vehicles">Three Sensor Types Drive Autonomous Vehicles | Fierce Electronics</a>
   </td>
   <td>
   19 Spet 2022
   </td>
  </tr>
  <tr>
   <td><a href="https://encyclopedia.pub/entry/8356">Sensor Technology in Autonomous Vehicles | Encyclopedia MDPI</a>
   </td>
   <td>
   19 Spet 2022
   </td>
  </tr>
  <tr>
   <td><a href="https://www.mdpi.com/1424-8220/21/16/5397/pdf">Overview of vehicle sensors</a>
   </td>
   <td>
   19 Spet 2022
   </td>
  </tr>
</table>
