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
Sadly this week started of pretty bad, we (mostly me) managed to kill my Raspberry Pi 4, this is a bit of a pain seeing as they are out of stock everywhere at the moment.
![Rest in Pi](./images/deadPi.png)
Luckily we can borrow Corné's Pi for the time being so the project can carry on. For the rest this week I have spent time creating this documentation website and working on getting the PWM libraries working, for this I am having to make use of blinka. Blinka allows running Circuit-Python libraries in normaly Python
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

Lastly this week I am busy getting the ESC funtionality added to the dashboard so that we can start the motor and such from there.
## Feedback Sessions
Writeup of feedback sessions coming