# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Master's thesis repository for Uppsala University. The project contains LaTeX templates and documents for writing and compiling the thesis.

## Repository Structure

```
MastersThesis/
├── Uppsala_University_template/
│   ├── main.tex                           # LaTeX title page template
│   └── Uppsala_University_seal_svg.png    # University logo
└── Andrei Olaru MA Thesis Proposal UU.docx # Thesis proposal (Word format)
```

## LaTeX Compilation

### Basic Compilation Commands

```bash
# Compile LaTeX to PDF (run from Uppsala_University_template directory)
cd Uppsala_University_template
pdflatex main.tex

# For documents with bibliography
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Using latexmk (automatic build tool - recommended)
latexmk -pdf main.tex

# Clean auxiliary files
latexmk -c              # Clean auxiliary files
latexmk -C              # Clean all generated files including PDF
```

### Alternative Compilation Methods

```bash
# Using XeLaTeX (for Unicode and modern fonts)
xelatex main.tex

# Using LuaLaTeX (for advanced font features)
lualatex main.tex
```

## Uppsala University Template

The `Uppsala_University_template/main.tex` file is a title page template that includes:
- University branding with the Uppsala University seal
- Standard title page layout with course information, title, author, and date
- Package dependencies: babel, inputenc, amsmath, graphicx, float, todonotes

### Template Customization Points

When working with the template, customize these sections in `main.tex`:
- Line 40: University name
- Line 42-43: Course name and code
- Line 50: Document title
- Line 60: Author name
- Line 73: Date (uses `\today` by default)

## Working with LaTeX

### Common Packages Used

- `babel`: Language support (currently set to English)
- `inputenc`: UTF-8 input encoding
- `amsmath`: Mathematical typesetting
- `graphicx`: Image inclusion
- `float`: Float positioning (figures, tables)
- `todonotes`: TODO annotations in the document

### Adding Content

To expand beyond the title page:
1. Add content after line 78 (before `\end{document}`)
2. Create sections with `\section{Title}`, `\subsection{Title}`
3. Include figures: `\includegraphics[options]{filename}`
4. Add citations with bibliography file and `\cite{key}`

### Directory Organization Best Practices

For a full thesis, consider organizing as:
```
chapters/       # Individual chapter .tex files
figures/        # Images and graphics
bibliography/   # .bib files for references
appendices/     # Appendix content
```

## Development Workflow

1. **Edit**: Modify .tex files with content
2. **Compile**: Run `pdflatex main.tex` or `latexmk -pdf main.tex`
3. **View**: Open generated PDF to review output
4. **Debug**: Check .log file for errors if compilation fails
5. **Clean**: Run `latexmk -c` to remove auxiliary files

## Common Issues and Solutions

### Image Not Found
- Ensure image file is in the same directory as .tex file or provide full/relative path
- Check image file extension matches (case-sensitive on Unix systems)

### Compilation Errors
- Read the .log file for detailed error messages
- Common issues: missing packages, unclosed braces, special characters without escaping

### Bibliography Not Showing
- Run the full compile sequence: pdflatex → bibtex → pdflatex → pdflatex
- Ensure .bib file exists and is referenced with `\bibliography{filename}`

### Font Issues
- If using special fonts, switch to XeLaTeX or LuaLaTeX
- Install missing font packages via TeX distribution package manager

## Version Control Notes

When using git (not currently initialized):
- Add `*.aux`, `*.log`, `*.out`, `*.toc`, `*.pdf` to .gitignore
- Keep source .tex files and images in version control
- Consider versioning the final PDF separately or in releases
