%define version	1.0.1
%define release	%mkrel 4

%define scim_version	1.4.0
%define prime_version	1.0.0.1

Name:		scim-prime
Summary:	SCIM IMEngine module for prime
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	http://sourceforge.jp/projects/scim-imengine/downloads/29156/%{name}-%{version}.tar.gz
Patch0:		scim-prime-1.0.1-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes:		%{_lib}scim-prime0
Requires:		prime >= %{prime_version}
Requires:		scim-client = %{scim_api}
BuildRequires:		prime-devel >= %{prime_version}
BuildRequires:		scim-devel >= 1.4.7-4mdk
BuildRequires:		automake, libltdl-devel

%description
Scim-prime is an SCIM IMEngine module for prime.
It supports Japanese input.

%prep
%setup -q

%build
autoreconf -fi
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

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun  -p /sbin/ldconfig
%endif


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir}/SetupUI/*.so
