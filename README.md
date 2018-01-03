# FolderIntegrator
Tool to integrate multi folders.

# Usage

With terminal command, adding folders as arguments creates single folder and integrate all files from folders into the single folder.

```bash
python core.py [folders]
```

## Before:
```
root_folder
    | - a
    |   |- a-a
    |   |- a-b
    | - b
    |   |- b-a
    |   |- b-b
    | - |- b-c
```

## After:
```
root_folder
    |- single_folder
    |   |- a-a
    |   |- a-b
    |   |- b-a
    |   |- b-b
    |   |- b-c
```