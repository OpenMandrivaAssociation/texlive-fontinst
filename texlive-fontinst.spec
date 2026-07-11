%global tl_name fontinst
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.933
Release:	%{tl_revision}.1
Summary:	Help with installing fonts for TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/fontinst
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontinst.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fontinst.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX macros for converting Adobe Font Metric files to TeX metric and
virtual font format. Fontinst helps mainly with the number crunching and
shovelling parts of font installation. This means in practice that it
creates a number of files which give the TeX metrics (and related
information) for a font family that (La)TeX needs to do any typesetting
in these fonts. Fontinst furthermore makes it easy to create fonts
containing glyphs from more than one base font, taking advantage of
(e.g.) "expert" font sets. Fontinst cannot examine files to see if they
contain any useful information, nor automatically search for files or
work with binary file formats; those tasks must normally be done
manually or with the help of some other tool, such as the pltotf and
vptovf programs.

