Name:		fonts-ttf-comic-relief
Version:	1.0
Release:	1
Summary:	Comic Relief ttf fonts
License:	SIL Open Font License v1.10
Group:		System/Fonts/True type
Url:		https://loudifier.com
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Comic Relief is an alternative to Comic Sans

%files
%dir %{_datadir}/fonts/TTF/comic-relief/
%{_datadir}/fonts/TTF/comic-relief/*

%prep
%setup -qn %{name}-%{version}/fonts/TTF/comic-relief/

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/comic-relief
install -Dm 644  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/comic-relief/
