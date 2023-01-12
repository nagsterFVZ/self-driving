# Steering and Drivetrain

## 1 - Introduction

In order to facilitate a self-driving vehicle numerous physical and software components will be needed alongside the chassis and drivetrain of the vehicle itself. This research document will outline what components will be needed, outline available options and support decisions made on what components to use.

## 2 - Requirements

### Steering

- The car needs to be able to navigate the tight corners of the NXP track.
- The car needs to be able to smoothly go around corners.

### Drivetrain

- The drivetrain has to be able to reach an output speed of 20-25km/h.
- The drivetrain has to have enough power to make the car drive at 50% speed when 60% of its total weight is added.

## 3 - Gears

### Types of gears

Spur gears and helical gears are two of the most common types of gears. They can often be used for the same types of applications, but what are the differences in these two types of gears?

Spur gears are the most common type, and are the most simple. They have straight teeth parallel to the axis of the gear. This is the most economical type of gear since it is easy to manufacture and has a simple design. These types of gears work well at low to medium speeds, but they start vibrating and making a lot of noise at higher rpm. Spur gears can only transfer parallel power.

Helical gears have teeth that are angled compared to the gear axis. Because of the angle teeth engage more gradually, they have smoother and quieter operation. They also have a greater tooth strength and a higher load carrying capacity. They can also transfer parallel and non-parallel power between shafts. Downside is that they create axial forces that need to be accounted for.

### Visualisation

For the gearing we experimented with 3d printing to save costs, metal gears of this size are pretty expensive. Since we are talking about low power transmission we thought that 3d printing gears can be enough if we get the size of the teeth right. We started off small because keeping things compact was a pre. We experienced that the printer could do it but that tolerances were too small to make a good working gear. For reference this gear is 7mm in diameter. At this size the teeth aren’t detailed enough to work properly with the bigger gear.

After this result we upscaled the gears a bit to see if the result would be better, instead of 3d modelling new gears we upscaled the first file by 2x. We basically got the same result but bigger, this probably has to do with the quality of the stl-file.

Since the gears didn’t run smooth again we started modelling new gears. By upping the modules of the gears (meaning bigger teeth and diameter) we got a good result, teeth look and feel strong and the gears run well. But as said in the previous subheader, spur-gears don’t run smooth at high speeds.

Since spur gears don’t run smooth at higher speed we of course tried to print helical gears to see if the printer could do it and if they would work well. They work great, even when not printed at the best settings. But there is one downside, the axial forces they create. Since handling those forces on an axle is not the easiest, we came up with the idea to “mirror” these gears so we would get a V-shaped gear. This would solve the problem with the axial forces in our eyes. We know that these gears work nice together, there is some friction but it’s plastic so after some use the sharper edges creating this friction will degrade. When those edges have degraded the gears will run smoother.

## 4 - Motors

First we are going to define the different types of electric motors and their pros and cons, then we will look at some variables important for choosing a motor. After that we will outline why we chose the motor that we have bought.

### Brushed motor

A brushed motor is a motor that works by reversing the polarity of the magnets through the use of brushes. The static magnets are on the outside and the electromagnets are on the inside on the rotor. While spinning, brushes change the polarity by brushing over the commutator. These switch the direction that the power flows through the rotor coils.

**Pros of brushed motors**:

- cheaper
- easier to control

**Cons of brushed motors**:

- more wear
- More friction that creates heat. (active cooling needed)

### Brushless motor

In a brushless motor, the polarity is reversed with a controller. The permanent magnets are on the inside(rotor) while the electromagnets are on the outside. When the polarity of these magnets is changed, they will either push or pull the rotor. This type of motor needs a controller to be able to turn.

**Pros of brushless motors:**

- Better control
- more power

**Cons of brushless motors:**

- expensive
- need an expensive controller
- RPM often higher

### Motor kV ratings

Most motors come with a kV-rating. This is a value that determines how fast the motor can spin and how much the RPM will increase when a higher voltage is applied.

For example; if you raise the voltage by one on a 1000 kV motor, the RPM will increase by 1000. With this you get an idea what the output of the motor is and the way the motor will react to changes in voltage.

### T-value

All electric motors have a t-value. This indicates the amount of wire that is wrapped inside the motor. A higher turn means that more wire is wrapped inside, thus increasing the resistance resulting in a slower motor. So, a 4T motor is faster than a 20T motor.

