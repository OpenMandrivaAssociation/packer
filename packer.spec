%define debug_package %{nil}

Summary:	Cloud image build tool
Name:		packer
Version:	1.6.1
Release:	2
Source0:	https://github.com/hashicorp/packer/archive/v%{version}.tar.gz
License:	MPL 2.0
Group:		Servers
Url:		https://packer.io/
# Tarball containing go dependencies -- generated by (inside the source tree)
# running:
# export GOPATH=/tmp/GOPATH
# make dev
# cd /tmp
# tar cJf godeps-for-packer-%{version}.tar.xz GOPATH
Source1:	packer-%{version}-GOPATH.tar.xz
# If VersionPrerelease isn't set, "make dev" fails
Patch0:		packer-1.6.1-versionstring.patch
BuildRequires:	golang make
BuildRequires:	git-core

%description
Packer automates the creation of any type of cloud machine image.

%prep
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
%autosetup -p1 -a 1

%build
export GOPATH="`pwd`/GOPATH"
#export PATH="`pwd`/godeps/bin:$PATH"
#export GOPROXY="file://`pwd`/.godeps"
make dev

%install
install -c -D bin/packer %{buildroot}%{_bindir}/packer

%files
%{_bindir}/packer
