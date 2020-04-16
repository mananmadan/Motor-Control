## Motor Control

**TO RUN THE CODE FOLLOW THE FOLLOWING INSTRUCTIONS:**

1. Go into the catkin_ws into the src folder and clone the node
```
cd catkin_ws/src
git clone https://github.com/mananmadan/Motor-Control
```
2. Compile by running

```
cd ..
catkin_make

```
3. Run roscore

```
roscore
```

4. Run the socket

```
cd catkin_ws/src/motor_control
cd src
python2 reciever.py

```
5. Run the node
```
rosrun motor_commands motor_commands.py

```
6. Temporalily publish the command on the /test topic

```
rostopic pub -1 /test std_msgs/Int16 -- 1.0

```
