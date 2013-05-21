%define oname KFingerManager
%define svn_snapshot 1050414 

Summary:	Fingerprint Manager for KDE4
Name:		kfingermanager
Version:	0.0
Release:	0.%{svn_snapshot}.5
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://websvn.kde.org/trunk/playground/base/kfingerprint/KFingerManager/
Source0:	%{oname}-%{version}.%{svn_snapshot}.tar.bz2
Patch0:		kfingermanager-mdv-fix-category.patch
BuildRequires:	kdelibs4-devel

%description
Fingerprint Manager for KDE4.

%files
%{_kde_libdir}/kde4/kcm_kfingermanager.so
%{_kde_appsdir}/kfingermanager
%{_kde_datadir}/config/kfingerrc
%{_kde_datadir}/kde4/services/kfingermanager.desktop

#--------------------------------------------------------------------

%prep
%setup -qn %{oname}
%patch0 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

