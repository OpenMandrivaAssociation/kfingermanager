%define oname KFingerManager
%define svn_snapshot 1050414 

Summary:	Fingerprint Manager for KDE4
Name:		kfingermanager
Version:	0.0
Release:	0.%{svn_snapshot}.8
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		http://websvn.kde.org/trunk/playground/base/kfingerprint/KFingerManager/
Source0:	%{oname}-%{version}.%{svn_snapshot}.tar.bz2
Source1:	%{name}.po
Patch0:		kfingermanager-mdv-fix-category.patch
#Patch1:         KFingerManager-russian.patch
BuildRequires:	kdelibs4-devel

%description
Fingerprint Manager for KDE4.

%files
%lang(ru) %{_localedir}/ru/LC_MESSAGES/*
%{_kde_libdir}/kde4/kcm_kfingermanager.so
%{_kde_appsdir}/kfingermanager
%{_kde_datadir}/config/kfingerrc
%{_kde_datadir}/kde4/services/kfingermanager.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}
%patch0
#patch1 -p1
# cp %{SOURCE1} .

%build
%cmake_kde4
%make
pwd
msgfmt %{SOURCE1} -o kcmkfingermanager.mo
# msgfmt %{name}.po -o %{name}.mo

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_localedir}/ru/LC_MESSAGES/
install -m 644 build/kcmkfingermanager.mo %{buildroot}%{_localedir}/ru/LC_MESSAGES/

