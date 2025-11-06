import os
import xml.etree.ElementTree as ET

# The script uses only the standard library (xml.etree.ElementTree), so no additional packages are required. Created by me -  AR Rahman
def find_strings_file(folder):
    """Return the path to strings.xml inside a folder, or None if not found."""
    for file in os.listdir(folder):
        if file.lower() == "strings.xml":
            return os.path.join(folder, file)
    return None

def load_strings(file_path):
    """Load strings.xml and return a dictionary of key -> value"""
    tree = ET.parse(file_path)
    root = tree.getroot()
    strings_dict = {}
    for string in root.findall('string'):
        key = string.get('name')
        value = string.text if string.text else ''
        strings_dict[key] = value
    return strings_dict

def compare_strings(original_folder, translated_folder):
    original_file = find_strings_file(original_folder)
    translated_file = find_strings_file(translated_folder)

    if not original_file:
        print(f"Error: No strings.xml found in {original_folder}")
        return
    if not translated_file:
        print(f"Error: No strings.xml found in {translated_folder}")
        return

    original = load_strings(original_file)
    translated = load_strings(translated_file)

    missing_keys = [key for key in original if key not in translated]

    total = len(original)
    translated_count = total - len(missing_keys)
    percent = (translated_count / total) * 100

    print(f"Total strings: {total}")
    print(f"Translated strings: {translated_count}")
    print(f"Missing translations: {len(missing_keys)}")
    print(f"Translation completion: {percent:.2f}%\n")

    if missing_keys:
        print("Missing keys:")
        for key in missing_keys:
            print(f"- {key}")
    else:
        print("All keys are translated. ✅ 100% complete.")

if __name__ == "__main__":
    original_folder = "values"
    # change folder name here
    translated_folder = "values-bn"
    compare_strings(original_folder, translated_folder)
