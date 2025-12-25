# Proto-Luke: The Jamesian Protograph

A forensic reconstruction of the primitive Gospel underlying the Lukan tradition, identified with the Jerusalem community led by James the Just.

## Overview

This project presents a critical text reconstruction of **Proto-Luke (the Jamesian Protograph)**—the hypothetical earliest stratum of the Third Gospel. The reconstruction applies the "New Marcionite Paradigm" which recognizes Marcion's *Evangelion* as a witness to a pre-canonical text rather than an edited mutilation of canonical Luke.

## Methodology

The reconstruction relies on three forensic vectors:

1. **Editorial Fatigue Analysis** — Where canonical Luke betrays expansion of a shorter source (e.g., the Capernaum reference in Luke 4:23 before Jesus visits Capernaum in canonical order)

2. **Triangulation of Witnesses** — Patristic testimony (Tertullian, Epiphanius, Adamantius) cross-referenced with the Western manuscript tradition (Codex Bezae, Old Latin)

3. **Western Non-Interpolations** — Passages present in Alexandrian manuscripts but absent in the Western tradition, identified by Westcott and Hort as later theological additions

## Excised Material

Material categorized as secondary redaction includes:
- Infancy narratives (Luke 1–2)
- Genealogy (Luke 3:23–38)
- Baptism and Temptation narratives
- Physicalist resurrection proofs (Luke 24:39–43)

These layers were added in the second century to anchor the primitive narrative in Davidic biology and anti-Docetic polemic.

## Key Scholarly Sources

- **Matthias Klinghardt**, *The Oldest Gospel and the Formation of the Canonical Gospels* (2015/2021)
- **Jason BeDuhn**, *The First New Testament: Marcion's Scriptural Canon* (2013)
- **Markus Vinzent**, *Christ's Resurrection in Early Christianity* (2011)

## Project Structure

```
├── data/
│   ├── proto_luke.json              # Primary source: Greek text, English translation, notes
│   └── THE GOSPEL (PROTO-LUKE)*.md  # Chapter markdown sources
├── docs/
│   └── research_questions.md        # Scholarly questions and resolutions
├── output/
│   └── Proto-Luke_Jamesian_Protograph.pdf  # Generated PDF
├── scripts/
│   ├── json_to_pdf.py               # PDF generation
│   ├── json_to_latex.py             # LaTeX generation
│   └── generate_text.py             # Text extraction
└── README.md
```

## Branching Strategy (GitFlow)

- **main** — Stable releases only
- **develop** — Active development and research
- **feature/** — New features or chapters
- **hotfix/** — Urgent fixes to main

## Output

The reconstruction is available as a formatted PDF: `output/Proto-Luke_Jamesian_Protograph.pdf`

## License

This scholarly reconstruction is provided for academic and research purposes.
