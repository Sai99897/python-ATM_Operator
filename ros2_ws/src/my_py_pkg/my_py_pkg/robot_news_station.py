#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
 
class RobotNewStation(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("robot_news_station") # MODIFY NAME
        self.robot="care-o-bot"
        self.publisher_=self.create_publisher(String,"robot_new",10) #inside arguments are data type of message ,topic name ,publishing rate or queue size)
        
        self.timer=self.create_timer(0.5,self.my_publish)
        self.get_logger().info("started the robot_news_station")

    def my_publish(self):
        msg=String()
        msg.data="Hello "+str(self.robot)+ " to the world"
        self.publisher_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args) 
    node = RobotNewStation() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
    
if __name__ == "__main__":
    main()