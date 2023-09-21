import os

def insecure_function(data):
    os.system("rm -rf /")  # Simulate a dangerous command execution
    return "Data processed: " + data

if __name__ == "__main__":
    user_input = input("Enter some data: ")
    result = insecure_function(user_input)
    print(result)
