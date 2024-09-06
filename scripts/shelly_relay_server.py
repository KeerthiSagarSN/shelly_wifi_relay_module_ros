#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
import requests

class Shelly1PMRelayServer(Node):

    def __init__(self):
        super().__init__('shelly_1pm_relay_server')
        self.srv = self.create_service(SetBool, 'shelly_relay_control', self.relay_control_callback)
        self.shelly_ip = '192.168.30.11'  # Replace with your Shelly 1PM's IP address
        self.get_logger().info('Shelly 1PM Relay Server is ready')

    def relay_control_callback(self, request, response):
        state = 'on' if request.data else 'off'
        success = self.send_shelly_request(state)
        
        response.success = success
        response.message = f'Relay turned {state}' if success else f'Failed to turn relay {state}'
        return response

    def send_shelly_request(self, state):
        url = f'http://{self.shelly_ip}/relay/0'
        params = {'turn': state}
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            self.get_logger().info(f'Successfully sent request to Shelly: {response.text}')
            return True
        except requests.RequestException as e:
            self.get_logger().error(f'Failed to send request to Shelly: {e}')
            return False

def main(args=None):
    rclpy.init(args=args)

    shelly_server = Shelly1PMRelayServer()

    try:
        rclpy.spin(shelly_server)
    except KeyboardInterrupt:
        pass
    finally:
        shelly_server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()