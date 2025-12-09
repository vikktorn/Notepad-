1. For each file (Swift / Kotlin) you run a macro that:

extracts only variable names (val/var/let/static let ... =)

deletes everything else

sorts names alphabetically



2. Then you use Compare on those two “name-only” tabs.



So you compare naming only, not whole code.


---

1. Regex we’ll use

Works for both Swift + Kotlin token lines like:

val graphSurface01 = Color(...)

public static let graphSurface01 = Color(...)


Keep only the name:

Find what:
^.*\b(?:val|var|let|static\s+let)\s+([A-Za-z_][A-Za-z0-9_]*).*$

Replace with:
\1


Then delete all lines that are not “just a name”:

Find what:
^(?![A-Za-z_][A-Za-z0-9_]*$).*$

Replace with:
(empty)



---

2. Record the macro once

Do this ONCE and save as e.g. ExtractNames:

1. Open one of your files (Swift or Kotlin).


2. Macro → Start Recording


3. Press Ctrl+A (select all).


4. Open Search → Replace…

Search mode: Regular expression

Find what:
^.*\b(?:val|var|let|static\s+let)\s+([A-Za-z_][A-Za-z0-9_]*).*$

Replace with:
\1

Click Replace All

Close dialog.



5. Open Search → Replace… again

Search mode: Regular expression

Find what:
^(?![A-Za-z_][A-Za-z0-9_]*$).*$

Replace with: (leave empty)

Replace All

Close dialog.



6. Remove empty lines:

Search → Replace…

Find what: ^\s*$

Replace with: (empty)

Search mode: Regular expression

Replace All, close.



7. Sort names:

Edit → Line Operations → Sort Lines Lexicographically Ascending



8. Macro → Stop Recording


9. Macro → Save Current Recorded Macro…

Name: ExtractNames

Give it a shortcut (e.g. Ctrl+Alt+E)




Now you have a macro that turns any Swift/Kotlin file into a sorted list of variable names.


---

3. Use it for comparison

For each side:

1. File → Open original:

Colors.swift



2. File → Save As… → Colors_names.txt (so you don’t destroy real file)


3. Run macro: Macro → ExtractNames (or your shortcut).



Repeat for Kotlin file:

1. Open ThemeColors.kt


2. Save As ThemeColors_names.txt


3. Run macro.



Now you have:

Colors_names.txt = sorted Swift names

ThemeColors_names.txt = sorted Kotlin names



---

4. Compare just the names

1. Open both *_names.txt files.


2. Plugins → Compare → Compare



Now Compare shows:

green / red only where names differ

missing names clearly visible

no noise from types, generics, etc.



---

If you send me 2–3 example lines from each file (Swift + Kotlin), I can tweak the regex to match your exact naming pattern (e.g. if you also have enum cases or nested objects).
