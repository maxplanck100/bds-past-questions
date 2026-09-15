# Raw Question Papers

This directory contains the original or subject-split PDF files of
Kathmandu University (KU) BDS past examination papers.

These PDFs are the **source material for the entire question-bank
pipeline**:

`raw-pdfs → extracted → answers → analysis → appendix`

Do not edit, rewrite, OCR, or annotate the PDFs stored here. Any
processed or derived content should be placed in the appropriate
downstream directory.

---

## Directory Structure

```text
raw-pdfs/
└── year-1/
    ├── anatomy.pdf
    ├── biochemistry.pdf
    ├── microbiology.pdf
    ├── pathology.pdf
    ├── pharmacology.pdf
    └── physiology.pdf
````

Each academic year should have its own directory:

```text
raw-pdfs/
├── year-1/
├── year-2/
├── year-3/
└── ...
```

Subject filenames should remain lowercase and descriptive, for example:

```text
anatomy.pdf
biochemistry.pdf
microbiology.pdf
pathology.pdf
pharmacology.pdf
physiology.pdf
```

---

## Source Quality

Whenever possible, use the clearest available copy of the original
question paper.

Prefer:

1. Original university-issued PDF
2. Clear scanned copy
3. Reliable student/archive copy

Avoid heavily compressed, cropped, or incomplete copies when a better
source is available.

If a paper is incomplete or contains genuinely unreadable sections,
keep the original PDF unchanged and record the issue during the
extraction/verification stage.

---

## Adding a New Paper

Before adding a PDF:

* Confirm the correct academic year.
* Confirm the subject.
* Check that the paper is complete.
* Use the standard filename.
* Do not modify the original questions.
* Keep the PDF inside the appropriate `year-<N>/` directory.

Example:

```text
raw-pdfs/year-1/anatomy.pdf
```

Further processing should follow the workflow described in
[`../WALKTHROUGH.md`](../WALKTHROUGH.md).

---

## Recommended Textbooks

These books can be useful later when developing or verifying answers.
They are **reference recommendations, not replacements for the original
question papers or official KU teaching materials**.

### Anatomy

* *Gray's Anatomy for Students* — Richard L. Drake et al.
* *BD Chaurasia's Human Anatomy* — B. D. Chaurasia

### Biochemistry

* *Harper's Illustrated Biochemistry* — Victor W. Rodwell et al.
* *Lippincott Illustrated Reviews: Biochemistry* — Denise R. Ferrier

### Microbiology

* *Jawetz, Melnick & Adelberg's Medical Microbiology*
* *Ananthanarayan and Paniker's Textbook of Microbiology*

### Pathology

* *Robbins & Cotran Pathologic Basis of Disease*
* *Harsh Mohan Textbook of Pathology*

### Pharmacology

* *Katzung & Trevor's Basic & Clinical Pharmacology*
* *Goodman & Gilman's The Pharmacological Basis of Therapeutics*

### Physiology

* *Guyton and Hall Textbook of Medical Physiology*
* *Ganong's Review of Medical Physiology*

Use the edition recommended by the relevant KU course/faculty where
possible.

---

## Important

This directory is intended to preserve the **source layer** of the
project.

Do not place:

* OCR text
* corrected questions
* answers
* explanations
* topic analysis
* frequency statistics
* prediction lists
* cheatsheets

inside `raw-pdfs/`.

Those belong in the corresponding downstream directories.
