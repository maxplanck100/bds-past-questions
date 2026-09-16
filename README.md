# BDS Past Questions Bank (KU)

A structured and searchable collection of **BDS past examination questions from Kathmandu University (KU)**, organized by academic year and subject.

The project focuses on preserving past questions in a clean, study-friendly format through **PDF organization, OCR extraction, answer development, topic-frequency analysis, and revision resources**.

> **Project goal:** Turn scattered past-question papers into a reliable, structured study and revision resource for BDS students.

---

### Repository Structure

```text
bds-past-questions/
│
├── README.md
├── SUBJECTS.md
├── WALKTHROUGH.md
├── reusable-query.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
│
├── raw-pdfs/                         # Original/split past-question PDFs
│   └── year-1/
│       ├── anatomy.pdf
│       ├── biochemistry.pdf
│       ├── microbiology.pdf
│       ├── pathology.pdf
│       ├── pharmacology.pdf
│       ├── physiology.pdf
│       ├── BDS_1st_year_all_subjects_17-22.pdf
│       └── BDS_1st_year_all_subjects_images.pdf
│
├── extracted/                        # OCR-cleaned questions only
│   └── year-1/
│       ├── anatomy.md
│       ├── biochemistry.md
│       ├── microbiology.md
│       ├── pathology.md
│       ├── pharmacology.md
│       ├── physiology.md
│       ├── BDS_1st_year_all_subjects_17-22.md
│       └── BDS_1st_year_all_subjects_images_oral_bio.md
│
├── answers/                          # Verified/community-contributed answers
│   └── year-1/
│       ├── anatomy.md
│       ├── biochemistry.md
│       ├── microbiology.md
│       ├── pathology.md
│       ├── pharmacology.md
│       ├── physiology.md
│       ├── oral_biology.md
│       └── BDS_1st_year_all_subjects_17-22.md
│
├── analysis/                         # Topic frequency and exam prediction analysis
│   └── year-1/
│       ├── anatomy_top_topics.md
│       ├── biochemistry_top_topics.md
│       ├── microbiology_top_topics.md
│       ├── pathology_top_topics.md
│       ├── pharmacology_top_topics.md
│       ├── physiology_top_topics.md
│       ├── oral_biology_top_topics.md
│       └── BDS_1st_year_all_subjects_17-22.md
│
├── appendix/                         # Rapid revision cheatsheets
│   └── year-1/
│       ├── anatomy_cheatsheet.md
│       ├── biochemistry_cheatsheet.md
│       ├── microbiology_cheatsheet.md
│       ├── pathology_cheatsheet.md
│       ├── pharmacology_cheatsheet.md
│       ├── physiology_cheatsheet.md
│       ├── oral_biology_cheatsheet.md
│       └── BDS_1st_year_all_subjects_17-22.md
│
└── scripts/                          # Utility and automation scripts
    └── split_pdf.py
```

---

## Project Status

| Year   | Subjects & Sets | Extracted | Answered | Analyzed | Cheatsheets |
| ------ | --------------- | --------- | -------- | -------- | ----------- |
| Year 1 | 7 + Multi-Set   | 8/8 (100%)| 8/8 (100%)| 8/8 (100%)| 8/8 (100%) |
| Year 2 | —               | —         | —        | —        | —           |
| Year 3 | —               | —         | —        | —        | —           |
| Year 4 | —               | —         | —        | —        | —           |
| Year 5 | —               | —         | —        | —        | —           |

### Year 1 Curriculum Status

All Kathmandu University BDS 1st Year core subjects and multi-subject consolidated sets have been fully processed across the entire pipeline:

* [x] **Anatomy** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **Biochemistry** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **Microbiology** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **Pathology** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **Pharmacology** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **Physiology** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **Oral Biology** (Extraction, Answers, Top Topics Analysis, Quick Revision Cheatsheet)
* [x] **All Subjects 2017–2022 Multi-Paper Collection** (Extraction, Answers, Cross-Subject Analysis, Integrated Cheatsheet)       | —        | —        |
| Year 5 | —        | —         | —        | —        |

### Current Focus

**Year 1 — Question Extraction Complete**

* [x] Anatomy
* [x] Biochemistry
* [x] Microbiology
* [x] Pathology
* [x] Pharmacology
* [x] Physiology
* [x] Answer development
* [x] Topic/frequency analysis
* [x] Revision cheatsheets

---

## Project Workflow

The repository follows a staged workflow:

```text
Past Question PDFs
        │
        ▼
   PDF Organization
        │
        ▼
   OCR Extraction
        │
        ▼
   Manual Cleanup
        │
        ▼
  Structured Questions
        │
        ▼
  Answer Development
        │
        ▼
 Topic/Frequency Analysis
        │
        ▼
 Revision Cheatsheets
```

### 1. PDF Collection & Organization

Original past-question papers are collected and organized by academic year and subject.

Large multi-subject PDFs can be split into individual subject PDFs using the utility in:

```text
scripts/split_pdf.py
```

### 2. OCR Extraction

Scanned question papers are converted into searchable text using OCR and subsequently cleaned and structured.

