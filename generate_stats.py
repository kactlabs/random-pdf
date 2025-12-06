#!/usr/bin/env python3
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def get_folder_stats(folder_path):
    """Get statistics for PDF files in a folder recursively"""
    stats = {
        'folder': folder_path.name,
        'pdf_count': 0,
        'total_size': 0,
        'files': []
    }
    
    if not folder_path.exists():
        return stats
    
    # Recursively find all PDF files
    for file in folder_path.rglob('*.pdf'):
        if file.is_file():
            size = file.stat().st_size
            stats['pdf_count'] += 1
            stats['total_size'] += size
            stats['files'].append({
                'name': file.name,
                'size': size
            })
    
    return stats

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def generate_stats():
    """Generate statistics for all PDF folders"""
    base_path = Path('.')
    folders = ['misc', 'resumes', 'us_pdf']
    
    all_stats = []
    total_pdfs = 0
    total_size = 0
    
    for folder_name in folders:
        folder_path = base_path / folder_name
        stats = get_folder_stats(folder_path)
        all_stats.append(stats)
        total_pdfs += stats['pdf_count']
        total_size += stats['total_size']
    
    # Generate markdown table
    markdown = "# Random PDF Collection\n\n"
    markdown += "## PDF Statistics\n\n"
    markdown += "| Folder | PDF Count | Total Size |\n"
    markdown += "|--------|-----------|------------|\n"
    
    for stats in all_stats:
        markdown += f"| {stats['folder']} | {stats['pdf_count']} | {format_size(stats['total_size'])} |\n"
    
    markdown += f"| **Total** | **{total_pdfs}** | **{format_size(total_size)}** |\n\n"
    markdown += f"*Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
    
    # Write to README
    with open('README.md', 'w') as f:
        f.write(markdown)
    
    print(f"Stats generated successfully!")
    print(f"Total PDFs: {total_pdfs}")
    print(f"Total Size: {format_size(total_size)}")

if __name__ == '__main__':
    generate_stats()
