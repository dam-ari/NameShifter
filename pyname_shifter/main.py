import os
import argparse

def rename_files(folder, replace, add_start, add_end, include_folders, apply_child_folders):
    for root, dirs, files in os.walk(folder):
        # If not applying to child folders, clear the dirs list
        if (not apply_child_folders) and (not include_folders):
            dirs.clear()

        # Process files
        for file in files:
            new_name = file
            if replace:
                new_name = new_name.replace(replace[0], replace[1])
            if add_start:
                new_name = add_start + new_name
            if add_end:
                name, ext = os.path.splitext(new_name)
                new_name = name + add_end + ext
            os.rename(os.path.join(root, file), os.path.join(root, new_name))

        # Process folders if include_folders is True
        if include_folders:
            for dir in dirs:
                new_name = dir
                if replace:
                    new_name = new_name.replace(replace[0], replace[1])
                if add_start:
                    new_name = add_start + new_name
                if add_end:
                    new_name += add_end
                os.rename(os.path.join(root, dir), os.path.join(root, new_name))

def main():
    parser = argparse.ArgumentParser(description="Rename files and folders in a directory.")
    parser.add_argument("folder", type=str, help="The folder to process")
    parser.add_argument("-rp", "--replace", nargs=2, help="Replace string: -rp string_a string_b")
    parser.add_argument("-add-st-b", "--add_start", type=str, help="Add string to start: -add-st-b string")
    parser.add_argument("-add-st-e", "--add_end", type=str, help="Add string to end: -add-st-e string")
    parser.add_argument("-if", "--include_folders", action="store_true", help="Include folder names in rename")
    parser.add_argument("-acf", "--apply_child_folders", action="store_true", help="Apply to child folders")

    args = parser.parse_args()

    rename_files(args.folder, args.replace, args.add_start, args.add_end, args.include_folders, args.apply_child_folders)

if __name__ == "__main__":
    main()
