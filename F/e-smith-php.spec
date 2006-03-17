Summary: e-smith specific PHP configuration and templates.
%define name e-smith-php
Name: %{name}
%define version 1.12.0
%define release 01
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base, php >= 4.0.1
Requires: e-smith-lib >= 1.15.1-16
BuildRequires: e-smith-devtools >= 1.11.0-12
AutoReqProv: no

%changelog
* Fri Mar 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Mon Jan 30 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.0-10
- Remove all pre/post/preun/postun scriptlets. [SME: 469]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-09
- Bump release number only

* Tue Oct 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-08]
- Prevent i-bay name aliasing in default open_basedir restriction.
  [SF: 1330228]

* Tue Sep  6 2005 Tony Clayton <apc@e-smith.com>
- [1.11.0-07]
- Turn register_globals off by default [SF: 1271218]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-06]
- Update to current db access APIs, in readiness for move of dbs to private
  directory. [SF: 1216546 (Shad)]

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-05]
- Update include_path in php.ini, to base and add-on pear directories.

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Use generic_template_expand action to expand /etc/php.ini.
  Add e-smith-lib dependency. Add e-smith-devtools dependency. [MN00064130]
- Remove anachronisms in /etc/php.ini templates.
- Fix loss of AllowUrlFopen property during post-install. [MN00064752]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Convert apache config fragments to apache2 format. [charlieb MN00051144]

* Fri Nov  5 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Remove specification of dynamic extensions, as that is done with newer
  php via /etc/php.d/.  [charlieb MN00051515]
- Replace deprecated Copyright header with License header.
- Remove bogus WARNING text from spec file. [charlieb]

* Mon Jan 26 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-01]
- rolling to dev - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-13]
- Fixed a typo in the previous version. [msoulier 8852]

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-12]
- Wrappered the restart of the e-smith web server so that it is conditional on
  e-smith-apache being installed. [msoulier 8852]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-11]
- Remembered that we can't query the rpm database during rpm installs.
  [msoulier 8852]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-10]
- Wrappered the restart of the e-smith web server so that it is conditional on
  e-smith-apache being installed. [msoulier 8852]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-09]
- Added a type default fragment. [msoulier 3299]

* Wed Apr 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-08]
- Increase limits to allow webmail attachments of 10MB, rather than 2MB
  MemoryLimit 8M -> 32M, PostMaxSize 8M -> 20M, UploadMaxFilesize 2M -> 10M [gordonr 8478]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-07]
- set allow_url_fopen = Off by default, tunable in config db [gordonr 4970]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-06]
- And back out last change - not a bug [gordonr 7836]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-05]
- Fix include_path in php.ini [gordonr 7836]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-04]
- Update more httpd.conf fragments to new interface [gordonr 7600]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-03]
- Update httpd.conf fragment to new interface [gordonr 7600]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-02]
- Adding .phtml extension. [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-01]
- rolling to development stream to 1.9.0

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-05]
- Backing out changes since 1.8.0-01, as they belong in a development stream.
  [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-04]
- Fixed a syntax error that I should have caught before committing the last
  version. [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-03]
- Bringing the api up to the modern version. [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-02]
- Added index.phtml to the DirectoryIndex directive, and made the code a
  little nicer to look at. [msoulier 6543]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Mon Jul 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Add conf-php link to bootstrap-console-save event [charlieb 1939]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to development stream number to 1.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.5-01]
- RPM rebuild forced by cvsroot2rpm

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.4-01]
- Turned off display_errors, use error_log -> syslog instead, as per
  Dan Brown's PHP upgrade HOWTO
- Tidied up formatting in that fragment [gordonr 3019]

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.3-01]
- Imported into CVS

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.1-01]
- rollRPM: Rolled version number to 1.5.1-01. Includes patches up to 1.5.0-03.

* Mon Feb 04 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-03]
- Remove all comments from php.ini template fragments.
- Allow some resource limits to be set by properties of the php service
  in the config db.

* Mon Feb 04 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Template /etc/php.ini, and expand template during conf-php action.
- Make some simplifications to the conf-php script, and remove a 
  potential error case (php is not in config db and event is neither
  post-install or post-upgrade).

* Mon Feb 4 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- rollRPM: Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-03.

* Thu Sep 6 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-03]
- Restrict PHP programs residing in an i-bay to only be able to open files
  which reside in the same i-bay. An i-bay property PHPBaseDir is available
  to override this restriction.

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-02.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Load PHP modules late, not first. This corrects a compatibility problem
  with RedHat 7.1 RPMS.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-05.

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-05]
- Changed license to GPL

* Fri Mar 23 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-04]
- Disable PHP MIME type by default
- Enable PHP MIME type for each i-bay for which dynamic content is enabled.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-03]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- changed action to run at 50, instead of 55.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-10.

* Wed Jan 17 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-10]
- PHP is enabled by default.

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-9]
- rolling to 9, 8 is missing.
- pulling expand httpd.conf, we'll leave conf-httpd
  to do it.

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-8]
- pulled restarting apache - just expand httpd.conf

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-7]
- apache now restarts whenever php's status changes

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-6]
- expand httpd.conf template from conf-php

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-5]
- add apache restart code to conf-php

* Sat Jan  6 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-4]
- Only run %post actions in runlevel 7

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-3]
- put createlinks back in.

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-2]
- expand PHP httpd.conf fragments conditionally based on
  service status.
- add PHP to the services database and default to disabled.

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-1]
- Rolled version to 1.1.0-1. Inlcudes patches up to 0.1-1.

* Tue Nov 14 2000 Adrian Chung <adrianc@e-smith.com>
- initial release

%description
This package adds necessary e-smith template fragments to enable
php specific configuration items.

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
