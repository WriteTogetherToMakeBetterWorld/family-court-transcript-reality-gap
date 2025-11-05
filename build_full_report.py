#!/usr/bin/env python3
"""
Build full-report.md from modular section files in SECTIONS folder
"""

import os
from pathlib import Path

# Define the order of folders and files
SECTION_ORDER = [
    # Introduction
    "SECTIONS/introduction/introduction-and-context.md",
    
    # Analysis Layers (in numbered order)
    "SECTIONS/analysis-layers/0.IntroToAnalysis.md",
    "SECTIONS/analysis-layers/1.institutional-design.md",
    "SECTIONS/analysis-layers/2.judicial-gatekeeping.md",
    "SECTIONS/analysis-layers/3.professional-practice.md",
    "SECTIONS/analysis-layers/4.user-experience.md",
    "SECTIONS/analysis-layers/5.external-monitors.md",
    "SECTIONS/analysis-layers/6.cross-layer-synthesis.md",
    "SECTIONS/analysis-layers/7.children-epistemic-blindspot.md",
    
    # Reform Proposals
    "SECTIONS/reform-proposals/1.procedural-operational",
    "SECTIONS/reform-proposals/2.structural-philosophical",
    "SECTIONS/reform-proposals/3.meta-level-analysis.md",
    
    # Resources
    "SECTIONS/resources/glossary.md",
    "SECTIONS/resources/references.md",
]

def build_report():
    """Concatenate all section files into full-report.md"""
    output_file = "full-report.md"
    
    print("Building full-report.md from sections...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for section_path in SECTION_ORDER:
            if os.path.exists(section_path):
                print(f"  Adding: {section_path}")
                with open(section_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write("\n\n")  # Add spacing between sections
            else:
                print(f"  WARNING: File not found: {section_path}")
    
    print(f"\n✅ Successfully built {output_file}")

if __name__ == "__main__":
    build_report()
