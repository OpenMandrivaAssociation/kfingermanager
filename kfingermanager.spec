%define oname KFingerManager
%define svn_snapshot 1050414 

Summary:	Fingerprint Manager for KDE4
Name:		kfingermanager
Version:	0.0
Release:	0.%{svn_snapshot}.5
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		http://websvn.kde.org/trunk/playground/base/kfingerprint/KFingerManager/
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
%setup -q -n %{oname}
%patch0 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1050414.4mdv2011.0
+ Revision: 666027
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0-0.1050414.3mdv2011.0
+ Revision: 606263
- rebuild

  + John Balcaen <mikala@mandriva.org>
    - Add a patch to fix category for systemsettings

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.1050414.1mdv2010.1
+ Revision: 466896
- import kfingermanager

