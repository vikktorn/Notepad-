# Token Name Extraction & Comparison (Swift + Kotlin) in Notepad++

This guide explains how to extract token names from Swift and Kotlin files using Notepad++, clean them, sort them, and compare them using the Compare plugin.

---

## 1. Extract Names From Swift File

Swift lines look like:

static var surfaceBackground: Color { ... }
static let graphSurface01Static = color(name: "graphSurface01")

We want to extract only the variable names.

Open: Search → Replace…

Find what:
^\s*static\s+(?:var|let)\s+([A-Za-z_][A-Za-z0-9_]*)[:\s=]

Replace with:
\1

Settings:
Search mode: Regular expression
Wrap around: Yes
In selection: No

Click: Replace All

---

## 2. Clean the Extracted Swift Output

Remove everything except clean names.

Step A — Remove Non-Name Lines

Find what:
^(?![A-Za-z_][A-Za-z0-9_]*$).*

Replace with:
(leave empty)

Replace All.

Step B — Remove Empty Lines

Find what:
^\s*$

Replace with:
(leave empty)

Replace All.

Step C — Sort Swift Names

Edit → Line Operations → Sort Lines Lexicographically Ascending

---

## 3. Extract Names From Kotlin File

Kotlin lines look like:

val graphSurface01Static = Color(...)

Extract the identifier before '='.

Open: Search → Replace…

Find what:
^\s*val\s+([A-Za-z_][A-Za-z0-9_]*)\s*=

Replace with:
\1

Settings:
Search mode: Regular expression
Wrap around: Yes
In selection: No

Click: Replace All

---

## 4. Clean the Extracted Kotlin Output

Step A — Remove Non-Name Lines

Find what:
^(?![A-Za-z_][A-Za-z0-9_]*$).*

Replace with:
(leave empty)

Replace All.

Step B — Remove Empty Lines

Find what:
^\s*$

Replace with:
(leave empty)

Replace All.

Step C — Sort Kotlin Names

Edit → Line Operations → Sort Lines Lexicographically Ascending

---

## 5. Compare Swift vs Kotlin Names

Open both cleaned files:

Swift_names.txt  
Kotlin_names.txt

Then run:

Plugins → Compare → Compare

This produces a clean, line-by-line naming diff without any code noise.

---

## Finished

You now have a reproducible workflow to validate naming consistency between Swift and Kotlin token files using Notepad++.
