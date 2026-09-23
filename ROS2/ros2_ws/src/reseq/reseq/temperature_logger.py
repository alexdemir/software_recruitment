from datetime import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class TemperatureLogger(Node):
    def __init__(self, filename: str = 'log.txt'):
        super().__init__('temperature_logger')
        self.filename = filename
        self.subscription = self.create_subscription(
            Float32,
            '/temperature',
            self.callback,
            10
        )

    def callback(self, temperature: Float32):
        if temperature.data >= 50.0:
            now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f'[{now_str}] High temperature detected: {temperature.data:.2f} °C'
            self.get_logger().warn(log_entry)
            with open(self.filename, 'a') as f:
                f.write(f'{log_entry}\n')


def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger('log.txt')

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
