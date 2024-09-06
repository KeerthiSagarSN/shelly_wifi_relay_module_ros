# shelly_wifi_relay_module_ros2
To run the WIFI relay module through ROS2 Service Client: 

Clone the repository into your workspace

```
cd ros2_ws\src\
git clone KeerthiSagarSN\shelly_wifi_relay_module_ros2\
```
Build the repository
```
cd ros2_ws\
colcon build
```

Launch the Wifi_relay service using the following command

```
ros2 run shelly_wifi_relay_module_ros2 shelly_relay_server.py
```
Launch the client for sending ON/OFF requests to the relay as follows

For switchin ON
```
ros2 run shelly_wifi_relay_module_ros2 shelly_relay_client.py on
```

For switchin OFF
```
ros2 run shelly_wifi_relay_module_ros2 shelly_relay_client.py off
```

