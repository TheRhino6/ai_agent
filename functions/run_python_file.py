import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_path, file_path))
        valid_target_file = os.path.commonpath([abs_path, target_file]) == abs_path
        if valid_target_file == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        comp_process = subprocess.run(command, cwd=abs_path, capture_output=True, text=True, timeout=30)
        rtn = None
        if comp_process.returncode != 0:
            rtn = f"Process exited with code {comp_process.returncode}"
        if not comp_process.stdout and not comp_process.stderr:
            emp = "No output produced"
        elif comp_process.stdout and not comp_process.stderr:
            emp = f"STDOUT:\n{comp_process.stdout}"
        elif not comp_process.stdout and comp_process.stderr:
            emp = f"STDERR:\n{comp_process.stderr}"
        else:
            emp = f"STDOUT:\n{comp_process.stdout}\nSTDERR:\n{comp_process.stderr}"
        return f"{rtn}\n{emp}" if rtn else emp

    except Exception as e:
        return f"Error: executing Python file: {str(e)}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a Python file in the specified directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional command-line arguments to pass to the script",
                },
            },
            "required": ["file_path"]
        },
    },
}