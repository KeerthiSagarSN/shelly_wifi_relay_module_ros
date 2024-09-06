#!/usr/bin/env python

import rospy
from std_srvs.srv import SetBool, SetBoolResponse
import requests

class Shelly1PMRelayServer:

    def __init__(self):
        rospy.init_node('shelly_1pm_relay_server')
        self.srv = rospy.Service('shelly_relay_control', SetBool, self.relay_control_callback)
        self.shelly_ip = '192.168.30.11'  # Replace with your Shelly 1PM's IP address
        rospy.loginfo('Shelly 1PM Relay Server is ready')

    def relay_control_callback(self, request):
        state = 'on' if request.data else 'off'
        success = self.send_shelly_request(state)
        
        response = SetBoolResponse()
        response.success = success
        response.message = f'Relay turned {state}' if success else f'Failed to turn relay {state}'
        return response

    def send_shelly_request(self, state):
        url = f'http://{self.shelly_ip}/relay/0'
        params = {'turn': state}
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            rospy.loginfo(f'Successfully sent request to Shelly: {response.text}')
            return True
        except requests.RequestException as e:
            rospy.logerr(f'Failed to send request to Shelly: {e}')
            return False

if __name__ == '__main__':
    try:
        server = Shelly1PMRelayServer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass