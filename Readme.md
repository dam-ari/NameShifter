
# PyNameShifter

This Python script, PyNameShifter, is designed to efficiently rename files and folders within a specified directory. It offers several flags to customize the renaming process, catering to various needs, such as adding prefixes/suffixes, replacing parts of file or folder names, and applying changes to subdirectories.

## Features

- **Replace String**: Change a specific substring in file/folder names.
- **Add Prefix**: Attach a prefix to the beginning of file/folder names.
- **Add Suffix**: Append a suffix to the end of file/folder names (before the file extension for files).
- **Include Folders**: Optionally include folder names in the renaming process.
- **Apply to Child Folders**: Recursively apply the renaming to all files and folders within subdirectories.

## Usage

First, ensure you have Python installed on your system. Then, you can run the script from the command line.

### Basic Command Structure

```bash
python script.py [folder_path] [flags]
```

### Flags

- `-rp` or `--replace`: Replace a substring in names. Requires two arguments (the string to be replaced and its replacement).
  - Example: `-rp oldstring newstring`
- `-add-st-b` or `--add_start`: Add a prefix to names.
  - Example: `-add-st-b prefix_`
- `-add-st-e` or `--add_end`: Add a suffix to names.
  - Example: `-add-st-e _suffix`
- `-if` or `--include_folders`: Apply renaming to folder names as well.
  - Usage: `-if` (no additional arguments needed)
- `-acf` or `--apply_child_folders`: Apply renaming recursively to all files/folders in subdirectories.
  - Usage: `-acf` (no additional arguments needed)

### Examples

1. **Replace a substring in file names within a folder**:
   ```bash
   python script.py /path/to/folder -rp oldstring newstring
   ```

2. **Add a prefix to file names and include folder names**:
   ```bash
   python script.py /path/to/folder -add-st-b cool_ -if
   ```

3. **Add a suffix to file names in all subdirectories**:
   ```bash
   python script.py /path/to/folder -add-st-e _v2 -acf
   ```

4. **Combine flags for complex renaming**:
   ```bash
   python script.py /path/to/folder -rp old new -add-st-b start_ -add-st-e _end -if -acf
   ```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This script is released under the MIT License.
