# Project Blog Floris van Zeeland
## Week 1: 05-09-2022
This week myself and the group spent most of our time getting to know each other and defining the project. I asked Chris for some further details and constraints. Then with the group we began brainstorming potential ideas for the project. We divided the project into different parts of the vehicle so that we can all work independently and also together. My part of the project is the control system. So writing the software that will control the car.

The rest of the week was spent working on my personal development plan.
## Week 2: 12-09-2022
I started the week by completing my PDP and then continuing work on the plan of approach. This week I also started working on my research for the control system. This consists mainly of determining the hardware on which the final code will run.
## Week 3: 19-09-2022
After the research into different hardware options last week, I proposed that we go with a Raspberry Pi 4. This week I spent many days configuring the pi, sadly due to strange issues and legacy documentation I ended up reinstalling different operating systems multiple times. This was mostly due to certain functionality not working in one OS but working in another.
## Week 4: 26-09-2022
This week I finally got the Pi working as needed. I have now chosen to go for the latest Raspian OS, this has support for the Pi Camera we want to use. However the database solution Redis was still giving issues. I spent the rest of the week trying to resolve these problems, in the end I had to build the module I needed myself to get it running.
## Week 5: 03-10-2022
After getting Redis working last week, I have spent this week starting to implement the polling of sensors and storing their data to the Redis in memory database. So far I have implemented the reading of data from the gyroscope, accelerometer, magnetometer and the analogue to digital boards. I did have to do some troubleshooting in order to figure out how to properly read data over I2C. But after digging through some datasheets I managed to get the data readout working.
## Week 6: 10-10-2022
This week I have been busy comparing different image detection and machine learning libraries. Besides that I have helped with some brainstorming for the suspension/drivetrain setup and updated my personal development plan. I also found some more useful materials for learning lane detection so I will be looking at those next week.
## Week 7: 17-10-2022
For most of this week I have spent time creating this documentation website and working on getting the PWM libraries working, for this I am having to make use of blinka. Blinka allows running Circuit-Python libraries in normal Python. It is developed by adafruit and we need it for using many of their other libraries that support some of the sensors we use.
## Week 8: 31-10-2022
I spent this week working on the Dashboard for showing the different sensor data. I also spent some time refing the ingest script which handles getting the data from the sensors. We used to get sensor data every second, we have now changed that to get data 10 times per second and average it to 1 point. This way our data is a lot less prone to errors due to fluctuations and represents are more accurate display of the sensor data.
## Week 9: 07-11-2022 - Midterm
This week we had our midterm presentation, so most of the week was spent preparing our presentation and demo. Michael and Tom presented our project while I was responsible for the demo and Q&A. We sadly had some techincall difficulties with the car startup which inpacted the demo. Because of this for the final presentation I will ensure that we have a pre-recorded demo in the event that the live demo has issues again. Further this week I did some more changes to the dashboard in order to get it working better.
<iframe width="560" height="315" src="https://www.youtube.com/embed/yt2jBFw0TAQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Week 10: 14-11-2022
This week was spent doing a lot of the administrative tasks for the project. These tasks were also geared towards my PDP goals. For my soft goal of budgeting I went and reworked our part list/budget into a good structured document. Now we can easy see what parts have been ordered, what we are borrowing and how much we have spent. I also added this part list to our documentation.

I also spent a good amount of time updating the content of all the blogs. Lastly I spent time on doing some more research into how best we can controll the ESC using python on our Pi.
## Week 11: 21-11-2022
I started the week working on implementing last weeks research into controlling the ESC. After some trial and error I managed to get it working. Turns out we do not need a PWM controller and can use the PWM thats on the Pi itself. The ESC responds to a frquency of 50Hz with a duty cycle of 5%-10%. I then had to implement the inputs to mimic the calibration and arming sequence on the ESC.

Due to some issues with WiFi on the Pi that I discovered a few weeks back, we have had to start from a new install of Pi OS. So this week I spent 2 days setting up the new install. While doing this I documented every step of the process so that anyone else having to setup the project has a clear guide. The first major pieces of this guide are completed and visible [here](https://becreative.distillation.dev/project/installation.html). The guide still needs to be completed with the setup instructions for the Dashboard, those will follow next week.

I finished the week by implementing ESC functionality into the dashboard. I also ran into an issue with noise in the PWM signal to the ESC, I spent a few hours debuging and fixing that.

## Week 12: 28-11-2022
I started the week by wrapping up adding the ESC functionality into the dashboard. I also had to rewrite some of the ESC control code in order to have better reliability with the arming and calibration sequences.

Next I started working with OpenCV to process image data from the Raspberry Pi Camera. We put the control box on roughly the same hight as the car would be. Then I took some pictures with the camera and started writing the code to filter out the background and leave us with only the track the car is driving on. This process is done in about 5 steps and takes 0.04s per frame. So currently we can process about 20 frames per second. Next I started doing research how we can use this data in TensorFlow. This was mostly research and I am planning to start implementing this over the coming weeks.

## Week 13: 05-12-2022
This week was a bit of a hazy week, a few in the group including myself were sick. I spent Wednesday at home but the rest of the week was at Fontys working as usual. I started the week with testing the new motor and making sure that it responds to the same inputs as the old one. I also created the class to interface with the servo motor so that we can now use that too. Most of Tuesday was spent on updating my PDP with all the progress thus far.

To wrap the week up I reworked the OpenCV script to work with a live video stream. This worked pretty well and we will be able to use it in the coming weeks.

# Week 14: 12-12-2022
This week I started setting everything up to train our model for driving the track. After discussing with a machine learning engineer we deduced the best aproach would be to create a virtual enviroment in Unreal Engine and integrate AirSim to expose API's in order to controll the vehicle from the python script.

Getting the unreal enviroment setup is proving to be a lot of work. The AirSim documentation is not supper clear as it's different parts dont seem to have always been updated when new version were released. Importing our vehicle into Unreal Engine was also a challange as it first had to be exported to Blender and rigged. There are still some issues with the vehicle including the wheels falling off. The setup with AirSim will likely take a few more days, but hopefully end of next week we can start running some trainings.

## Feedback Sessions
### Feedback Session: 08-12-2022
For this feedback session we went one by one and updated the teacher and the group on where we are currently in regards to our goals. My goals are currently all on track, there was no real feedback from the group or the teacher. Everyone was pleased with my progression and group leadership.