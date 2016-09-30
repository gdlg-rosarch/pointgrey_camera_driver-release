Name:           ros-indigo-pointgrey-camera-driver
Version:        0.12.2
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
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-exposure-msgs
Requires:       ros-indigo-image-proc
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-wfov-camera-msgs
BuildRequires:  curl
BuildRequires:  dpkg
BuildRequires:  libcurl-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libusbx-devel
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-updater
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
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Sep 30 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.12.2-0
- Autogenerated by Bloom

* Wed Dec 09 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.12.1-1
- Autogenerated by Bloom

* Fri Nov 06 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.12.1-0
- Autogenerated by Bloom

