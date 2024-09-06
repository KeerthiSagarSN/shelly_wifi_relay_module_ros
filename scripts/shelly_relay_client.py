#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
import sys

class Shelly1PMRelayClient(Node):

    def __init__(self):
        super().__init__('shelly_1pm_relay_client')
        self.client = self.create_client(SetBool, 'shelly_relay_control')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.req = SetBool.Request()

    def send_request(self, state):
        self.req.data = state
        future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)

    client = Shelly1PMRelayClient()

    if len(sys.argv) != 2 or sys.argv[1] not in ['on', 'off']:
        client.get_logger().error('Usage: ros2 run your_package shelly_relay_client.py <on|off>')
        client.destroy_node()
        rclpy.shutdown()
        return

    state = sys.argv[1] == 'on'
    response = client.send_request(state)

    if response.success:
        client.get_logger().info(f'Successfully turned relay {"on" if state else "off"}')
    else:
        client.get_logger().error(f'Failed to turn relay {"on" if state else "off"}')

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()