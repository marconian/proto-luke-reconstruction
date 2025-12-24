"""
Proto-Luke Text Generator
Converts the JSON structure into readable paragraph formats.
"""

import json
from pathlib import Path


def load_proto_luke(json_path: str) -> dict:
    """Load the Proto-Luke JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_english_text(data: dict, include_refs: bool = False) -> str:
    """Generate continuous English text with chapter breaks."""
    lines = []
    lines.append(f"# {data['title']}\n")
    lines.append(f"*{data['description']}*\n")
    lines.append("---\n")
    
    for chapter in data['chapters']:
        lines.append(f"\n## Chapter {chapter['chapter']}: {chapter.get('title', '')}\n")
        
        if chapter.get('preamble'):
            lines.append(f"*{chapter['preamble']}*\n")
        
        # Group verses into paragraphs (roughly every 3-5 verses or at natural breaks)
        paragraph = []
        for verse in chapter.get('verses', []):
            if include_refs:
                text = f"[{verse['canonical_ref']}] {verse['english']}"
            else:
                text = verse['english']
            paragraph.append(text)
        
        # Join as continuous paragraph
        lines.append(" ".join(paragraph) + "\n")
    
    return "\n".join(lines)


def generate_greek_text(data: dict, include_refs: bool = False) -> str:
    """Generate continuous Greek text with chapter breaks."""
    lines = []
    lines.append(f"# {data['title']} (GREEK)\n")
    lines.append("---\n")
    
    for chapter in data['chapters']:
        lines.append(f"\n## Κεφάλαιον {chapter['chapter']}\n")
        
        paragraph = []
        for verse in chapter.get('verses', []):
            if include_refs:
                text = f"[{verse['canonical_ref']}] {verse['greek']}"
            else:
                text = verse['greek']
            paragraph.append(text)
        
        lines.append(" ".join(paragraph) + "\n")
    
    return "\n".join(lines)


def generate_parallel_text(data: dict) -> str:
    """Generate side-by-side Greek and English (verse by verse)."""
    lines = []
    lines.append(f"# {data['title']} (PARALLEL TEXT)\n")
    lines.append(f"*{data['description']}*\n")
    lines.append("---\n")
    
    for chapter in data['chapters']:
        lines.append(f"\n## Chapter {chapter['chapter']}\n")
        
        if chapter.get('preamble'):
            lines.append(f"*{chapter['preamble']}*\n")
        
        for verse in chapter.get('verses', []):
            lines.append(f"### {chapter['chapter']}:{verse['verse']} ({verse['canonical_ref']})\n")
            lines.append(f"**Greek:** {verse['greek']}\n")
            lines.append(f"**English:** {verse['english']}\n")
    
    return "\n".join(lines)


def generate_verse_numbered(data: dict) -> str:
    """Generate traditional verse-numbered format."""
    lines = []
    lines.append(f"# {data['title']}\n")
    lines.append(f"*{data['description']}*\n")
    lines.append("---\n")
    
    for chapter in data['chapters']:
        lines.append(f"\n## Chapter {chapter['chapter']}\n")
        
        if chapter.get('preamble'):
            lines.append(f"*{chapter['preamble']}*\n")
        
        for verse in chapter.get('verses', []):
            # Superscript-style verse number
            lines.append(f"**{verse['verse']}** {verse['english']}")
        
        lines.append("")  # Blank line after chapter
    
    return "\n".join(lines)


def generate_critical_edition(data: dict) -> str:
    """Generate a critical edition format with notes inline."""
    lines = []
    lines.append(f"# {data['title']}\n")
    lines.append(f"## Critical Edition with Apparatus\n")
    lines.append(f"*{data['description']}*\n")
    lines.append("---\n")
    
    for chapter in data['chapters']:
        lines.append(f"\n## Chapter {chapter['chapter']}: {chapter.get('title', '')}\n")
        
        if chapter.get('preamble'):
            lines.append(f"### Preamble\n{chapter['preamble']}\n")
        
        lines.append("### Text\n")
        
        for verse in chapter.get('verses', []):
            lines.append(f"**{chapter['chapter']}:{verse['verse']}** ({verse['canonical_ref']})")
            lines.append(f"> {verse['greek']}")
            lines.append(f"> {verse['english']}\n")
        
        # Add notes section
        if chapter.get('notes'):
            lines.append("### Critical Notes\n")
            for note in chapter['notes']:
                lines.append(f"- **{note['term']}**: {note['explanation']}\n")
        
        # Add chapter notes if present
        if chapter.get('chapter_notes'):
            for cn in chapter['chapter_notes']:
                lines.append(f"#### {cn.get('title', 'Note')}\n")
                lines.append(f"{cn.get('explanation', '')}\n")
    
    return "\n".join(lines)


def generate_reading_text(data: dict) -> str:
    """Generate clean reading text without verse numbers (narrative flow)."""
    lines = []
    lines.append(f"# {data['title']}\n")
    lines.append(f"*{data['description']}*\n")
    lines.append("---\n")
    
    for chapter in data['chapters']:
        lines.append(f"\n## Chapter {chapter['chapter']}\n")
        
        if chapter.get('preamble'):
            lines.append(f"*{chapter['preamble']}*\n")
        
        # Combine verses into flowing paragraphs
        # Break at logical points (dialogue, scene changes)
        paragraph = []
        for verse in chapter.get('verses', []):
            text = verse['english']
            
            # Start new paragraph for direct speech or scene transitions
            if text.startswith('"') or text.startswith('And he said') or text.startswith('And Jesus'):
                if paragraph:
                    lines.append(" ".join(paragraph) + "\n")
                    paragraph = []
            
            paragraph.append(text)
        
        if paragraph:
            lines.append(" ".join(paragraph) + "\n")
    
    return "\n".join(lines)


def main():
    # Paths
    json_path = Path(__file__).parent.parent / "proto_luke.json"
    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Load data
    print(f"Loading {json_path}...")
    data = load_proto_luke(json_path)
    
    # Generate outputs
    formats = {
        "proto_luke_english.md": generate_english_text(data),
        "proto_luke_english_refs.md": generate_english_text(data, include_refs=True),
        "proto_luke_greek.md": generate_greek_text(data),
        "proto_luke_parallel.md": generate_parallel_text(data),
        "proto_luke_verses.md": generate_verse_numbered(data),
        "proto_luke_critical.md": generate_critical_edition(data),
        "proto_luke_reading.md": generate_reading_text(data),
    }
    
    for filename, content in formats.items():
        output_path = output_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated: {output_path}")
    
    print("\nDone! Generated formats:")
    print("  - english.md: Continuous English text")
    print("  - english_refs.md: English with canonical references")
    print("  - greek.md: Greek text only")
    print("  - parallel.md: Greek/English side by side")
    print("  - verses.md: Traditional verse-numbered format")
    print("  - critical.md: Critical edition with apparatus")
    print("  - reading.md: Clean narrative flow")


if __name__ == "__main__":
    main()
