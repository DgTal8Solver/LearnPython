def main():
    import platform
    import sys
    import os

    path = os.path.join(
        os.path.dirname(__file__), 
        "os_info.txt"
    )
    with open(path, 'w', encoding = "utf-8") as file:
        file.write(f"OS info is \n{platform.system()}\nPython version is {sys.version}")

if __name__ == "__main__":
    main()