%define name fireflies
%define version 2.07
%define release %mkrel 6

Summary: Colourful OpenGL screensaver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://somewhere.fscked.org/fireflies/%{name}-%{version}.tar.bz2
URL: http://somewhere.fscked.org/fireflies/
License: GPL
Group: Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libmesaglut-devel
BuildRequires: SDL-devel
BuildRequires: X11-devel
Requires: xscreensaver >= 4.12

%description
Fireflies is an OpenGL screensaver for Linux (using xscreensaver) and
Windows. It also works as a standalone program, which allows you to
move and rotate the camera. Swarms of bugs fly around the screen
leaving colorful translucent trails that get blown around by the wind.

%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%_libdir
%make CXX="g++ $LDFLAGS -DHAVE_GLX" 

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 src/%name %buildroot%_libexecdir/xscreensaver/%name
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%_libexecdir/xscreensaver/%name
# already in xscreensaver
#%{_datadir}/xscreensaver/config/fireflies.xml
