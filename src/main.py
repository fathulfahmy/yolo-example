import os
import subprocess

APPLICATION_DIR = os.path.dirname(__file__)


def hyphen_to_title_case(filename):
    name_without_extension = filename.replace(".py", "")
    words = name_without_extension.split("-")
    title_case_name = " ".join(word.capitalize() for word in words)
    return title_case_name


def list_application_files():
    application_files = [
        f for f in os.listdir(APPLICATION_DIR) if f.endswith(".py") and f != "main.py"
    ]
    return application_files


def run_application(application_file):
    print(f"Running {application_file}...")
    subprocess.run(["python", os.path.join(APPLICATION_DIR, application_file)])


def display_menu(application_files):
    print("\nUltralytics YOLO Applications\n")
    for idx, application_file in enumerate(application_files, 1):
        print(f"{idx}. {hyphen_to_title_case(application_file)}")
    print(f"{len(application_files) + 1}. Exit\n")


def main():
    while True:
        application_files = list_application_files()

        if not application_files:
            print("No application files found in the current directory.")
            break

        display_menu(application_files)

        try:
            selection = int(input("Select application: "))
            if selection == len(application_files) + 1:
                print("Exiting program...")
                break
            elif 1 <= selection <= len(application_files):
                run_application(application_files[selection - 1])
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Invalid selection, please enter a number.")


if __name__ == "__main__":
    main()
