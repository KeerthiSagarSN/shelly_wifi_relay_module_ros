from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['shelly_wifi_relay_module_ros1'],
    package_dir={'': 'src'}
)

setup(**d)