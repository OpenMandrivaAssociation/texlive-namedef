Name:		texlive-namedef
Version:	55881
Release:	1
Summary:	TeX definitions with named parameters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/namedef
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namedef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namedef.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namedef.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a prefix \named to be used in TeX
definitions so that parameters can be identified by their name
rather than by number, giving parameters a semantic rather than
syntactic meaning, making it easy to understand long
definitions. A usual definition reads: \def\SayHello#1{Hello,
#1!} but with namedef you can replace #1 by, say, #[person]:
\named\def\SayHello#[person]{Hello, #[person]!} and \named will
figure out the numbering of the parameters for you.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/namedef
%{_texmfdistdir}/tex/generic/namedef
%doc %{_texmfdistdir}/doc/generic/namedef

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
