Name:           ros-indigo-pointgrey-camera-driver
Version:        0.11.0
Release:        0%{?dist}
Summary:        ROS pointgrey_camera_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pointgrey_camera_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       libraw1394-devel
Requires:       libusbx-devel
Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-driver-base
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-exposure-msgs
Requires:       ros-indigo-image-proc
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-wfov-camera-msgs
BuildRequires:  dpkg
BuildRequires:  libraw1394-devel
BuildRequires:  libusbx-devel
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-driver-base
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-exposure-msgs
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-wfov-camera-msgs

%description
Point Grey camera driver based on libflycapture2.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Nov 07 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.11.0-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.10.0-0
- Autogenerated by Bloom

