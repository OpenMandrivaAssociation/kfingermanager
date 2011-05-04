%define oname KFingerManager
%define svn_snapshot 1050414 

Summary:	Fingerprint Manager for KDE4
Name:	  	kfingermanager
Version:	0.0
Release:	%mkrel 0.%svn_snapshot.4
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	%oname-%version.%svn_snapshot.tar.bz2
Patch0:		kfingermanager-mdv-fix-category.patch
URL:		http://websvn.kde.org/trunk/playground/base/kfingerprint/KFingerManager/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel

%description
Fingerprint Manager for KDE4

%files -f %name.lang
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_kfingermanager.so
%_kde_appsdir/kfingermanager
%_kde_datadir/config/kfingerrc
%_kde_datadir/kde4/services/kfingermanager.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %oname
%patch0 

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
