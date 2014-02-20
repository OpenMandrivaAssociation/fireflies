%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Colourful OpenGL screensaver
Name:		fireflies
Version:	2.07
Release:	12
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://somewhere.fscked.org/fireflies/
Source0:	http://somewhere.fscked.org/fireflies/%{name}-%{version}.tar.bz2
Patch0:		fireflies-2.07-gcc4.3.patch
Patch1:		libgfx-fltk-header.patch
Patch2:		fireflies-2.07-missing-header.patch
Patch3:		fireflies-2.07-libgfx-libpng15.patch
Patch4:		fireflies-2.07-libgfx-libpng16.patch
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
Requires:	xscreensaver

%description
Fireflies is an OpenGL screensaver for Linux (using xscreensaver) and
Windows. It also works as a standalone program, which allows you to
move and rotate the camera. Swarms of bugs fly around the screen
leaving colorful translucent trails that get blown around by the wind.

%files
%doc README ChangeLog
%{_libexecdir}/xscreensaver/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q
tar xzf libgfx*
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p0

%build
cd libgfx
%configure2_5x
cd src
%make
cd ../..
%configure2_5x
%make OPT_LIBS=-lX11

%install
install -D -m 755 src/%{name} %{buildroot}%{_libexecdir}/xscreensaver/%{name}

