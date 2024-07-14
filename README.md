雷达：livox_mid360

gazebo打不开，断开网络连接即


编译
```
cd RoboSim
colcon build --symlink
```


启动仿真,world为可选项RMUC/RMUL
```
source install/setup.bash
ros2 launch pb_rm_simulation rm_simulation.launch.py world:=RMUL
```

启动FAST_LIO
```

source install/setup.bash
ros2 launch fast_lio mapping.launch.py config_file:=mid360.yaml
```