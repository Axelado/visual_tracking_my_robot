from setuptools import setup
from glob import glob

package_name = 'visual_tracking_my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*launch.py')),
        ('share/' + package_name + '/params', glob('params/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Axel NIATO',
    maintainer_email='axelniato@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detect_ball = visual_tracking_my_robot.detect_ball:main',
            'detect_ball_3d = visual_tracking_my_robot.detect_ball_3d:main',
            'follow_ball = visual_tracking_my_robot.follow_ball:main',
        ],
    },
)
