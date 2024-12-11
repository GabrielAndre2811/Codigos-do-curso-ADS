def execute_code(code):
    try:
        result = eval(code)
        return result
    except Exception as e:
        return f"Error: {e}"

# Suposta entrada do usuário
malicious_input = "__import__('os').system('echo Malicious code executed!')"
output = execute_code(malicious_input)
print(output)
