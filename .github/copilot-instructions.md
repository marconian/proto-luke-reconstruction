# Proto-Luke Reconstruction Project - Editorial Instructions

## Project Overview

This repository contains a scholarly reconstruction of **Proto-Luke** (the Jamesian Protograph), a hypothetical source document underlying the canonical Gospel of Luke. The reconstruction is based on the **New Marcionite Paradigm** in biblical scholarship.

### Key Scholarly Sources
- **Matthias Klinghardt** - *The Oldest Gospel and the Formation of the Canonical Gospels*
- **Jason BeDuhn** - *The First New Testament: Marcion's Scriptural Canon*
- **Markus Vinzent** - *Marcion and the Dating of the Synoptic Gospels*
- **Novum Testamentum Graece (NTG 27)** - Greek text base

### Research Assistant

All scholarly questions and editorial decisions requiring in-depth knowledge should be referred to our NotebookLM research assistant: **[The Bible Notebook](https://notebooklm.google.com/notebook/ddf5f7ea-f040-4920-96a4-8e284ee327fe?authuser=1)**

This research assistant has access to all primary sources and scholarly materials needed for the reconstruction. Do NOT make independent editorial decisions on content—consult The Bible Notebook first.

### Core Premise
The reconstruction proceeds from the hypothesis that Marcion's Gospel (*Evangelion*) preserves an earlier form of the Jesus tradition than canonical Luke, and that this earlier form reflects a **Jamesian** (Jewish-Christian) theological perspective rather than a Pauline one.

---

## Terminology Guidelines

### The Protagonist

| ✅ CORRECT | ❌ INCORRECT |
|-----------|-------------|
| **Jesus** | "the Messenger" |
| **he/him** (referring to Jesus) | "the Messenger" as title |

- Always refer to the protagonist as **"Jesus"** in English translations and notes
- The term "the Messenger" was incorrectly used in earlier drafts and has been systematically replaced
- Exception: Lowercase **"messenger(s)"** is correct when translating **ἄγγελος** (angelos) referring to actual angels/messengers

### Jamesian vs. Pauline Vocabulary

This is a **Jamesian** reconstruction. Avoid Pauline theological terminology:

| ✅ JAMESIAN (Use These) | ❌ PAULINE (Avoid) |
|------------------------|-------------------|
| "The Living One" (ὁ ζῶν) | "Soma Pneumatikon" |
| "Exaltation" | "Spiritual Body" |
| "Raised/Risen" | "Resurrection body" (when emphasizing physicality) |
| "Vindication" | Pauline atonement language |

### Greek Text Conventions

- Greek text uses the **Novum Testamentum Graece (NTG 27)** edition as base
- Preserve original Greek in `greek_text` fields
- Use standard scholarly transliteration when discussing Greek in notes
- Mark textual variants explicitly

---

## JSON Structure

The primary data file is `data/proto_luke.json`. Structure:

```json
{
  "title": "THE GOSPEL (PROTO-LUKE)",
  "subtitle": "The Jamesian Protograph",
  "preface": "...",
  "chapters": [
    {
      "chapter_number": 1,
      "preamble": "Chapter introduction...",
      "verses": [
        {
          "verse_number": 1,
          "greek_text": "...",
          "english_translation": "...",
          "notes": "Scholarly apparatus..."
        }
      ]
    }
  ]
}
```

### Field Guidelines

- **preface**: Scholarly introduction with citations
- **preamble**: Chapter-level introduction explaining context and theological themes
- **greek_text**: NTG 27 based Greek, with variants noted
- **english_translation**: Clear, readable translation following Jamesian terminology
- **notes**: Scholarly apparatus including:
  - Textual variants
  - Marcionite parallels
  - Western Non-Interpolations
  - Synoptic comparisons
  - Theological commentary

---

## File Organization

```
ProtoLuke/
├── .github/
│   └── copilot-instructions.md    # This file
├── data/
│   └── proto_luke.json            # Primary reconstruction data
├── docs/
│   └── research_questions.md      # Scholarly decisions log
├── output/
│   └── Proto-Luke_Jamesian_Protograph.pdf
├── scripts/
│   └── json_to_pdf.py             # PDF generation script
└── README.md
```

---

## GitFlow Workflow

- **main**: Release-ready versions only
- **develop**: Active development branch
- Feature work: Create feature branches from `develop`
- Merge to `main` only for releases

---

## Research Questions Protocol

When encountering scholarly decisions, document in `docs/research_questions.md`:

1. State the question clearly
2. Provide relevant evidence
3. Document the decision and rationale
4. Mark as RESOLVED with implementation notes

---

## PDF Generation

Run from project root:

```bash
python scripts/json_to_pdf.py
```

Output: `output/Proto-Luke_Jamesian_Protograph.pdf`

---

## Common Editorial Tasks

### Adding/Editing Verses
1. Ensure Greek text matches NTG 27 (or note variants)
2. Consult **The Bible Notebook** research assistant for editorial decisions
3. Translation uses Jamesian terminology
4. Notes cite scholarly sources appropriately
5. Cross-reference Marcionite parallels where applicable

### Terminology Checks
Before committing, verify:
- [ ] No instances of "the Messenger" as title for Jesus
- [ ] No Pauline "Soma Pneumatikon" language
- [ ] Greek text properly formatted (NTG 27 base)
- [ ] Citations follow scholarly convention
- [ ] Editorial decisions validated with The Bible Notebook

### Quality Assurance
- Regenerate PDF after JSON changes
- Verify JSON validity (no syntax errors)
- Check cross-references between chapters

---

## Scholarly Context Notes

### Marcionite Parallels
Where Marcion's *Evangelion* (as reconstructed by scholars) differs from canonical Luke, note:
- The Marcionite reading
- Whether it likely represents the earlier form
- Theological implications of variants

### The Passion Narrative
Chapter 22+ represents the Passion narrative. Special attention to:
- Luke 22:43-44 (Agony in Gethsemane) - textual variant, consult The Bible Notebook
- Luke 23:34a ("Father, forgive them") - textual variant, consult The Bible Notebook
- Luke 24 resurrection accounts - Jamesian "Living One" terminology

---

## Contact & Attribution

Repository: https://github.com/marconian/proto-luke-reconstruction.git

This reconstruction is a scholarly exercise in textual criticism and should be cited appropriately in academic work.
