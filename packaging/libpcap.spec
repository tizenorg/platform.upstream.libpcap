Name:           libpcap
Version:        1.3.0
Release:        0
License:        BSD-3-Clause
Summary:        A Library for Network Sniffers
Url:            http://www.tcpdump.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
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

%build
pic="pic"
autoreconf -fiv
export CFLAGS="%{optflags} -f$pic" CXXFLAGS="%{optflags} -f$pic"
%configure \
  --enable-ipv6
make %{?_smp_mflags} all shared

%install
%make_install

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
