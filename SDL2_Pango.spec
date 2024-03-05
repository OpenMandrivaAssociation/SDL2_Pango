
%define major   4

%define libname     %mklibname %{name}
%define develname   %mklibname %{name} -d

Summary:    Rendering of internationalized text for SDL2 (Simple DirectMedia Layer)
Name:       SDL2_Pango
Version:    2.1.5
Release:    1
License:    zlib
Group:      System/Libraries
URL:        https://github.com/markuskimius/SDL2_Pango
Source0:    https://github.com/markuskimius/SDL2_Pango/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(pango)

%description
Rendering of internationalized text for SDL2 (Simple DirectMedia Layer)

%package -n   %{libname}
Summary:      Main library for %{name}
Group:        System/Libraries
Obsoletes:    %{_lib}%{name}2.0_2 < 2.0.0-2

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n   %{develname}
Summary:      Headers for developing programs that will use %{name}
Group:        Development/C
Requires:     %{libname} = %{version}-%{release}
Provides:     lib%{name}-devel = %{version}-%{release}
Provides:     %{name}%{major}-devel = %{version}-%{release}
Provides:     %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{develname}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/SDL2_Pango.h
