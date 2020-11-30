%global debug_package %{nil}

Name: zfs-auto-snapshot
Version: 1.2.4
Release: 1%{?dist}
Summary: An alternative implementation of the zfs-auto-snapshot service for Linux that is compatible with zfs-linux and zfs-fuse.

Group: Development/Tools
License: GPL 2.0
URL: https://github.com/45drives/zfs-auto-snapshot
Source0: %{name}-%{version}.tar.gz

%description
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
mkdir -p %{buildroot}
mkdir -p %{buildroot}/etc/cron.{d,hourly,daily,weekly,monthly}
mkdir -p %{buildroot}/usr/local/share/man/man8/
mkdir -p %{buildroot}/usr/local/sbin/


pushd etc/
    cp -a zfs-auto-snapshot.cron.frequent %{buildroot}/etc/cron.d/zfs-auto-snapshot
    for i in hourly daily weekly monthly; do
        cp -a zfs-auto-snapshot.cron.$i %{buildroot}/etc/cron.$i/zfs-auto-snapshot
    done
popd

cp src/zfs-auto-snapshot.8 %{buildroot}/usr/local/share/man/man8/zfs-auto-snapshot.8
cp src/zfs-auto-snapshot.sh %{buildroot}/usr/local/sbin/zfs-auto-snapshot

%clean
rm -rf %{buildroot}

%files
/etc/cron.d/zfs-auto-snapshot
/etc/cron.hourly/zfs-auto-snapshot
/etc/cron.daily/zfs-auto-snapshot
/etc/cron.weekly/zfs-auto-snapshot
/etc/cron.monthly/zfs-auto-snapshot
%doc /usr/local/share/man/man8/zfs-auto-snapshot.8
/usr/local/sbin/zfs-auto-snapshot


%changelog
* Mon Nov 30 2020 Brett Kelly <bkelly@45drives.com> 1.2.4
- first build of zfs-auto-snapshot

