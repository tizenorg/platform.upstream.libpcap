Name:           libpcap
Version:        1.3.0
Release:        0
License:        BSD-3-Clause
Summary:        A Library for Network Sniffers
Url:            http://www.tcpdump.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch0:         libpcap-1.0.0-filter-fix.patch
Patch1:         libpcap-1.0.0-pcap-bpf.patch
Patch2:         libpcap-1.0.0-ppp.patch
Patch3:         libpcap-1.0.0-s390.patch
Patch4:         libpcap-ocloexec.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libusb-devel

%description
libpcap is a library used by packet sniffer programs. It provides an
interface for them to capture and analyze packets from network devices.
This package is only needed if you plan to compile or write such a
program yourself.

%package devel
Summary:        A Library for Network Sniffers
Group:          Development/Libraries/C and C++
Requires:       libpcap = %{version}

%description devel
libpcap is a library used by packet sniffer programs. It provides an
interface for them to capture and analyze packets from network devices.
This package is only needed if you plan to compile or write such a
program yourself.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4

%build
pic="pic"
autoreconf -fiv
export CFLAGS="%{optflags} -f$pic" CXXFLAGS="%{optflags} -f$pic"
%configure \
  --enable-ipv6
make %{?_smp_mflags} all shared

%install
mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} install install-shared

%docs_package

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_bindir}/pcap-config
%{_libdir}/*.so
%{_libdir}/*.*a

%changelog
