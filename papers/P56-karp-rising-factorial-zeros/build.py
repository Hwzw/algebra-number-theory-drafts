#!/usr/bin/env python3
"""Generate LaTeX and PDF from the authoritative Markdown manuscript.
Requires Pandoc and Tectonic. PANDOC and TECTONIC may specify executable paths.
"""
import os
from pathlib import Path
import re
import shutil
import subprocess

HERE=Path(__file__).resolve().parent

def executable(name):
    result=os.environ.get(name.upper()) or shutil.which(name)
    if not result:
        raise SystemExit(f'Install {name} or set {name.upper()} to its executable path.')
    return result

source=(HERE/'manuscript.md').read_text()
source='## Abstract'+source.split('## Abstract',1)[1]
source=re.sub(r'^## ', '# ', source, flags=re.M)
body=subprocess.check_output([executable('pandoc'),'-f','markdown+tex_math_dollars-smart',
                              '-t','latex'],input=source,text=True)
body=body.replace(r'\section{',r'\Needspace{6\baselineskip}\section{')
body=re.sub(r'(?=\\textbf\{(?:Theorem|Lemma|Proposition) )',
            lambda _:r'\Needspace{5\baselineskip}',body)
preamble=r'''\documentclass[11pt]{article}
\usepackage[margin=0.95in]{geometry}
\usepackage{amsmath,amssymb,lmodern}
\usepackage[T1]{fontenc}
\usepackage{needspace}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\hypersetup{pdftitle={Negative real zeros of a rising-factorial transform},pdfauthor={Henry Zweiman}}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{Negative real zeros of a rising-factorial transform}
\author{Henry Zweiman}
\date{September 22, 2026}
\begin{document}
\maketitle
\begin{center}\small Research preprint, version 1.0.\\
Prepared with OpenAI Codex; not peer reviewed.\end{center}
'''
(HERE/'manuscript.tex').write_text(preamble+body+'\n\\end{document}\n')
subprocess.run([executable('tectonic'),'--keep-logs','--outdir',str(HERE),
                str(HERE/'manuscript.tex')],check=True)
