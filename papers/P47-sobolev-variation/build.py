#!/usr/bin/env python3
"""Build explicit-math Markdown into portable LaTeX and PDF.

Requires Pandoc and Tectonic on PATH, or the research workspace's tool folder.
No heuristic math conversion is performed. manuscript.md is authoritative.
"""
from pathlib import Path
import os,re,shutil,subprocess
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
def executable(name):
    value=shutil.which(name)
    fallback=ROOT/'tools'/name/name
    if value:return value
    if fallback.is_file():return str(fallback)
    raise SystemExit(f'Install {name} and add it to PATH.')
s=(HERE/'manuscript.md').read_text()
title,s=s.split('\n',1)
s=s.replace('\nHenry Zweiman\n','\n',1).replace('\nSeptember 16, 2026\n','\n',1)
s=re.sub(r'^(#{2,}) ',lambda m:m.group(1)[1:]+' ',s,flags=re.M)
body=subprocess.check_output([executable('pandoc'),'-f','markdown+tex_math_dollars-smart','-t','latex','--top-level-division=section'],input=s,text=True)
body=body.replace('∎',r'\(\square\)').replace('Ł',r'\L{}').replace('ł',r'\l{}')
body=body.replace(r'\section{References}',r'\clearpage\raggedright\section{References}')
body=body.replace(r'\section{',r'\Needspace{8\baselineskip}\section{')
body=re.sub(r'(?=\\textbf\{(?:Theorem|Lemma|Proposition|Corollary) )',lambda _:r'\Needspace{6\baselineskip}',body)
for phrase, lines in [('Put \\(K_x', 8), ('Substitute (7.7)', 12)]:
    body=body.replace(phrase, r'\Needspace{'+str(lines)+r'\baselineskip}'+phrase)
body=body.replace(r'\subsection{8.1. A zero count', r'\Needspace{12\baselineskip}\subsection{8.1. A zero count')
preamble=r'''\documentclass[11pt]{article}
\usepackage[margin=0.88in]{geometry}
\usepackage{amsmath,amssymb,lmodern}
\usepackage[T1]{fontenc}
\usepackage{needspace}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.35em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{Sharp total variation bounds from spherical rearrangement}
\author{Henry Zweiman}
\date{September 16, 2026}
\begin{document}
\maketitle
'''
(HERE/'manuscript.tex').write_text(preamble+body+'\n\\end{document}\n')
subprocess.run([executable('tectonic'),'--keep-logs','--outdir',str(HERE),str(HERE/'manuscript.tex')],check=True)