The `extracted/` directory contains **questions only** and should not contain answers or explanations.

### 3. Answer Development

Answers are added separately under:

```text
answers/
```

Answers should be reviewed and, where possible, cross-checked against authoritative textbooks, lecture materials, and the relevant syllabus.

### 4. Topic & Frequency Analysis

Past questions can be analyzed across multiple years to identify:

* Frequently repeated topics
* Commonly tested concepts
* Question patterns
* High-frequency chapters
* Changes in examination trends

Analysis results are stored under:

```text
analysis/
```

### 5. Revision Cheatsheets

Frequently tested or high-priority topics can eventually be condensed into concise revision materials.

These resources are stored under:

```text
appendix/
```

---

## Tools & Methodology

The project may use a combination of:

* PDF processing tools
* OCR software
* LLM-assisted text cleanup
* Manual verification
* Markdown
* Python automation scripts
* Statistical/frequency analysis

Specific tools may change as the project develops. The objective is **accuracy and usefulness**, rather than dependence on a particular tool.

---

## Content Organization

Each subject follows the same general structure:

```text
Subject
├── Raw PDF
├── Extracted Questions
├── Answers
├── Topic Analysis
└── Revision Cheatsheet
```

This separation keeps the original questions distinct from interpretations, answers, and derived analysis.

---

## Accuracy & Verification

OCR output can contain errors, particularly with:

* Medical terminology
* Drug names
* Anatomical terms
* Abbreviations
* Diagrams
* Tables
* Handwritten annotations
* Poor-quality scans

Therefore, extracted questions should be compared against the original PDF whenever accuracy is important.

Answers contributed to this repository are **not automatically considered official answers**. They should be reviewed and cross-checked with appropriate academic sources.

---

## Recommended Books

The following textbooks are recommended as standard references for the six Year 1 subjects. Students should prioritize the books and resources specifically recommended by their university and lecturers.

| Subject | Recommended Textbook | Author(s) |
|---|---|---|
| **Anatomy** | *Gray's Anatomy for Students* | Richard L. Drake, A. Wayne Vogl & Adam W. M. Mitchell |
| **Biochemistry** | *Harper's Illustrated Biochemistry* | Victor W. Rodwell et al. |
| **Microbiology** | *Jawetz, Melnick & Adelberg's Medical Microbiology* | Karen C. Carroll et al. |
| **Pathology** | *Robbins & Cotran Pathologic Basis of Disease* | Vinay Kumar, Abul K. Abbas & Jon C. Aster |
| **Pharmacology** | *Katzung's Basic & Clinical Pharmacology* | Bertram G. Katzung, Susan B. Vanderah |
| **Physiology** | *Guyton and Hall Textbook of Medical Physiology* | John E. Hall & Michael E. Hall |
| **Oral Biology** | *Orban's Oral Histology and Embryology* / *Wheeler's Dental Anatomy, Physiology and Occlusion* | G.S. Kumar / Stanley J. Nelson |

### Suggested Use

These books should be treated as **reference textbooks**, not as substitutes for the official curriculum or lecturer-provided materials.

For efficient exam preparation:

- Use **past questions** to identify commonly tested topics.
- Use the **recommended textbooks** to understand concepts and verify answers.
- Use **lecturer notes and official course materials** to align your preparation with the university curriculum.
- Use the repository's future **analysis and cheatsheets** for targeted revision.
- Always cross-check potentially ambiguous or disputed answers with authoritative sources.

> **Note:** Textbook editions may change over time. Use the edition recommended by your department or lecturer when available.

---

## Disclaimer

This repository is an **independent educational and study resource**.

Past examination questions are reproduced for educational and revision purposes. The repository is not affiliated with or officially endorsed by Kathmandu University or any affiliated institution unless explicitly stated.

Answers, explanations, analyses, predictions, and revision materials are community-contributed or independently generated and **should not be treated as official university marking schemes**.

Students should verify information against their:

- **Official syllabus**
- **Lecturer-provided materials**
- **Recommended textbooks**
- **Institutional resources**
- **Other authoritative academic sources**

---

## Contributing

Contributions are welcome.

You can contribute by:

* Adding missing past papers
* Correcting OCR errors
* Improving question formatting
* Providing answers or explanations
* Citing reliable sources
* Identifying repeated topics
* Improving analysis
* Creating revision resources
* Improving automation scripts

Before contributing, please read:

```text
CONTRIBUTING.md
```

---

## Project Principles

The project follows a few simple principles:

1. **Preserve the original question.**
2. **Keep OCR output separate from answers.**
3. **Verify important corrections against the source PDF.**
4. **Prefer authoritative academic references.**
5. **Clearly distinguish facts from interpretation or prediction.**
6. **Do not present community answers as official answers.**
7. **Keep the repository structured and easy to navigate.**
8. **Automate repetitive work where practical.**

---

## Long-Term Goal

The eventual goal is to build a comprehensive BDS past-question knowledge base where students can move from:

**Past Papers → Structured Questions → Verified Answers → Topic Trends → High-Yield Revision**

while keeping the original source material, derived analysis, and community contributions clearly separated.
