Name:           ros-indigo-urdfdom-py
Version:        0.3.3
Release:        1%{?dist}
Summary:        ROS urdfdom_py package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/urdf_parser_py
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       python-lxml
Requires:       ros-indigo-catkin
BuildRequires:  python-catkin_pkg
BuildRequires:  python-devel
BuildRequires:  ros-indigo-catkin

%description
Python implementation of the URDF parser.

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
* Fri Feb 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 0.3.3-1
- Autogenerated by Bloom

* Fri Feb 10 2017 Chris Lalancette <clalancette@osrfoundation.org> - 0.3.3-0
- Autogenerated by Bloom

* Mon Feb 22 2016 Ioan Sucan <isucan@google.com> - 0.3.1-1
- Autogenerated by Bloom

* Mon Feb 22 2016 Ioan Sucan <isucan@google.com> - 0.3.1-0
- Autogenerated by Bloom

