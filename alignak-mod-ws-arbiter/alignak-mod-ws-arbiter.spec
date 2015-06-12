Name:		alignak-mod-ws-arbiter
Version:	ebae7950be9452ab80ec58575e9887d9b2a15d2a
Release:	1
Summary:	Alignak module for external commands trough HTTP

Group:		Network
License:	AGPLv3+
URL:		https://github.com/shinken-monitoring/mod-ws-arbiter
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

Requires:   alignak-common >= 2.0
Requires:   python-influxdb

%description
Alignak module for listening external commands from a web service 

%prep
%setup -qn mod-ws-arbiter-%{version}


%build


%install
rm -rf %{buildroot}/*

install -d %{buildroot}/usr/share/pyshared/alignak/modules/mod-ws-arbiter
install -pm07555 module/* %{buildroot}/usr/share/pyshared/alignak/modules/mod-ws-arbiter

install -d %{buildroot}/usr/share/doc/%{name}
install -pm0755 README.rst %{buildroot}/%{_docdir}/%{name}

install -d %{buildroot}/etc/alignak/modules
install -pm0755 etc/modules/* %{buildroot}/etc/alignak/modules


%files
/usr/share/pyshared/alignak/modules/mod-ws-arbiter
%config(noreplace) %{_sysconfdir}/alignak/modules/

%doc %{_docdir}/%{name}/*


%changelog
* Wed Jan 21 2015 Alexandre Viau <alexandre@alexandreviau.net> 2.7.3-1
- Initial Package