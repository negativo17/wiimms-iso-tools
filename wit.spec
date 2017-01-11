%global revision 7331

Name:           wit
Version:        2.40a
Release:        1%{?dist}
Summary:        Tools for manipulating Wii/Gamecube games

License:        GPLv2+
URL:            http://wit.wiimm.de/

Source0:        wit-%{revision}svn.tar.bz2
Source1:        README.Fedora
Source99:       %{name}-svn-checkout.sh
Patch0:         %{name}-cflags.patch
Patch1:         %{name}-system-bzip2.patch

#BuildRequires:  bzip2-devel
BuildRequires:  fuse-devel

%description
Wiimms ISO Tools is a set of command line tools to manipulate Wii/GameCube ISO
images and WBFS containers.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .cflags
cp %{SOURCE1} .
# Set correct revision without using svn:
sed -i -e 's/revision=0/revision=%{revision}/g' setup.sh

# Remove bundled bzip2
#rm -fr src/libbz2 src/lib-bzip2.c
#patch1 -p1 -b .system-bzip2

%build
make %{?_smp_mflags} \
    INSTALL_PATH=%{_prefix} \
    SHARE_PATH=%{_sharedstatedir}/wit \
    all

%install
mkdir -p %{buildroot}%{_sharedstatedir}/wit
mkdir -p %{buildroot}%{_bindir}
install -m 755 wdf wit wwt wfuse %{buildroot}%{_bindir}
ln -sf wdf %{buildroot}%{_bindir}/wdf-cat
ln -sf wdf %{buildroot}%{_bindir}/wdf-dump
install -p -m 644 share/*.txt %{buildroot}%{_sharedstatedir}/wit
install -p -m 755 load-titles.sh %{buildroot}%{_sharedstatedir}/wit

%files
%doc WDF.txt README.Fedora
%{_bindir}/wdf
%{_bindir}/wdf-cat
%{_bindir}/wdf-dump
%{_bindir}/wfuse
%{_bindir}/wit
%{_bindir}/wwt
%{_sharedstatedir}/wit

%changelog
* Wed Jan 11 2017 Simone Caronni <negativo17@gmail.com> - 2.40a-1
- Update to latest 2.40a.

* Fri Jan 08 2016 Simone Caronni <negativo17@gmail.com> - 2.31a-1
- Update to 2.31a.

* Wed Jan 07 2015 Simone Caronni <negativo17@gmail.com> - 2.30a-1.5771svn
- Update to 2.30a (SVN revision 5771).
- Remove subversion working copy (to avoid metadata upgrades):
  http://subversion.apache.org/docs/release-notes/1.7.html#wc-ng
- Remove subversion build requirement.
- Set code revision in spec file instead of using subversion on the checkout.

* Fri Apr 11 2014 Simone Caronni <negativo17@gmail.com> - 2.28a-1.4980svn
- Update to 2.28a.

* Sun Feb 09 2014 Simone Caronni <negativo17@gmail.com> - 2.27a-1.4908svn
- Update to 2.27a.

* Tue Jan 21 2014 Simone Caronni <negativo17@gmail.com> - 2.25a-1.4825svn
- Updated to 4825svn.

* Sun Jul 21 2013 Simone Caronni <negativo17@gmail.com> - 2.23a-1.4534svn
- Updated to 2.23a.
- Remove non-working EPEL 5 support.

* Wed May 01 2013 Simone Caronni <negativo17@gmail.com> - 2.20a-1.4399svn
- Updated to 2.20a.

* Wed Apr 03 2013 Simone Caronni <negativo17@gmail.com> - 2.13a-2.4298svn
- Update to 2.13a.

* Fri Mar 15 2013 Simone Caronni <negativo17@gmail.com> - 2.12a-2.4272svn
- Update to 2.12a.

* Wed Feb 13 2013 Simone Caronni <negativo17@gmail.com> - 2.11a-2.4233svn
- Update to 2.11a.
- Remove %%{_isa} from BuildRequires.

* Tue Feb 12 2013 Simone Caronni <negativo17@gmail.com> - 2.10a-2.4118svn
- Use system bzip2.
- Use macros everywhere in spec file.

* Fri Oct 19 2012 Simone Caronni <negativo17@gmail.com> - 2.10a-1.4118svn
- Updated.

* Thu Sep 06 2012 Simone Caronni <negativo17@gmail.com> - 2.08a-1.4027svn
- Updated to 2.08a.

* Fri Jul 20 2012 Simone Caronni <negativo17@gmail.com> - 2.06a-1.3955svn
- Updated to 2.07a.

* Mon Jun 18 2012 Simone Caronni <negativo17@gmail.com> - 2.06a-1.3832svn
- Updated to 2.06a.

* Wed May 16 2012 Simone Caronni <negativo17@gmail.com> - 2.05b-2.3611svn
- Updated to 2.05b.
- Add RPM_OPT_FLAGS to make command.
- Remove install macro.
- Require svn >= 1.7 (Fedora 17+)

* Mon Apr 16 2012 Simone Caronni <negativo17@gmail.com> - 2.05a-1.3591svn
- Updated to 2.05a.

* Sat Mar 17 2012 Simone Caronni <negativo17@gmail.com> - 2.04a-1.3554svn
- Updated to 2.04a.
- Updated README.Fedora with examples.

* Wed Feb 15 2012 Simone Caronni <negativo17@gmail.com> - 2.03a-3.3309svn
- Update to 2.03a.
- Removed suid on wwt, added titles support.
- Added README.Fedora with examples.

* Wed Oct 26 2011 Simone Caronni <negativo17@gmail.com> - 2.00b-2.2855svn
- rpmlint fixes.

* Wed Oct 26 2011 Simone Caronni <negativo17@gmail.com> - 2.00b-2.2855svn
- rpmlint fixes.

* Tue Oct 25 2011 Simone Caronni <negativo17@gmail.com> - 2.00b-1.2855svn
- Updated.

* Tue Mar 15 2011 Simone Caronni <negativo17@gmail.com> - 1.28a-1.2356svn
- Updated.

* Thu Dec 16 2010 Simone Caronni <negativo17@gmail.com> - 1.23-1.2103svn
- First build.

