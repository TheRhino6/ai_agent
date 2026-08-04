import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path
        if valid_target_file == False:
            raise ValueError(f'Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_file):
            raise ValueError(f'Cannot write to "{file_path}" as it is a directory')
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a file relative to the working directory, creating directories as needed",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}