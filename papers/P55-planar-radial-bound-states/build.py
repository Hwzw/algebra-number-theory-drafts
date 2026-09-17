#!/usr/bin/env python3
"""Build the review manuscript from the authoritative Markdown source."""
from pathlib import Path
import re
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

def executable(name):
    found = shutil.which(name)
    fallback = ROOT / 'tools' / name / name
    if found:
        return found
    if fallback.is_file():
        return str(fallback)
    raise SystemExit(f'Install {name} or put it on PATH.')

source = (HERE / 'manuscript.md').read_text()
source = source.split('\n', 1)[1]
source = source.replace('\nResearch draft prepared for Henry Zweiman\n', '\n', 1)
source = source.replace('\nSeptember 17, 2026\n', '\n', 1)
source = source.replace('–', '-').replace('—', '--').replace('‑', '-')
source = re.sub(r'^## ', '# ', source, flags=re.M)
body = subprocess.check_output(
    [executable('pandoc'), '-f', 'markdown+tex_math_dollars-smart', '-t', 'latex'],
    input=source, text=True,
)
body = body.replace(r'\section{', r'\Needspace{7\baselineskip}\section{')
body = re.sub(r'(?=\\textbf\{(?:Theorem|Lemma|Corollary|Proposition) )',
              lambda _: r'\Needspace{5\baselineskip}', body)
body = body.replace(r'\Needspace{5\baselineskip}\textbf{Theorem 1.1',
                    r'\Needspace{11\baselineskip}\textbf{Theorem 1.1')
preamble = r'''\documentclass[11pt]{article}
\usepackage[margin=0.9in]{geometry}
\usepackage{amsmath,amssymb,lmodern}
\usepackage[T1]{fontenc}
\usepackage{needspace}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.3em}
\setcounter{secnumdepth}{0}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{A planar comparison argument for radial bound states}
\author{Research draft prepared for Henry Zweiman}
\date{September 17, 2026}
\begin{document}
\maketitle
'''
(HERE / 'manuscript.tex').write_text(preamble + body + '\n\\end{document}\n')
subprocess.run([executable('tectonic'), '--keep-logs', '--outdir', str(HERE),
                str(HERE / 'manuscript.tex')], check=True)
