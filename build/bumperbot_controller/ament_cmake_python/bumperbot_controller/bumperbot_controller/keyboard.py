#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
import sys
import termios
import tty

class KeyboardController(Node):
    def __init__(self, name: str):
        super().__init__(name)
        self.keyboard_publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.callback)

    def callback(self):
        # Callback function to be implemented
        pass

    def read_keyboard(self, msg: int, vel: float):
        # Function to read keyboard input and publish TwistStamped message
        twist = TwistStamped()
        twist.twist.linear.x = vel if msg == 1 else 0.0
        twist.twist.angular.z = vel if msg == 2 else 0.0
        self.keyboard_publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardController('keyboard_controller')
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    def getchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def main(args=None):
        rclpy.init(args=args)
        node = KeyboardController('keyboard_controller')
        
        try:
            vel = 0.2
            while rclpy.ok():
                key = getchar()
                msg = -1
                if key == 'w':
                    msg = 1
                elif key == 's':
                    msg = 0
                elif key == 'a':
                    msg = 2
                elif key == 'd':
                    msg = 3
                elif key == 'q':
                    break
                elif key == 'e':
                    vel += 0.1
                elif key == 'r':
                    vel -= 0.1
                
                node.read_keyboard(msg, vel)
        except KeyboardInterrupt:
            pass

        node.destroy_node()
        rclpy.shutdown()



    if __name__ == '__main__':
        main()
        print("Control Your Robot!")
        print("---------------------------")
        print("Moving around:")
        print("   w    ")
        print("a  s  d")
        print("Increase/Decrease speed:")
        print("e/r")
        print("Quit:")
        print("q")