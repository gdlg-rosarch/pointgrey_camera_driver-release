# Script generated with Bloom
pkgdesc="ROS - Point Grey camera driver based on libflycapture2."
url='http://ros.org/wiki/pointgrey_camera_driver'

pkgname='ros-lunar-pointgrey-camera-driver'
pkgver='0.13.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('curl'
'dpkg'
'libraw1394'
'libusbx'
'ros-lunar-camera-info-manager'
'ros-lunar-catkin'
'ros-lunar-diagnostic-updater'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-exposure-msgs'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-roslaunch'
'ros-lunar-roslint'
'ros-lunar-sensor-msgs'
'ros-lunar-wfov-camera-msgs'
)

depends=('libraw1394'
'libusbx'
'ros-lunar-camera-info-manager'
'ros-lunar-diagnostic-updater'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-exposure-msgs'
'ros-lunar-image-proc'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-stereo-image-proc'
'ros-lunar-wfov-camera-msgs'
)

conflicts=()
replaces=()

_dir=pointgrey_camera_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/pointgrey_camera_driver $srcdir/pointgrey_camera_driver
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

