#!/usr/bin/env python3
"""
Build full-report.md from modular section files in SECTIONS folder
Auto-update CHANGELOG with commit info
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path

# Define the order of folders and files
SECTION_ORDER = [
    "SECTIONS/introduction/introduction-and-context.md",
    "SECTIONS/analysis-layers/0.IntroToAnalysis.md",
    "SECTIONS/analysis-layers/1.institutional-design.md",
    "SECTIONS/analysis-layers/2.judicial-gatekeeping.md",
    "SECTIONS/analysis-layers/3.professional-practice.md",
    "SECTIONS/analysis-layers/4.user-experience.md",
    "SECTIONS/analysis-layers/5.external-monitors.md",
    "SECTIONS/analysis-layers/6.cross-layer-synthesis.md",
    "SECTIONS/analysis-layers/7.children-epistemic-blindspot.md",
    "SECTIONS/reform-proposals/1.procedural-operational",
    "SECTIONS/reform-proposals/2.structural-philosophical",
    "SECTIONS/reform-proposals/3.meta-level-analysis.md",
    "SECTIONS/resources/glossary.md",
    "SECTIONS/resources/references.md",
]

def get_last_commit_info():
    """Get the last commit message and author"""
    try:
        commit_msg = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%s'], 
            encoding='utf-8'
        ).strip()
        author = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%an'], 
            encoding='utf-8'
        ).strip()
        return commit_msg, author
    except:
        return "Section updated", "NoEndsNoGains"

def update_changelog():
    """Add new entry to CHANGELOG.md"""
    today = datetime.now().strftime('%Y-%m-%d')
    commit_msg, author = get_last_commit_info()
    
    # Read existing changelog
    try:
        with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return
    
    # Find the table and insert new row after header
    new_entry = f"| {today} | — | {commit_msg} | @{author} |\n"
    
    # Find where to insert (after the first data row)
    for i, line in enumerate(lines):
        if '| 2025-11-03 |' in line:  # Find the first existing entry
            lines.insert(i + 1, new_entry)
            break
    
    # Write back
    with open('CHANGELOG.md', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✓ Updated CHANGELOG with: {commit_msg}")

def build_report():
    """Concatenate all section files into full-report.md"""
    output_file = "full-report.md"
    
    print("Building full-report.md from sections...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for section_path in SECTION_ORDER:
            if os.path.exists(section_path):
                print(f"  Adding: {section_path}")
                with open(section_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n")
            else:
                print(f"  WARNING: File not found: {section_path}")
        
        # Add CHANGELOG link at end
        outfile.write("---\n\n")
        outfile.write("## Revision History\n\n")
        outfile.write("See [CHANGELOG.md](CHANGELOG.md) for complete revision history.\n\n")
        outfile.write("---\n\n")
    
    print(f"Successfully built {output_file}")
    
    # Update changelog
    update_changelog()

if __name__ == "__main__":
    build_report()
