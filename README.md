# FolderIntegrator
Tool to integrate multi folders.

# Usage

With terminal command, adding folders as arguments creates single folder and integrate all files from folders into the single folder.

```bash
python core.py [folders]
```

### Before:
```
root_folder
    | - a
    |   |- a-a
    |   |- a-b
    | - b
    |   |- b-a
    |   |- b-b
    |   |- b-c
```

### After:
```
root_folder
    |- single_folder
    |   |- a-a
    |   |- a-b
    |   |- b-a
    |   |- b-b
    |   |- b-c
```

# Credits

- Icon made by [Appzgear](https://www.flaticon.com/authors/appzgear) from www.flaticon.com 
- Icons made by [Smashicons](https://www.flaticon.com/authors/smashicons) from www.flaticon.com is licensed by [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/)