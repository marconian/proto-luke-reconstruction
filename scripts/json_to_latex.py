#!/usr/bin/env python3
"""
JSON to LaTeX Converter for Proto-Luke Gospel
Generates a professional PDF with Greek/English parallel columns
"""

import json
import re
import os
from pathlib import Path


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters in text."""
    if not text:
        return ""
    
    # Order matters - escape backslash first
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
    
    # Handle em-dashes and en-dashes
    text = text.replace('—', '---')
    text = text.replace('–', '--')
    
    # Handle smart quotes
    text = text.replace('"', "``")
    text = text.replace('"', "''")
    text = text.replace(''', "'")
    text = text.replace(''', "`")
    
    return text


def escape_latex_greek(text: str) -> str:
    """Escape LaTeX characters for Greek text (minimal escaping needed)."""
    if not text:
        return ""
    
    # For Greek, we mainly need to escape structural characters
    replacements = [
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
    
    return text


def generate_preamble(title: str, description: str) -> str:
    """Generate LaTeX document preamble."""
    return r"""\documentclass[11pt, twoside, openany]{book}

% Page geometry
\usepackage[
    paperwidth=7in,
    paperheight=10in,
    inner=0.9in,
    outer=0.7in,
    top=0.8in,
    bottom=0.9in
]{geometry}

% Font setup with XeLaTeX
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage{english}
\setotherlanguage{greek}

% Use professional fonts
\setmainfont{Palatino Linotype}[
    Ligatures=TeX,
    Numbers=OldStyle
]
\setsansfont{Calibri}[
    Ligatures=TeX
]
\newfontfamily\greekfont{Palatino Linotype}[
    Script=Greek,
    Ligatures=TeX
]

% Parallel columns
\usepackage{paracol}
\setcolumnwidth{0.48\textwidth, 0.48\textwidth}

% Styling packages
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{ragged2e}
\usepackage{setspace}

% Color definitions
\definecolor{chaptercolor}{RGB}{139, 69, 19}
\definecolor{versenum}{RGB}{128, 0, 0}
\definecolor{notecolor}{RGB}{70, 70, 70}
\definecolor{termcolor}{RGB}{0, 51, 102}

% Chapter styling
\titleformat{\chapter}[display]
    {\normalfont\Large\scshape\centering}
    {}
    {0pt}
    {\color{chaptercolor}\LARGE}
\titlespacing*{\chapter}{0pt}{30pt}{20pt}

% Section styling for notes
\titleformat{\section}
    {\normalfont\large\bfseries\color{chaptercolor}}
    {}
    {0pt}
    {}
\titlespacing*{\section}{0pt}{15pt}{8pt}

% Headers and footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\textsc{The Gospel (Proto-Luke)}}
\fancyhead[RO]{\small\textsc{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}

% Adjust spacing
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}

