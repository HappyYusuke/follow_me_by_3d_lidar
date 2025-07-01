# detection_visualizer.py という名前で保存してください

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from vision_msgs.msg import Detection3DArray
from visualization_msgs.msg import Marker, MarkerArray

class Detection3DVisualizer(Node):
    def __init__(self):
        super().__init__('detection_3d_visualizer_node')
        
        # 3D検出結果トピックの購読
        # TODO: 実際のトピック名に合わせて変更してください
        self.subscription = self.create_subscription(
            Detection3DArray,
            '/bbox',  
            self.detection_callback,
            10)
        
        # MarkerArray配信用パブリッシャー
        self.marker_publisher = self.create_publisher(MarkerArray, '/detections/markers', 10)

    def detection_callback(self, msg: Detection3DArray):
        marker_array = MarkerArray()
        
        # 検出された各オブジェクトに対してマーカーを作成
        for i, detection in enumerate(msg.detections):
            marker = Marker()
            marker.header = msg.header
            marker.ns = "detections"
            marker.id = i
            marker.type = Marker.CUBE
            marker.action = Marker.ADD
            
            # バウンディングボックスの中心位置と姿勢を設定
            marker.pose = detection.bbox.center
            
            # バウンディングボックスの大きさを設定
            marker.scale = detection.bbox.size
            
            # マーカーの色を設定 (例: 半透明の赤色)
            marker.color.r = 1.0
            marker.color.g = 0.0
            marker.color.b = 0.0
            marker.color.a = 0.7  # 透明度
            
            # マーカーの表示時間を設定 (例: 1秒)
            marker.lifetime = Duration(seconds=1.0).to_msg()
            
            marker_array.markers.append(marker)
            
        # MarkerArrayをパブリッシュ
        self.marker_publisher.publish(marker_array)

def main(args=None):
    rclpy.init(args=args)
    visualizer_node = Detection3DVisualizer()
    rclpy.spin(visualizer_node)
    visualizer_node.destroy_node()
    rclpy.shutdown()
