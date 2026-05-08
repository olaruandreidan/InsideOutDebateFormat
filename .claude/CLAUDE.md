# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Master's thesis manuscript for Uppsala University by Andrei Dan Olaru, titled **"Applying Transformative Game Design Theory to Competitive Debate"**. It uses Research through Design to develop a new competitive debate format ("Inside Out") that addresses problems in World Schools and British Parliamentary, and argues that debate is a class of role-playing games whose transformative potential is unlocked by treating it as one in design.

The repo holds the full manuscript (intro through conclusion plus annexes), the research material that fed it (playtest transcripts, debrief notes, supervisor annotations), and a separate source-annotations document. The main entry-point file is still named `thesis_proposal.tex` for historical reasons.

## Repository Structure

Two LaTeX documents live at the root:
- `thesis_proposal.tex` — the main thesis manuscript. Inputs files from `chapters/` in this order: `introduction`, `background`, `theoretical_framework`, `methods`, `design`, `results`, `discussion`, `conclusion`, `annexes`.
- `source_annotations.tex` — a *separate* self-contained document (own preamble, custom `\entry{...}` macro) compiled independently to `source_annotations.pdf`. Don't confuse the two when editing.

Directories:
- `chapters/` — body chapters listed above, plus the annex hub `annexes.tex` which inputs `annex_format.tex` (Annexes A–B), `annex_materials.tex` (C–E), `annex_reports.tex` (F–H), and `annex_clues.tex` (I).
- `sources/` — reference PDFs grouped under `On debate/`, `On games/`, `On research/`. Reading material; cited in `references.bib`.
- `otherdocuments/` — **research material and source artifacts**, not output. Includes playtest transcripts (`transcriptPlaytest1.txt`, `transcriptPlaytest2.txt`, `transcriptPlaytest2Debrief.txt`), playtest notes (`Notes from first playtest.txt`, `Notes after Playtest 2.txt`), the supervisor-annotated PDF (`annotated-thesis_proposal_JJ.pdf`), the Uppsala title-page template (`uppsala_University_template/`), the Inside Out format description (`InsideOutDebateFormat.rtf`, `.pptx`), and working notes (`On the discussion.md`, `Results remake points.txt`, `SummaryResultsSection.txt`, `commendations.txt`). When integrating playtest evidence into a chapter, this is where the raw material lives.
- `scripts/wordcount.sh` — body word count (see below).
- `tools/texcount.pl` — vendored TeXcount 3.1.1 used as a fallback by the wordcount script.
- `docs/` — public web pages for the Inside Out format (`index.html`).
- `references.bib` — bibliography (biblatex/biber, APA style).

Title-page seal is loaded from `otherdocuments/uppsala_University_template/Uppsala_University_seal_svg.png` (referenced by `thesis_proposal.tex`).

## LaTeX Compilation

The main document is `thesis_proposal.tex` at the repository root. It uses **biblatex with biber** (APA style), not bibtex.

### Compilation Commands

```bash
# Recommended: latexmk handles the full build cycle automatically
latexmk -pdf thesis_proposal.tex

# The source-annotations document compiles independently
latexmk -pdf source_annotations.tex

# Manual compilation (must use pdflatex + biber, not bibtex)
pdflatex thesis_proposal.tex
biber thesis_proposal
pdflatex thesis_proposal.tex
pdflatex thesis_proposal.tex

# Clean auxiliary files
latexmk -c              # Clean auxiliary files
latexmk -C              # Clean all generated files including PDF
```

VSCode (LaTeX Workshop, see `.vscode/settings.json`) auto-builds on save with `latexmk`, so during interactive editing manual recompiles are usually unnecessary.

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

## Editorial Conventions

- **Commenting out prose**: prefix each line with `%` rather than wrapping blocks in `\iffalse … \fi`. This was a deliberate switch (commit `c9322b3`) so commented passages stay searchable and diff cleanly. Don't reintroduce `\iffalse` to hide content.
- **Drafting against research material**: when revising a chapter to better reflect playtest evidence or supervisor feedback, the source material is in `otherdocuments/` (transcripts, notes, the annotated PDF). Read from there; write to `chapters/`.
- **Annexes are not body text** — they live in their own `chapters/annex_*.tex` files (orchestrated by `chapters/annexes.tex`) and are excluded from the body word count.

## Word Count

Run the body word count (excludes annexes and bibliography):

```bash
./scripts/wordcount.sh
```

Prints a per-chapter breakdown plus a `TOTAL (body)` row. The script prefers a system `texcount` if installed (`sudo tlmgr install texcount`) and otherwise falls back to the vendored `tools/texcount.pl` (TeXcount 3.1.1 from CTAN, run via `perl`). Vendoring the tool means word-counting works on any machine that clones the repo, regardless of the local TeX install state.

The script counts the eight chapter files in `chapters/` that constitute body content; annexes (`annex_*.tex`, hub: `chapters/annexes.tex`) are excluded by being absent from the script's chapter list. The bibliography is auto-excluded because it's generated by biber from `references.bib` and produces no LaTeX-source words.

If you add a new body chapter, also append its name to the `chapters=( … )` array in `scripts/wordcount.sh`.

## Editing Workflow

1. **Edit** chapter files in `chapters/` or the main `thesis_proposal.tex`
2. **Compile** with `latexmk -pdf thesis_proposal.tex`
3. **View** `thesis_proposal.pdf`
4. **Debug** via `thesis_proposal.log` if compilation fails

## Common Issues

### Adding a New Chapter
1. Create `chapters/newchapter.tex` with a `\section{TITLE}` heading
2. Add `\input{chapters/newchapter}` in `thesis_proposal.tex` between existing `\input` lines
3. Append the chapter name to the `chapters=( … )` array in `scripts/wordcount.sh` so it counts toward the body total.

### Adding a New Annex
1. Either add a section to one of the existing `chapters/annex_*.tex` files, or create a new `chapters/annex_<topic>.tex` and `\input` it from `chapters/annexes.tex`.
2. Annexes are intentionally excluded from the body word count — leave them out of `scripts/wordcount.sh`'s `chapters=( … )` array.
