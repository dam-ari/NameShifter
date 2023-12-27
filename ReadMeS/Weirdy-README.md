
# 🚀 PyNameShifter: The Ultimate Renaming Wizard 🧙‍♂️

Welcome to PyNameShifter, the magical tool that makes renaming files as fun as casting spells in a wizard's duel! 🪄✨

## Features

- **🔀 Replace String**: Turn `boring_filename.txt` into `exciting_filename.txt` with a flick of a wand!
- **🎩 Add Prefix**: Presto! Now it's `super_exciting_filename.txt`!
- **🎉 Add Suffix**: Abracadabra! It becomes `super_exciting_filename_the_sequel.txt`!
- **📁 Include Folders**: Why stop at files? Rename folders too and watch the magic unfold!
- **🌌 Apply to Child Folders**: Let the enchantment reach every corner of your directory kingdom!

## Usage

Just whisper the incantations below into your terminal crystal ball. 🔮

### Basic Spell Structure

```bash
python script.py [folder_path] [flags]
```

### Magical Flags

- `-rp` or `--replace`: Replace a string in names. 
  - Example: `-rp boring exciting`
- `-add-st-b` or `--add_start`: Add a prefix to names.
  - Example: `-add-st-b super_`
- `-add-st-e` or `--add_end`: Add a suffix to names.
  - Example: `-add-st-e _the_sequel`
- `-if` or `--include_folders`: Enchant folder names as well.
  - Usage: `-if`
- `-acf` or `--apply_child_folders`: Extend your magic to the subdirectories.
  - Usage: `-acf`

### Examples

1. **Turn your file names into a fairy tale**:
   ```bash
   python script.py /path/to/folder -rp dull fantastic
   ```

2. **Start a file name revolution**:
   ```bash
   python script.py /castle/great_hall -add-st-b Royal_ -if
   ```

3. **End the saga with a bang**:
   ```bash
   python script.py /path/to/adventure -add-st-e _Finale -acf
   ```

4. **Concoct a complex renaming potion**:
   ```bash
   python script.py /path/to/magicland -rp old new -add-st-b start_ -add-st-e _end -if -acf
   ```

## Installation 📦

### From PyPI

You can easily install PyNameShifter from the Python Package Index (PyPI) with a simple incantation in your terminal:

```bash
pip install PyNameShifter
```

Once installed, the magic of PyNameShifter is at your command line fingertips!

### Using the 'ns' Command

After installation, summon the powers of PyNameShifter directly from your terminal using the mystical `ns` command:

```bash
ns /path/to/your/folder -flags
```

For example, to transform all file names in `/path/to/magicland`:

```bash
ns /path/to/magicland -rp old new -add-st-b start_ -add-st-e _end -if -acf
```

Now go forth and rename with the might of a thousand wizards! 🧙🌟

## Contributing

Got a spell to add? Fork this repository, cast your enhancement, and submit a pull request. For major sorcery, please open a scroll (issue) first to discuss your magical ideas.

## License

This wizardry is released under the MIT License - free as a phoenix in flight!
