import subprocess

def execute_code(code):
    try:
        # Execute the code using the exec function
        exec(code)

        # Return success message
        return "Code executed successfully."
    except Exception as e:
        # Return error message
        return str(e)

def execute_snippet(snippet):
    try:
        # Execute the snippet using the subprocess module
        process = subprocess.Popen(snippet, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Return the output and error messages
        return output.decode("utf-8"), error.decode("utf-8")
    except Exception as e:
        # Return error message
        return str(e)

code = """
def say_hello():
    print("Hello, world!")

say_hello()
"""

snippet = "python -c 'print(\"Hello, world!\")'"

code_output = execute_code(code)
snippet_output, snippet_error = execute_snippet(snippet)

print("Code execution output:", code_output)
print("Snippet output:", snippet_output)
print("Snippet error:", snippet_error
