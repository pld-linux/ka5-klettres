#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		klettres
Summary:	klettres
Name:		ka5-%{kaname}
Version:	22.12.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	67716e777b7d80306fd42ab3ff7cc8b1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KLettres aims to help to learn the alphabet and then to read some
syllables in different languages. It is meant to help learning the
very first sounds of a new language, for children or for adults.

%description -l pl.UTF-8
Celem KLettres jest pomoc w nauce alfabetu i czytania różnych
sylab w różnych językach. Program ma pomagać uczyć się pierwszych
dźwięków nowego języka, przeznaczony jest zarówno dla dzieci
jak i dorosłych.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/org.kde.klettres.desktop
%{_datadir}/config.kcfg/klettres.kcfg
%{_iconsdir}/hicolor/128x128/apps/klettres.png
%{_iconsdir}/hicolor/16x16/apps/klettres.png
%{_iconsdir}/hicolor/22x22/apps/klettres.png
%{_iconsdir}/hicolor/32x32/apps/klettres.png
%{_iconsdir}/hicolor/48x48/apps/klettres.png
%{_iconsdir}/hicolor/64x64/apps/klettres.png
%{_datadir}/klettres
%{_datadir}/kxmlgui5/klettres
%{_datadir}/metainfo/org.kde.klettres.appdata.xml
%{_datadir}/qlogging-categories5/klettres.categories
%{_datadir}/knsrcfiles/klettres.knsrc
