
from pathlib import Path
import hashlib


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    file_path = input("Enter file name or path: ").strip()
    target_file = Path(file_path)

    if not target_file.is_file():
        print("Error: File not found!")
        return

    baseline_file = Path(str(target_file) + ".sha256")
    current_hash = calculate_sha256(target_file)

    if baseline_file.exists():
        saved_hash = baseline_file.read_text().strip()

        if current_hash == saved_hash:
            print("STATUS: File is unchanged.")
            print("SHA-256:", current_hash)
        else:
            print("WARNING: File has been modified!")
            print("Original hash:", saved_hash)
            print("Current hash: ", current_hash)

    else:
        baseline_file.write_text(current_hash + "\n")
        print("Baseline created successfully!")
        print("SHA-256:", current_hash)
        print("Run again later to check file integrity.")


if __name__ == "__main__":
    main()
