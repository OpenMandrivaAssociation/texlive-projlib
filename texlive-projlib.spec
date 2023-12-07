Name:		texlive-projlib
Version:	68784
Release:	1
Summary:	A series of tools to simplify your workflow
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/projlib
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/projlib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/projlib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/projlib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ProjLib is a collection of tools to help you write LaTeX
documents. With the main package ProjLib loaded, you no longer
need to set up the theorem-like environments, nor to manually
configure the appropriate multilingual settings. In addition, a
series of auxiliary functionalities are introduced.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/projlib
%{_texmfdistdir}/tex/latex/projlib
%doc %{_texmfdistdir}/doc/latex/projlib

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
