# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Master's thesis proposal for Uppsala University by Andrei Dan Olaru. The thesis is titled **"Applying Transformative Game Design Theory to Competitive Debate"** and uses Research through Design methodology to create a new competitive debate format called "Inside Out" that addresses problems in existing formats (World Schools, British Parliamentary).

The thesis argues that debate is a class of role-playing games with transformative potential, and applies transformative game design theory to improve format design.

## Repository Structure

```
MastersThesis/
├── thesis_proposal.tex                    # Main LaTeX document (entry point)
├── references.bib                         # Bibliography (biblatex/biber, APA style)
├── chapters/
│   ├── introduction.tex                   # Research question, motivation, problem statement
│   ├── background.tex                     # Literature review: debate as transformative game & RPG
│   ├── theoretical_framework.tex          # Transformational container, bleed, procedural rhetoric
│   ├── methods.tex                        # Research through Design, observation, interviews
│   ├── design.tex                         # The "Inside Out" debate format design
│   └── conclusion.tex                     # Conclusion + Timeline Annex
├── Sources/
│   ├── On debate/                         # Reference PDFs on competitive debate
│   ├── On games/                          # Reference PDFs on game design & RPGs
│   └── On research/                       # Reference PDFs on research methodology
├── Uppsala_University_template/
│   ├── main.tex                           # Title page template (referenced by thesis_proposal.tex)
│   └── Uppsala_University_seal_svg.png    # University logo
├── InsideOutDebateFormat.rtf              # Inside Out format description (RTF)
├── InsideOut_Debate_Format.pptx           # Inside Out format presentation
├── annotated-thesis_proposal_JJ.pdf       # Supervisor-annotated proposal
├── Andrei Olaru MA Thesis Proposal UU.docx # Original thesis proposal (Word)
└── .gitignore
```

## LaTeX Compilation

The main document is `thesis_proposal.tex` at the repository root. It uses **biblatex with biber** (APA style), not bibtex.

### Compilation Commands

```bash
# Recommended: latexmk handles the full build cycle automatically
latexmk -pdf thesis_proposal.tex

# Manual compilation (must use pdflatex + biber, not bibtex)
pdflatex thesis_proposal.tex
biber thesis_proposal
pdflatex thesis_proposal.tex
pdflatex thesis_proposal.tex

# Clean auxiliary files
latexmk -c              # Clean auxiliary files
latexmk -C              # Clean all generated files including PDF
```

### Key Packages

- `biblatex` with `biber` backend (APA style) -- bibliography management
- `babel`, `inputenc`, `csquotes` -- language and encoding
- `amsmath` -- math typesetting
- `graphicx`, `float` -- figures
- `geometry` -- page layout (1in margins)
- `tikz` -- diagrams
- `hyperref` -- clickable cross-references and URLs
- `titlesec` -- section heading formatting
- `todonotes` -- TODO annotations

### Citations

Use `\textcite{key}` for in-text citations and `\parencite{key}` for parenthetical (APA style via biblatex). Bibliography entries are in `references.bib`.

## Editing Workflow

1. **Edit** chapter files in `chapters/` or the main `thesis_proposal.tex`
2. **Compile** with `latexmk -pdf thesis_proposal.tex`
3. **View** `thesis_proposal.pdf`
4. **Debug** via `thesis_proposal.log` if compilation fails

## Common Issues

### Bibliography Not Showing
- This project uses **biber**, not bibtex. Run `biber thesis_proposal` (not `bibtex`)
- Or just use `latexmk -pdf` which handles everything automatically

### Adding a New Chapter
1. Create `chapters/newchapter.tex` with a `\section{TITLE}` heading
2. Add `\input{chapters/newchapter}` in `thesis_proposal.tex` between existing `\input` lines

### Image Paths
- Images reference paths relative to the root (e.g., `Uppsala_University_template/Uppsala_University_seal_svg.png`)
