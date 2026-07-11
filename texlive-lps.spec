%global tl_name lps
%global tl_revision 21322

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Class for Logic and Philosophy of Science
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lps
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lps.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The 'Logic and Philosophy of Science' journal is an online publication
of the University of Trieste (Italy). The class builds on the standard
article class to offer a format that LaTeX authors may use when
submitting to the journal.

