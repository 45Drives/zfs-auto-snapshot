Name: zfs-auto-snapshots
Version: 1.2.4
Release: 1%{?dist}
Summary: An alternative implementation of the zfs-auto-snapshot service for Linux
that is compatible with zfs-linux and zfs-fuse.

Group: Development/Tools
License: GPL 2.0
URL: https://github.com/45drives/zfs-auto-snapshot
Source0: %{name}-%{version}.tar.gz

%description
An alternative implementation of the zfs-auto-snapshot service for Linux
that is compatible with zfs-linux and zfs-fuse.

Automatically create, rotate, and destroy periodic ZFS snapshots. This is
the utility that creates the @zfs-auto-snap_frequent, @zfs-auto-snap_hourly,
@zfs-auto-snap_daily, @zfs-auto-snap_weekly, and @zfs-auto-snap_monthly
snapshots if it is installed.

This program is a posixly correct bourne shell script.  It depends only on
the zfs utilities and cron, and can run in the dash shell.

%prep
%setup -q

%build
# empty

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%make_install

%clean
rm -rf %{buildroot}

%files
/etc/cron.d/zfs-auto-snapshot
/etc/cron.hourly/zfs-auto-snapshot
/etc/cron.daily/zfs-auto-snapshot
/etc/cron.weekly/zfs-auto-snapshot
/etc/cron.monthly/zfs-auto-snapshot
%doc /usr/local/share/man/man8/zfs-auto-snapshot.8
%{_bindir}/zfs-auto-snapshot


%changelog
* Mon Nov 30 2020 Brett Kelly <bkelly@45drives.com> 1.2.4
- first build of zfs-auto-snapshot