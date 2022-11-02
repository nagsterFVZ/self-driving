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