# How to Co-Create Safely

**You cannot edit the main report directly** — `main` is protected.  
**You *can* safely add data, analyses, or ideas** — every contribution is credited in the public [Revision Log](./CHANGELOG.md).

---

## Consent to Use

**By submitting any file or analysis, you agree:**

- [ ] **I confirm** this is **my own or fully anonymized** content  
- [ ] **I agree** it can be used in this **public research**, cited, and shared  
- [ ] **No personal or child identifiers** are included

> *Only submit if all boxes are true.*

---

## 6 Layers of Truth – Where to Put Your Files

| Layer | What It Is | Folder | Example |
|-------|------------|--------|---------|
| **1** | **Forms, guidance, transcription companies** | `DATA/layer1_institutional/` | `EX160-form.pdf`, `TranscribeCo-pricing.xlsx` |
| **2** | **The ruling** (judgments, orders, bundles, skeleton arguments, position statements, etc.) | `DATA/layer2_judicial/` | `EWFC-2025-123.pdf`, `court-order-redacted.md` |
| **3** | **Practitioners** (solicitors, barristers, CAFCASS, Social Services) | `DATA/layer3_practitioner/` | `barrister-letter.docx`, `CAFCASS-wait-times.csv` |
| **4** | **Parents & litigants in person** | `DATA/layer4_LEAP/` | `anon-parent-timeline.txt`, `McKenzie-note.md` |
| **5** | **Advocacy, media, NGOs** | `DATA/layer5_NGOs_media/` | `WomenAid-report.pdf`, `BBC-article-link.md` |
| **6** | **Children’s views** (fully anonymized) | `DATA/layer6_childrensviews/` | `child-drawing-001.pdf`, `quote-age9.txt` |

---

## Your Analysis → `DATA/processed/`

- Save as: `DATA/processed/your-name-your-finding.md`
- Use this **template**:

```markdown
---
title: [Your Title]
author: @[your-github-name]
date: YYYY-MM-DD
layers: [1, 3, 6]
---

## Summary
One-sentence insight.

## Data Used
- `../layer1_institutional/...`
- `../layer6_childrensviews/...`
