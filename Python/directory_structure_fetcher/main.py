import os
from pathlib import Path

DEFAULT_EXCLUDES = {".git", ".github", "venv", "__pycache__", "node_modules"}

def is_hidden_or_unwanted(name: str, excluded: set[str]) -> bool:
    return name.startswith(".") or name in excluded

def write_tree(
    root: Path,
    file,
    prefix: str = "",
    excluded_dirs: set[str] = DEFAULT_EXCLUDES
):
    entries = sorted([
        entry for entry in root.iterdir()
        if not is_hidden_or_unwanted(entry.name, excluded_dirs)
    ], key=lambda e: (e.is_file(), e.name.lower()))

    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        file.write(f"{prefix}{connector}{entry.name}\n")

        if entry.is_dir():
            extension = "    " if index == len(entries) - 1 else "│   "
            write_tree(entry, file, prefix + extension, excluded_dirs)

def fetch_tree_structure(root_dir: Path, output_file: Path, excludes: set[str]) -> None:
    with output_file.open("w", encoding="utf-8") as f:
        f.write(f"{root_dir.name}/\n")
        write_tree(root_dir, f, excluded_dirs=excludes)

if __name__ == "__main__":
    root_input = input("Enter the root directory to scan (default: current folder): ").strip() or "."
    exclude_input = input(f"Enter folders to exclude, separated by commas (default: {', '.join(DEFAULT_EXCLUDES)}): ").strip()

    excludes = set(item.strip() for item in exclude_input.split(",")) if exclude_input else DEFAULT_EXCLUDES

    root_path = Path(root_input).resolve()
    output_path = Path(__file__).resolve().parent / "structure.txt"

    if not root_path.exists() or not root_path.is_dir():
        print(f"Error: '{root_path}' is not a valid directory.")
    else:
        fetch_tree_structure(root_path, output_path, excludes)
        print(f"✅ Tree structure written to: {output_path}")
