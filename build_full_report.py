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
    
    # All reform-proposals and resource files at the end in your order:
    "SECTIONS/reform-proposals/1.procedural-operational.md",
    "SECTIONS/reform-proposals/2.structural-philosophical.md",
    "SECTIONS/reform-proposals/3.meta-leval-analysis.md",  # Ensure spelling matches filename!
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
        return "Content updated", "NoEndsNoGains"

def update_changelog():
    """Add new entry to CHANGELOG.md"""
    today = datetime.now().strftime('%Y-%m-%d')
    commit_msg, author
