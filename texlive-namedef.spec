%global tl_name namedef
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	TeX definitions with named parameters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/namedef
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/namedef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/namedef.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/namedef.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(l3kernel)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a prefix \named to be used in TeX definitions so
that parameters can be identified by their name rather than by number,
giving parameters a semantic rather than syntactic meaning, making it
easy to understand long definitions. A usual definition reads:
\def\SayHello#1{Hello, #1!} but with namedef you can replace #1 by, say,
#[person]: \named\def\SayHello#[person]{Hello, #[person]!} and \named
will figure out the numbering of the parameters for you.

