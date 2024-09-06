#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool
import sys

def shelly_relay_client(state):
    rospy.init_node('shelly_1pm_relay_client', anonymous=True)
    rospy.wait_for_service('shelly_relay_control')
    try:
        relay_control = rospy.ServiceProxy('shelly_relay_control', SetBool)
        response = relay_control(state)
        return response.success, response.message
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return False, str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['on', 'off']:
        rospy.logerr('Usage: rosrun shelly_wifi_relay_module shelly_relay_client.py <on|off>')
        sys.exit(1)

    state = sys.argv[1] == 'on'
    success, message = shelly_relay_client(state)

    if success:
        rospy.loginfo(f'Successfully turned relay {"on" if state else "off"}')
    else:
        rospy.logerr(f'Failed to turn relay {"on" if state else "off"}: {message}')