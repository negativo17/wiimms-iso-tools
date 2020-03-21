Name:           wiimms-iso-tools
Version:        3.02a
Release:        1%{?dist}
Summary:        Tools for manipulating Wii/Gamecube games

License:        GPLv2+
URL:            http://wit.wiimm.de/

Source0:        https://download.wiimm.de/source/%{name}/%{name}.source-%{version}.txz
Source1:        README.Fedora
Patch0:         %{name}-cflags.patch
#Patch1:         %{name}-system-bzip2.patch

#BuildRequires:  bzip2-devel
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
Wiimms ISO Tools is a set of command line tools to manipulate Wii/GameCube ISO
images and WBFS containers.

%prep
%autosetup -p1 -n %{name}.source-%{version}
cp %{SOURCE1} .

# Remove bundled bzip2
#rm -fr src/libbz2

%build
%make_build INSTALL_PATH=%{_prefix} all

%install
mkdir -p %{buildroot}%{_sharedstatedir}/wit
mkdir -p %{buildroot}%{_bindir}

install -m 755 wdf wit wwt wfuse %{buildroot}%{_bindir}
ln -sf wdf %{buildroot}%{_bindir}/wdf-cat
ln -sf wdf %{buildroot}%{_bindir}/wdf-dump

install -p -m 644 share/*.txt %{buildroot}%{_sharedstatedir}/wit
install -p -m 755 setup/load-titles.sh %{buildroot}%{_sharedstatedir}/wit

%files
%doc README.Fedora
%{_bindir}/wdf
%{_bindir}/wdf-cat
%{_bindir}/wdf-dump
%{_bindir}/wfuse
%{_bindir}/wit
%{_bindir}/wwt
%{_sharedstatedir}/wit

%changelog
* Sat Mar 21 2020 Simone Caronni <negativo17@gmail.com> - 3.02a-1
- Update to 3.02a.
- Trim changelog.
- Rename to wiimms-iso-tools.

* Wed Jan 11 2017 Simone Caronni <negativo17@gmail.com> - 2.40a-1
- Update to latest 2.40a.