% Custom commands
\newcommand{\versenum}[1]{{\color{versenum}\textsuperscript{\textbf{#1}}}}
\newcommand{\canonref}[1]{{\small\textit{[#1]}}}
\newcommand{\noteterm}[1]{{\color{termcolor}\textbf{#1}}}
\newcommand{\notecategory}[1]{{\small\textsc{#1}}}

% Hyperref (load last)
\usepackage[
    colorlinks=true,
    linkcolor=chaptercolor,
    urlcolor=chaptercolor,
    bookmarks=true,
    bookmarksnumbered=true,
    pdfstartview=FitH
]{hyperref}

\title{""" + escape_latex(title) + r"""}
\author{}
\date{}

\begin{document}

% Title page
\begin{titlepage}
    \centering
    \vspace*{2in}
    
    {\Huge\scshape The Gospel}\\[0.5cm]
    {\Large\scshape (Proto-Luke)}\\[1.5cm]
    
    \rule{0.6\textwidth}{0.5pt}\\[1cm]
    
    {\large\itshape A Forensic Reconstruction of the}\\[0.3cm]
    {\large\itshape Jamesian Protograph}\\[2cm]
    
    \vfill
    
    {\small With Greek and English Parallel Text}\\[0.3cm]
    {\small and Scholarly Commentary}
    
    \vspace{1in}
\end{titlepage}

% Description page
\thispagestyle{empty}
\vspace*{1in}
\begin{center}
    \textsc{Preface}
\end{center}
\vspace{0.5cm}

\begin{quote}
""" + escape_latex(description) + r"""
\end{quote}

\clearpage
\tableofcontents
\clearpage

"""


def generate_verse_pair(verse: dict) -> str:
    """Generate a parallel Greek/English verse pair."""
    verse_num = verse.get('verse', '')
    english = escape_latex(verse.get('english', ''))
    greek = escape_latex_greek(verse.get('greek', ''))
    canon_ref = verse.get('canonical_ref', '')
    
    # Build the verse block
    latex = r"""
\begin{paracol}{2}
\switchcolumn[0]
\begin{greek}
\versenum{""" + str(verse_num) + r"""} """ + greek + r"""
\end{greek}
\switchcolumn[1]
\versenum{""" + str(verse_num) + r"""} """ + english
    
    if canon_ref:
        latex += r""" \canonref{""" + escape_latex(canon_ref) + r"""}"""
    
    latex += r"""
\end{paracol}
\vspace{3pt}
"""
    return latex


def generate_note(note: dict) -> str:
    """Generate a formatted note entry."""
    term = escape_latex(note.get('term', ''))
    explanation = escape_latex(note.get('explanation', ''))
    category = note.get('category', '')
    verse_refs = note.get('verse_refs', [])
    
    # Format verse references
    if verse_refs:
        refs_str = ', '.join(str(v) for v in verse_refs)
        refs_latex = f" (v. {refs_str})"
    else:
        refs_latex = ""
    
    latex = r"""
\noindent\noteterm{""" + term + r"""}""" + refs_latex
    
    if category:
        latex += r""" \hfill \notecategory{""" + escape_latex(category) + r"""}"""
    
    latex += r"""

\begin{quote}
\small """ + explanation + r"""
\end{quote}
\vspace{6pt}
"""
    return latex


def generate_additional_explanation(additional: dict) -> str:
    """Generate additional explanation section if present."""
    if not additional:
        return ""
    
    title = escape_latex(additional.get('title', 'Additional Commentary'))
    
    latex = r"""
\subsection*{""" + title + r"""}

"""
    
    # Handle paragraphs if present
    paragraphs = additional.get('paragraphs', [])
    for para in paragraphs:
        latex += escape_latex(para) + r"""

"""
    
    return latex


def generate_chapter(chapter: dict) -> str:
    """Generate a complete chapter with verses and notes."""
    chapter_num = chapter.get('chapter', '')
    title = chapter.get('title', f'Chapter {chapter_num}')
    preamble = chapter.get('preamble', '')
    verses = chapter.get('verses', [])
    notes = chapter.get('notes', [])
    additional = chapter.get('additional_explanation', {})
    
    # Start chapter
    latex = r"""
\chapter{""" + escape_latex(title) + r"""}
"""
    
    # Add preamble if present
    if preamble:
        latex += r"""
\begin{quote}
\textit{""" + escape_latex(preamble) + r"""}
\end{quote}
\vspace{10pt}
"""
    
    # Add verses
    latex += r"""
\section*{Text}
"""
    
    for verse in verses:
        latex += generate_verse_pair(verse)
    
    # Add notes at end of chapter
    if notes:
        latex += r"""
\vspace{15pt}
\section*{Notes}
"""
        for note in notes:
            latex += generate_note(note)
    
    # Add additional explanation if present
    if additional:
        latex += generate_additional_explanation(additional)
    
    return latex


def generate_document(json_data: dict) -> str:
    """Generate the complete LaTeX document."""
    title = json_data.get('title', 'The Gospel (Proto-Luke)')
    description = json_data.get('description', '')
    chapters = json_data.get('chapters', [])
    
    # Build document
    latex = generate_preamble(title, description)
    
    for chapter in chapters:
        latex += generate_chapter(chapter)
    
    # End document
    latex += r"""
\end{document}
"""
    
    return latex


def main():
    """Main entry point."""
    # Paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    json_path = project_dir / 'proto_luke.json'
    output_path = project_dir / 'output' / 'proto_luke.tex'
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Load JSON
    print(f"Loading JSON from: {json_path}")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Found {len(data.get('chapters', []))} chapters")
    
    # Generate LaTeX
    print("Generating LaTeX...")
    latex = generate_document(data)
    
    # Write output
    print(f"Writing LaTeX to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex)
    
    print("Done! To compile:")
    print(f"  cd {output_path.parent}")
    print(f"  xelatex proto_luke.tex")
    print("  (run twice for table of contents)")


if __name__ == '__main__':
    main()
