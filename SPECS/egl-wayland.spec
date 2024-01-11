Name:           egl-wayland
Version:        1.1.9
Release:        3%{?dist}
Summary:        Wayland EGL External Platform library

License:        MIT
URL:            https://github.com/NVIDIA/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        10_nvidia_wayland.json
Source2:        15_nvidia_gbm.json
Patch0:         %url/commit/d4937adc5cd04ac7df98fc5616e40319fb52fdee.patch
Patch1:         %url/commit/daab8546eca8428543a4d958a2c53fc747f70672.patch
Patch2:         %url/commit/582b2d345abaa0e313cf16c902e602084ea59551.patch

BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  eglexternalplatform-devel
%if 0%{?fedora}
BuildRequires:  cmake
BuildRequires:  libglvnd-devel >= 1.3.4
%else
BuildRequires:  cmake3
BuildRequires:  mesa-libEGL-devel
%endif
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
Wayland EGL External Platform library

%package devel
Summary:        Wayland EGL External Platform library development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Wayland EGL External Platform library development package

%prep
%autosetup -p1
%if 0%{?rhel}
sed -i -e 's@>= 0.50@>= 0.47@g'  meson.build
%endif

%build
%meson
%meson_build


%install
%meson_install
install -m 0755 -d %{buildroot}%{_datadir}/egl/egl_external_platform.d/
install -pm 0644 %{SOURCE1} %{SOURCE2} %{buildroot}%{_datadir}/egl/egl_external_platform.d/
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json

%files devel
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/

%changelog
* Tue Nov 23 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-3
- Add upstream commits

* Sat Oct 16 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-2
- Add 15_nvidia_gbm.json

* Fri Oct 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-1
- Update to 1.1.9

* Fri Sep 17 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Fri May   7 2021 Olivier Fourdan <ofourdan@redhat.com> - 1.1.6-3
- Fix EGL stream closing causing a crash in Xwayland with EGLstream
  (#1943936, #1949415)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.6-1
- Update to 1.1.6

* Fri Aug 14 2020 Leigh Scott <leigh123linux@gmail.com> - 1.1.5-3
- Add upstream patch to address rhbz#1842473

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1.1.5-1
- Update to 1.1.5

* Mon Mar 30 2020 leigh123linux <leigh123linux@googlemail.com> - 1.1.4-4
- Use upstream commit to address missing mesa includes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Leigh Scott <leigh123linux@gmail.com> - 1.1.4-2
- Add patch to add missing mesa includes

* Sun Sep 15 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-1
- Update to 1.1.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.3-1
- Update to 1.1.3

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.2-3
- Rebuild with Meson fix for #1699099

* Sat Mar 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.2-2
- Switch to upstream fix

* Fri Feb 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.2-1
- Update to 1.1.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-3
- Fix the same crappy warning f28 generates

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-2
- Fix the crappy warning epel7 generates

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Nov 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-0.2.20181015git0eb29d4
- Update to latest git snapshot (rhbz#1653118)

* Mon Aug 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-0.1.20180916git1676d1d
- Update to 1.1.0 snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-0.2.20180626git395ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.5-0.1.20180626git395ce9f
- Update to 1.0.5 snapshot

* Sat Jun 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-0.1.20180602git4ab0873
- Update to 1.0.4 snapshot

* Tue Feb 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.3-2.20180201git6f5f7d0
- Update to latest git snapshot
- Switch to meson
- Install .so file to -devel as it's listed in wayland-eglstream.pc
- Fix directory ownership

* Wed Jan 31 2018 Jonas Ådahl <jadahl@redhat.com> - 1.0.3-1.20180111gitb283689
- Update to 1.0.3
- Add -devel package

* Thu Aug 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-0.4.20170802git1f4b1fd
- Update to latest git snapshot

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.3.20170628git818b613
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.2.20170628git818b613
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-0.1.20170628git818b613
- Update to 1.0.2 git

* Wed Mar 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-0.1.20170308git582fbf3
- Update to 1.0.1 git

* Tue Feb 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.7.20170207git05eb000
- Add license file

* Thu Feb 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.6.20170120git743d702
- Add requires libglvnd-egl
- Make review changes

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.5.20170120git743d702
- Drop devel sub-package

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.4.20170120git743d702
- Add 10_nvidia_wayland.json to libs sub-package

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.3.20170120git743d702
- Add loader directory to common sub-package
- Move libs to sub-package

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.2.20170120git743d702
- Add date to release

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.1.git743d702
- First build

