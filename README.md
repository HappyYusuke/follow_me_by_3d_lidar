# follow_me_by_3d_lidar
3D-LiDARを用いた人追従システムです。ROS2で動作します。

# Installation

ros2_tao__pointpillarsのファイルを置換します。
```
# 元のファイルを削除
rm ~/ros2_ws/src/ros2_tao_pointpillars/launch/pp_infer_launch.py

# 本リポジトリのファイルをコピー
cp ~/ros2_ws/src/follow_me_by_3d_lidar/external_files/pp_infer_launch.py ~/ros2_ws/src/ros2_tao_pointpillars/launch/
cp ~/ros2_ws/src/follow_me_by_3d_lidar/external_files/point_cloud2_iterator.hpp ~/ros2_ws/src/ros2_tao_pointpillars/include/pp_infer
```
