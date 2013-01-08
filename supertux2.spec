
%define 	gitdate	20130107
Summary:	Enhanced version of SuperTux Game
Summary(pl.UTF-8):	Rozbudowana wersja gry SuperTux
Name:		supertux2
Version:	0.3.3
Release:	%{gitdate}.1
License:	GPL
Group:		X11/Applications/Games
# Source0: supertux2-git-20130107.tar.bz2 created @20130107
# git clone https://code.google.com/p/supertux/
# cd supertux
# git archive --format=tar HEAD | bzip2 -9 > supertux2-git-20130107.tar.bz2
Source0:	http://files.guevara.pl/%{name}-git-20130107.tar.bz2
# Source0-md5:	925f8e6d9eb6793d1a68e1563f8e7bd2
Source1:	%{name}.sh
URL:		http://supertux.lethargik.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.4
BuildRequires:	SDL_image-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	glew-devel
BuildRequires:	physfs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
SuperTux 2 is a classic 2D jump'n run sidescroller game in a style
similar to the original Super Mario.

%description -l pl.UTF-8
SuperTux 2 to gra w stylu Super Mario Bros z pingwinem Tuksem w roli
głównej.

%prep
%setup -q -cn %{name}-%{version}

%build
mkdir -p build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX='%{_prefix}'
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
# supertux.xpm is provided by supertux pkg
mv $RPM_BUILD_ROOT%{_pixmapsdir}/supertux.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHATSNEW.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_prefix}/games/supertux2
%dir %{_docdir}/supertux2
%{_desktopdir}/supertux2.desktop
%{_docdir}/supertux2/*
%{_datadir}/games/supertux2
%{_pixmapsdir}/*

