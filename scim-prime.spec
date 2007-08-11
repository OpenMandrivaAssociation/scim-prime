%define version	1.0.0
%define release	%mkrel 2

%define scim_version	1.4.0
%define prime_version	1.0.0.1

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-prime
Summary:	Scim-prime is an SCIM IMEngine module for prime
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:		prime >= %{prime_version}
Requires:		scim >= %{scim_version}
BuildRequires:		libprime >= %{prime_version}
BuildRequires:		scim-devel >= 1.4.7-4mdk
BuildRequires:		automake, libltdl-devel

%description
Scim-prime is an SCIM IMEngine module for prime.
It supports Japanese input.


%package -n	%{libname}
Summary:	Scim-prime library
Group:		System/Internationalization

%description -n %{libname}
scim-prime library.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./bootstrap

# temporary hack to fix ltmain.sh version
set -x
aclocal -I m4
autoheader
libtoolize -c --automake 
automake --add-missing --copy --include-deps
autoconf

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{scim_plugins_dir}/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so
