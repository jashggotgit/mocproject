# MOC Project: ALVEARE Research Paper Presentation & State Diagrams

This directory contains the final deliverables for the research paper:
> **ALVEARE: A Full-Stack Domain-Specific Framework for Regular Expressions**  
> *Published in IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)*  
> *Authors: Filippo Carloni, Davide Conficconi, Emanuele Del Sozzo, Marco D. Santambrogio (Politecnico di Milano NECSTLab)*

---

## 📂 Deliverables Overview

### 1. Presentation Slides
* **`ALVEARE_Research_Paper_Presentation.pptx`**: Native 16:9 widescreen PowerPoint deck with custom styling, high-contrast visual hierarchy, card components, and embedded presenter speaker notes.
* **`ALVEARE_Research_Paper_Presentation.pdf`**: Print-ready high-resolution presentation PDF.
* **`slides_img/`**: Individual 1080p slide renders (`slide_01.png` to `slide_11.png`) for quick previews or document inserts.

### 2. State Diagrams (SVGs)
* **`alveare_simple_clean_diagram.svg`**: Classic planar automata graph (Style 1) with circular states ($Q_0$ to $Q_{20}$), blue start node, red rollback error recovery node ($Q_{10}$), and green double-ring accept node ($Q_{20}$). Zero crossing lines.
* **`alveare_phased_clean_diagram.svg`**: 4-row phased swimlane DFA (Style 2) breaking down execution into Compilation $\rightarrow$ ISA Dispatch $\rightarrow$ Stream Speculation $\rightarrow$ Match Writeback with self-loops.
* **`view_state_diagrams.html`**: Interactive side-by-side browser viewer to inspect, zoom, and print the state diagrams.

### 3. Documentation & Speaker Notes
* **`Presentation_Summary_and_Speaker_Notes.md`**: Complete slide-by-slide transcript, technical metrics, microarchitecture breakdown (Speculation Stack, 43-bit ISA, parallel front-end), and Q&A defense answers.

### 4. Reproducibility Scripts (`scripts/`)
* **`create_presentation.py`**: Python script using `python-pptx` that programmatically builds the slide deck.
* **`create_both_perfect_diagrams.py`**: Python generator for both SVG state diagrams.
* **`export_slides.ps1`**: PowerShell script using PowerPoint COM automation to export slides to PDF and high-res images.
