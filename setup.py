
import os, time, ctypes, subprocess, sys
import urllib.request

url = "https://github.com/Ceebox/cbLang/releases/download/0.1.2/cbLang.exe"
output_path = "cbLang.exe"
move_to_path = "C:\\Program Files\\cbLang"

def run(cmd):
    print(f"-> {cmd}")
    subprocess.run(cmd, shell=True)

def remove():
    SUCCESS_REMOVED = False
    try:
        run('assoc .cb=')
        run('ftype CBFile=')
        if os.path.exists(os.path.join(move_to_path, "cbLang.exe")):
            os.remove(os.path.join(move_to_path, "cbLang.exe"))
        if os.path.exists(move_to_path) and not os.listdir(move_to_path):
            os.rmdir(move_to_path)
        SUCCESS_REMOVED = True
    except Exception as e:
        print(f"Error removing registry entries or files: {e}")

    if SUCCESS_REMOVED:
        print("Register was removed")
        print("cbLang uninstalled successfully.")


def add():
    SUCCESS_DOWNLOAD = False
    SUCCESS_REGISTER = False

    print("Downloading cbLang...")
    try:
        urllib.request.urlretrieve(url, output_path)
        os.makedirs(move_to_path, exist_ok=True)
        os.replace(output_path, os.path.join(move_to_path, "cbLang.exe"))
        SUCCESS_DOWNLOAD = True
    except Exception as e:
        print(f"Error downloading cbLang: {e}")

    if SUCCESS_DOWNLOAD:
        print("cbLang installed successfully.")

    print("Register Filetype...")
    try:
        os.system('assoc .cb=CBFile')
        os.system(f'ftype CBFile="{os.path.join(move_to_path, "cbLang.exe")}" --run "%1"')
        SUCCESS_REGISTER = True
    except Exception as e:
        print(f"Error registering filetype: {e}")
        time.sleep(5)

    if SUCCESS_REGISTER:
        print("Filetype registered successfully.")

    print("Installation complete.")
    time.sleep(5)

def check_if_installed():
    return os.path.exists(os.path.join(move_to_path, "cbLang.exe"))

def main():
    print("Check if user is admin...")
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script must be run as administrator.")
        print("Restarting with admin privileges...")
        time.sleep(2)
        # Relaunch the script with admin rights
        params = ' '.join([f'"{arg}"' for arg in sys.argv])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        return
    while True:
        raw = input("Enter 'add' to install, 'remove' to uninstall or 'check' to verify installation: ")
        value = raw.strip().lower()
        if value == "add":
            add()
        elif value == "remove":
            if check_if_installed():
                remove()
            else:
                print("cbLang is not installed.")
        elif value == "check":
            if check_if_installed():
                print("cbLang is installed.")
            else:
                print("cbLang is not installed.")
        else:
            print("Invalid option.")

        time.sleep(2)
        os.system("cls")
        value = None

if __name__ == "__main__":
    main()