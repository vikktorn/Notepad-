import re
import sys
from pathlib import Path

# Rough keyword lists so we don't treat language keywords as "names"
SWIFT_KEYWORDS = {
    "class", "struct", "enum", "protocol", "extension",
    "func", "var", "let", "import", "if", "else", "switch",
    "case", "for", "while", "repeat", "return", "in", "do",
    "catch", "throw", "throws", "rethrows", "try", "guard",
    "where", "as", "is", "true", "false", "nil", "public",
    "private", "internal", "fileprivate", "open", "static",
    "self", "super", "associatedtype", "break", "continue"
}

KOTLIN_KEYWORDS = {
    "package", "import", "class", "interface", "object",
    "data", "sealed", "enum", "fun", "val", "var",
    "if", "else", "when", "for", "while", "do", "in",
    "is", "as", "null", "true", "false", "try", "catch",
    "finally", "throw", "return", "break", "continue",
    "this", "super", "public", "private", "internal",
    "protected", "override", "abstract", "open"
}

IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def extract_identifiers(text: str, keywords: set[str]) -> set[str]:
    ids: set[str] = set()
    for m in IDENT_RE.finditer(text):
        name = m.group(0)
        if name not in keywords:
            ids.add(name)
    return ids


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python compare_names.py <swift_file> <kotlin_file>")
        sys.exit(1)

    swift_path = Path(sys.argv[1])
    kotlin_path = Path(sys.argv[2])

    if not swift_path.is_file():
        print(f"Swift file not found: {swift_path}")
        sys.exit(1)
    if not kotlin_path.is_file():
        print(f"Kotlin file not found: {kotlin_path}")
        sys.exit(1)

    swift_text = swift_path.read_text(encoding="utf-8", errors="ignore")
    kotlin_text = kotlin_path.read_text(encoding="utf-8", errors="ignore")

    swift_ids = extract_identifiers(swift_text, SWIFT_KEYWORDS)
    kotlin_ids = extract_identifiers(kotlin_text, KOTLIN_KEYWORDS)

    only_swift = sorted(swift_ids - kotlin_ids)
    only_kotlin = sorted(kotlin_ids - swift_ids)
    common = sorted(swift_ids & kotlin_ids)

    print(f"Swift identifiers:  {len(swift_ids)}")
    print(f"Kotlin identifiers: {len(kotlin_ids)}")
    print(f"Common names:       {len(common)}")

    print("\n=== In Swift only ===")
    for name in only_swift:
        print(name)

    print("\n=== In Kotlin only ===")
    for name in only_kotlin:
        print(name)

    # If you want to see the overlap as well, uncomment:
    print("\n=== In BOTH ===")
    for name in common:
        print(name)


if __name__ == "__main__":
    main()
=IFERROR(INDEX(Kotlin!$A$2:$A$500; MATCH(A2; Kotlin!$A$2:$A$500; 0)); "")
