Summary:	Enhanced version of SuperTux Game
Summary(pl.UTF-8):	Rozbudowana wersja gry SuperTux
Name:		supertux2
Version:	0.3.3
Release:	0.5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/supertux/supertux-%{version}.tar.bz2
# Source0-md5:	f3f803e629ee51a9de0b366a036e393d
Source1:	supertux2.sh
# Source1-md5:	3eb2c5eebde638baded293419592e7c0
URL:		http://super-tux.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	OpenAL-devel
BuildRequires:	physfs-devel
BuildRequires:	boost-devel
BuildRequires:	glew-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Super Mario Bros style game starring Tux the penguin.

%description -l pl.UTF-8
Gra w stylu Super Mario Bros z pingwinem Tuksem w roli głównej.

%prep
%setup -qn supertux-%{version}

%build
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX='/usr'
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT/usr/share/pixmaps/supertux{,2}.xpm
mv $RPM_BUILD_ROOT/usr/share/pixmaps/supertux{,2}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHATSNEW.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/games/supertux2
%dir /usr/share/doc/supertux2
/usr/share/applications/supertux2.desktop
/usr/share/doc/supertux2/*
/usr/share/games/supertux2
/usr/share/pixmaps/supertux2.*
