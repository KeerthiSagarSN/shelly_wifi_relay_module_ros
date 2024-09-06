# shelly_wifi_relay_module_ros2
To run the WIFI relay module through ROS1 Service Client: 

Clone the repository into your workspace

```
cd ros_ws\src\
git clone KeerthiSagarSN\shelly_wifi_relay_module_ros1\
```
Build the repository
```
cd ros1_ws\
catkin build
```
Launch ROSCORE

```
roscore
```


Launch the Wifi_relay service using the following command

```
rosrun shelly_wifi_relay_module_ros1 shelly_relay_server.py
```
Launch the client for sending ON/OFF requests to the relay as follows

For switchin ON
```
rosrun shelly_wifi_relay_module_ros1 shelly_relay_client.py on
```

For switchin OFF
```
rosrun shelly_wifi_relay_module_ros1 shelly_relay_client.py off
```

