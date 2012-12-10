%define name fireflies
%define version 2.07
%define release %mkrel 10

Summary: Colourful OpenGL screensaver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://somewhere.fscked.org/fireflies/%{name}-%{version}.tar.bz2
Patch: fireflies-2.07-gcc4.3.patch
Patch1: libgfx-fltk-header.patch
Patch2: fireflies-2.07-missing-header.patch
URL: http://somewhere.fscked.org/fireflies/
License: GPL
Group: Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libmesaglu-devel
BuildRequires: SDL-devel
BuildRequires: libx11-devel
Requires: xscreensaver >= 4.12

%description
Fireflies is an OpenGL screensaver for Linux (using xscreensaver) and
Windows. It also works as a standalone program, which allows you to
move and rotate the camera. Swarms of bugs fly around the screen
leaving colorful translucent trails that get blown around by the wind.

%prep
%setup -q
tar xzf libgfx*
%patch -p1
%patch1 -p0
%patch2 -p1

%build
cd libgfx && %configure2_5x && cd src && %make
cd ../..
%configure2_5x
%make OPT_LIBS=-lX11

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


%changelog
* Tue Feb 07 2012 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-10mdv2012.0
+ Revision: 771576
- fix linking
- rebuild

* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 2.07-9
+ Revision: 635415
- tighten BR

* Tue Jul 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-8mdv2011.0
+ Revision: 401462
- fix build

* Sun Jul 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-7mdv2009.0
+ Revision: 250686
- fix libgfx build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-4mdv2008.0
+ Revision: 55224
- Import fireflies



* Thu Jul 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-4mdk
- Rebuild

* Wed May 24 2006 Götz Waschk <waschk@mandriva.org> 2.07-3mdk
- fix conflict with xscreensaver

* Wed May 24 2006 Götz Waschk <waschk@mandriva.org> 2.07-2mdk
- new X

* Sun May  7 2006 Götz Waschk <waschk@mandriva.org> 2.07-1mdk
- drop patch
- New release 2.07
- use mkrel

* Fri May  6 2005 Götz Waschk <waschk@mandriva.org> 2.06-5mdk
- fix build on x86_64

* Thu Dec 16 2004 Götz Waschk <waschk@linux-mandrake.com> 2.06-4mdk
- update vroot.h to fix bug 12702

* Fri Jun  4 2004 Götz Waschk <waschk@linux-mandrake.com> 2.06-3mdk
- fix buildrequires
- source URL
- new g++

* Fri Aug 15 2003 Götz Waschk <waschk@linux-mandrake.com> 2.06-2mdk
- requires latest xscreensaver package
- remove the xml file merged into xscreensaver

* Tue Jun 24 2003 Götz Waschk <waschk@linux-mandrake.com> 2.06-1mdk
- new version
- enable fullscreen mode

* Thu Apr 17 2003 Götz Waschk <waschk@linux-mandrake.com> 2.03-1mdk
- new version

* Tue Mar 11 2003 Götz Waschk <waschk@linux-mandrake.com> 2.02-2mdk
- fix buildrequires

* Mon Mar 10 2003 Götz Waschk <waschk@linux-mandrake.com> 2.02-1mdk
- fix build
- new version

* Mon Feb 24 2003 Götz Waschk <waschk@linux-mandrake.com> 2.0-1mdk
- initial package