Conclusion

Described above are the differences between a brushed and a brushless motor. Both motors serve a different goal and should be used in different projects.

It was decided to go with a brushless motor. They are more efficient and produce less heat. It is harder to precisely set a certain speed, and the speeds during testing have been very high. This has been due to not having a load on the motor. It is expected that when the motor is in the car, it will slow down and thus be easier to control.

For this project an active motor cooler has been bought, because even though the heat produced by a brushless motor is less than a brushless motor, it is still a significant amount.

- Why we chose this motor
- Why not another one

## 5 - Steering

Steering is done by pulling/pushing on a steering rod attached to the wheel hubs of the front wheels. A car can also steer by changing the amount of power that is delivered to each wheel to make it steer like a tank. For that to work however there needs to be multiple motors, which are not available.

In this car, we went with a servo in the base of the chassis. Attached to this is a hub to which the steering rods are connected. By rotating this hub, it will push/pull on the rods in such a way that the front wheels will steer in the same direction.

### Ackermann

If the steering rods were just attached to the wheel hubs, the steering would not be optimal. Due to the way a car drives through a corner, the front wheels are driving over circles with different radii. This means that the wheels need to steer at different angles to prevent sideways slip. To accomplish this the Ackermann steering geometry can be used while designing the steering mechanism.

For ackermann, there need to be small beams attached to the wheel hubs. These need to be pointing to the midpoint of the rear axle. This gives the front wheels their own turning degree with a specific input, so that there is no sideway slip while going through a corner.

### Steering in combination with suspension

The front wheels of the car are also suspended. This means that the wheel hubs move up and down. The steering hub on the servo however stays in the same place, so the steering rod needs to move up and down as well. This is accomplished with a ball joint on both steering rods at the hub side. On the hub side the hole is made bigger and the rod is bent in place, so that it can freely move around.

### Steering process description

We started on the steering mechanism relatively late in the process. We had already bought the servo and made space in the chassis to house the servo, but did not yet design a specific way to steer.

For the steering we bought a servo saver. This is an attachment to the servo that will immediately push on the mechanism, but a reverse force on the servo will be absorbed by a spring.

The servo saver had several holes to attach steering rods. We first bought only 2 ball joints. The idea was that on the wheel hubs we could bend the steering rods through a hole that was slightly bigger. This would allow the rod to make a slight angle, but still push/pull. While trying to bend the rods however they broke when the angle was around 90 degrees. To solve this we bought 2 more ball joints to use on the wheel hub side. Between these ball joints are the rods. These can be pushed further in the ball joints to adjust the default steering angle. By turning the servo we can push/pull the steering rods, thus steering the wheels and the car.

After the midterm we got the nxp cup plates on which we are going to have to drive. On these we noticed that we could not make the turns, as they are quite sharp, so we had to increase the steering angle. For this we found two solutions that could work,

- Decrease the wheel base(‘length’)
- Increase the steering angle

We decided to do both solutions, because we want to make the turn without locking the steering. (steering angle to spare) Increasing the steering angle is done by increasing the length of the servo saver. This means that with the same angle of rotation of the servo the steering rods are pushed/pulled further.

To decrease the wheelbase we had to stuff some components closer together to make the base of the car shorter.

After these changes the steering has improved massively. It can now easily take turns on the tiles. It also has steering angle to spare, which can be used to manoeuvre around the obstacles.

## Sources

<table>
  <tr>
   <td><strong>Title</strong>
   </td>
   <td><strong>Date Accessed</strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://gearmotions.com/helical-gears-vs-spur-gears/#:~:text=Spur%20gears%20are%20not%20known,angle%20to%20the%20gear%20axis">https://gearmotions.com/helical-gears-vs-spur-gears/#:~:text=Spur%20gears%20are%20not%20known,angle%20to%20the%20gear%20axis</a>. 
   </td>
   <td>
   22 Sept 2022
   </td>
  </tr>
  <tr>
   <td><a href="https://www.quora.com/What-is-anti-ackerman-steering-geometry">https://www.quora.com/What-is-anti-ackerman-steering-geometry</a> 
   </td>
   <td>
   17 Nov 2022
   </td>
  </tr>
</table>
