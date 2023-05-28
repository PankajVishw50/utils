import os


def create_numbered_files(directory, prefix, extension, n):
    for i in range(1, n+1):
        filename = f"{prefix}{i}.{extension}"  # Customize the file extension if needed
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as file:
            file.write(f"This is file {i}")
        print(f"Created file: {filename}")

def rename_extensions(directory, extension, extension_type=None):
    if not os.path.isdir(directory):
        raise Exception("Invalid dir name")

    for file in os.listdir(path):
        original_path = os.path.join(directory, file)
        original_name = file[:file.rfind(".") if file.rfind(".") >= 0 else None]
        original_extension = file[file.find(".")+1 if file.find(".") >= 0 else -1:None if file.find(".") >= 0 else -1]

        if not extension_type or original_extension.lower() == extension_type.lower():
            new_name = original_name + "." + extension
            new_path = os.path.join(directory, new_name)

            os.rename(original_path, new_path)


path = r"D:\testing\data\files"

# create_numbered_files(path, "photo", "txt", 20)

rename_extensions(path, "zip")
