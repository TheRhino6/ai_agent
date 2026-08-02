import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        if valid_target_dir == False:
            raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            if os.path.isfile(item_path):
                print(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir=False")
            elif os.path.isdir(item_path):
                print(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir=True")
        if not os.path.isdir(target_dir):
            raise ValueError(f'Error: "{directory}" is not a directory')
        return f"Success: \"{directory}\" is within the working directory"
    except Exception as e:
        return f"Error: {str(e)}"