# visual_tracking_my_robot

## Description
`visual_tracking_my_robot` is a ROS 2 package designed to enable a robot to visually track and follow a ball based on its color. The default color is yellow, but it can be customized to any other color via launch file parameters. The package supports both 2D and 3D ball detection, and provides real-time control commands to move the robot towards the ball.

## Features
- **Color-based ball detection**: The robot can track a ball based on a specified color in a video stream.
- **Real-time following**: The robot follows the ball based on the visual feedback received from the camera.
- **Customizable tracking**: Allows dynamic configuration of color, detection modes, and other parameters.
- **2D and 3D tracking**: Optional 3D tracking using depth data, in addition to 2D image-based tracking.
- **Simulation support**: Can be used with simulated time for testing in Gazebo or other simulation environments.

## Launch File Overview
The launch file provides various options to customize the behavior of the tracking system.

### Launch Arguments:
- **params_file**: Specifies the path to the parameters file for ball tracking.
  - Default: `params/ball_tracker_params.yaml`
- **detect_only**: If set to `true`, only the detection node will run (useful for testing detection without following the ball).
  - Default: `false`
- **follow_only**: If set to `true`, only the follow node will run (useful for testing following behavior with manually published ball detections).
  - Default: `false`
- **tune_detection**: Enables a tuning mode for the detection component, allowing for easier adjustments of detection parameters.
  - Default: `false`
- **use_sim_time**: Enables simulated time for the follow node, typically used when running in a simulation environment (e.g., Gazebo).
  - Default: `false`
- **image_topic**: The name of the input image topic used for ball detection.
  - Default: `/camera/image_raw`
- **cmd_vel_topic**: The name of the output velocity command topic used to control the robot's motion.
  - Default: `/cmd_vel_tracker`
- **enable_3d_tracker**: If set to `true`, enables 3D ball tracking using depth data.
  - Default: `false`

### Nodes:
- **detect_ball**: Detects the ball in a 2D image stream. 
  - Parameters: `params_file`, `tuning_mode`.
  - Remaps: `/image_in` to the image topic specified in the launch file.
- **detect_ball_3d**: Optional node that enables 3D ball tracking using depth data.
- **follow_ball**: Follows the detected ball, publishing velocity commands to move the robot towards the ball.
  - Parameters: `params_file`, `use_sim_time`.
  - Remaps: `/cmd_vel` to the velocity command topic specified in the launch file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_link>
   cd visual_tracking_my_robot
   ```

2. **Build the workspace**:
   Make sure you are in your ROS 2 workspace, then build the project:
   ```bash
   colcon build
   ```

3. **Source the workspace**:
   Source the workspace setup file:
   ```bash
   source install/setup.bash
   ```

## Usage

To launch the ball tracking system, use the following command:
```bash
ros2 launch visual_tracking_my_robot track_ball.launch.py
```

### Example Custom Configurations:

- **Run only ball detection**:
  ```bash
  ros2 launch visual_tracking_my_robot track_ball.launch.py detect_only:=true
  ```

- **Run only ball following** (with manually provided detections):
  ```bash
  ros2 launch visual_tracking_my_robot track_ball.launch.py follow_only:=true
  ```

- **Enable tuning mode for detection**:
  ```bash
  ros2 launch visual_tracking_my_robot track_ball.launch.py tune_detection:=true
  ```

- **Enable 3D ball tracking**:
  ```bash
  ros2 launch visual_tracking_my_robot track_ball.launch.py enable_3d_tracker:=true
  ```

- **Use simulated time**:
  ```bash
  ros2 launch visual_tracking_my_robot track_ball.launch.py use_sim_time:=true
  ```

## Dependencies
- [ROS 2](https://docs.ros.org/en/rolling/Installation.html)
- OpenCV (for image processing)
- A camera (e.g., webcam or Kinect) for input image stream
- Optionally, a depth camera for 3D tracking

## License
This project is licensed under the [MIT License](LICENSE).

## Contributors
- **Axel NIATO** - Lead Developer
