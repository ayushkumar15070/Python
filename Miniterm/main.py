import os
import tkinter as tk
from tkinter import scrolledtext


class MiniTerminal:

    def __init__(self, root):

        # ==========================================
        # WINDOW
        # ==========================================
        self.root = root

        self.root.title("MiniTerm")

        self.root.geometry("950x600")

        self.root.minsize(700, 450)

        self.root.configure(
            bg="black"
        )

        # ==========================================
        # CURRENT DIRECTORY
        # ==========================================

        self.current_directory = os.path.join(
            os.path.expanduser("~"),
            "MiniTerm"
        )

        # Create MiniTerm working directory
        os.makedirs(
            self.current_directory,
            exist_ok=True
        )

        # ==========================================
        # WRITING VARIABLES
        # ==========================================

        self.writing = False

        self.current_file = None

        self.file_content = []

        # ==========================================
        # TERMINAL OUTPUT
        # ==========================================

        self.output = scrolledtext.ScrolledText(
            self.root,
            bg="black",
            fg="white",
            insertbackground="white",
            selectbackground="gray",
            selectforeground="white",
            font=("Consolas", 12),
            wrap=tk.WORD,
            borderwidth=0
        )

        self.output.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=(10, 0)
        )

        self.output.config(
            state=tk.DISABLED
        )

        # ==========================================
        # INPUT AREA
        # ==========================================

        self.input_frame = tk.Frame(
            self.root,
            bg="black"
        )

        self.input_frame.pack(
            fill=tk.X,
            padx=10,
            pady=10
        )

        # ==========================================
        # PROMPT
        # ==========================================

        self.prompt = tk.Label(
            self.input_frame,
            text="MiniTerm >",
            bg="black",
            fg="white",
            font=("Consolas", 12),
            anchor="w"
        )

        self.prompt.pack(
            side=tk.LEFT
        )

        # ==========================================
        # COMMAND INPUT
        # ==========================================

        self.command_entry = tk.Entry(
            self.input_frame,
            bg="black",
            fg="white",
            insertbackground="white",
            selectbackground="gray",
            selectforeground="white",
            relief=tk.FLAT,
            font=("Consolas", 12)
        )

        self.command_entry.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True
        )

        # Press Enter
        self.command_entry.bind(
            "<Return>",
            self.execute_command
        )

        # ==========================================
        # STARTUP
        # ==========================================

        self.update_prompt()

        self.show_welcome()

        self.command_entry.focus()

    # =================================================
    # UPDATE PROMPT
    # =================================================

    def update_prompt(self):

        self.prompt.config(
            text=f"MiniTerm:{self.current_directory}>"
        )

    # =================================================
    # PRINT OUTPUT
    # =================================================

    def print_output(self, text=""):

        self.output.config(
            state=tk.NORMAL
        )

        self.output.insert(
            tk.END,
            text + "\n"
        )

        self.output.see(
            tk.END
        )

        self.output.config(
            state=tk.DISABLED
        )

    # =================================================
    # WELCOME MESSAGE
    # =================================================

    def show_welcome(self):

        self.print_output(
            "=============================================="
        )

        self.print_output(
            "                 MINITERM"
        )

        self.print_output(
            "          Your Personal Terminal"
        )

        self.print_output(
            "=============================================="
        )

        self.print_output()

        self.print_output(
            "Working directory:"
        )

        self.print_output(
            self.current_directory
        )

        self.print_output()

        self.print_output(
            "Type 'help' to see available commands."
        )

        self.print_output()

    # =================================================
    # EXECUTE COMMAND
    # =================================================

    def execute_command(self, event=None):

        command = self.command_entry.get().strip()

        # Clear input
        self.command_entry.delete(
            0,
            tk.END
        )

        if not command:
            return

        # =============================================
        # WRITING MODE
        # =============================================

        if self.writing:

            # Save the file
            if command.lower() == "save":

                self.save_file()

                return

            # Add line to file content
            self.file_content.append(
                command
            )

            self.print_output(
                "> " + command
            )

            return

        # =============================================
        # SHOW COMMAND
        # =============================================

        self.print_output(
            f"MiniTerm:{self.current_directory}> {command}"
        )

        # =============================================
        # SPLIT COMMAND
        # =============================================

        parts = command.split(
            maxsplit=1
        )

        command_name = parts[0].lower()

        argument = ""

        if len(parts) > 1:

            argument = parts[1].strip()

        # =============================================
        # HELP
        # =============================================

        if command_name == "help":

            self.show_help()

        # =============================================
        # LS
        # =============================================

        elif command_name == "ls":

            self.list_directory()

        # =============================================
        # CD
        # =============================================

        elif command_name == "cd":

            self.change_directory(
                argument
            )

        # =============================================
        # PWD
        # =============================================

        elif command_name == "pwd":

            self.print_output(
                self.current_directory
            )

        # =============================================
        # MKDIR
        # =============================================

        elif command_name == "mkdir":

            self.make_directory(
                argument
            )

        # =============================================
        # CREATE
        # =============================================

        elif command_name == "create":

            self.create_file(
                argument
            )

        # =============================================
        # WRITE
        # =============================================

        elif command_name == "write":

            self.start_writing(
                argument
            )

        # =============================================
        # SAVE
        # =============================================

        elif command_name == "save":

            self.print_output(
                "Nothing is currently being written."
            )

        # =============================================
        # DELETE
        # =============================================

        elif command_name == "delete":

            self.delete_file(
                argument
            )

        # =============================================
        # CLEAR
        # =============================================

        elif command_name == "clear":

            self.clear_terminal()

        # =============================================
        # EXIT
        # =============================================

        elif command_name == "exit":

            self.root.destroy()

            return

        # =============================================
        # UNKNOWN COMMAND
        # =============================================

        else:

            self.print_output(
                f"Unknown command: {command_name}"
            )

            self.print_output(
                "Type 'help' to see available commands."
            )

        self.print_output()

    # =================================================
    # HELP
    # =================================================

    def show_help(self):

        self.print_output(
            "Available commands:"
        )

        self.print_output()

        self.print_output(
            "ls"
        )

        self.print_output(
            "    List files and folders."
        )

        self.print_output()

        self.print_output(
            "cd <folder>"
        )

        self.print_output(
            "    Enter a folder."
        )

        self.print_output()

        self.print_output(
            "cd .."
        )

        self.print_output(
            "    Go to the parent folder."
        )

        self.print_output()

        self.print_output(
            "cd ."
        )

        self.print_output(
            "    Stay in the current folder."
        )

        self.print_output()

        self.print_output(
            "pwd"
        )

        self.print_output(
            "    Show current directory."
        )

        self.print_output()

        self.print_output(
            "mkdir <folder>"
        )

        self.print_output(
            "    Create a new folder."
        )

        self.print_output()

        self.print_output(
            "create <file>"
        )

        self.print_output(
            "    Create a new file."
        )

        self.print_output()

        self.print_output(
            "write <file>"
        )

        self.print_output(
            "    Write content into a file."
        )

        self.print_output()

        self.print_output(
            "save"
        )

        self.print_output(
            "    Save the file currently being written."
        )

        self.print_output()

        self.print_output(
            "delete <file>"
        )

        self.print_output(
            "    Delete a file."
        )

        self.print_output()

        self.print_output(
            "clear"
        )

        self.print_output(
            "    Clear the terminal."
        )

        self.print_output()

        self.print_output(
            "exit"
        )

        self.print_output(
            "    Close MiniTerm."
        )

    # =================================================
    # LS
    # =================================================

    def list_directory(self):

        try:

            items = os.listdir(
                self.current_directory
            )

            if not items:

                self.print_output(
                    "Directory is empty."
                )

                return

            # Sort folders/files alphabetically
            items.sort(
                key=str.lower
            )

            for item in items:

                full_path = os.path.join(
                    self.current_directory,
                    item
                )

                if os.path.isdir(full_path):

                    self.print_output(
                        f"[DIR]  {item}"
                    )

                else:

                    self.print_output(
                        f"[FILE] {item}"
                    )

        except Exception as error:

            self.print_output(
                f"Error: {error}"
            )

    # =================================================
    # CD
    # =================================================

    def change_directory(self, path):

        # No argument
        if not path:

            self.print_output(
                "Usage: cd <folder>"
            )

            return

        # =============================================
        # HANDLE HOME DIRECTORY
        # =============================================

        if path == "~":

            new_directory = os.path.expanduser(
                "~"
            )

        else:

            # =========================================
            # ABSOLUTE PATH
            # =========================================

            if os.path.isabs(path):

                new_directory = os.path.abspath(
                    path
                )

            # =========================================
            # RELATIVE PATH
            # =========================================

            else:

                new_directory = os.path.abspath(
                    os.path.join(
                        self.current_directory,
                        path
                    )
                )

        # =============================================
        # CHECK EXISTENCE
        # =============================================

        if not os.path.exists(new_directory):

            self.print_output(
                "Directory does not exist."
            )

            return

        # =============================================
        # CHECK DIRECTORY
        # =============================================

        if not os.path.isdir(new_directory):

            self.print_output(
                "That is a file, not a directory."
            )

            return

        # =============================================
        # CHANGE DIRECTORY
        # =============================================

        self.current_directory = new_directory

        self.update_prompt()

        self.print_output(
            "Changed directory to:"
        )

        self.print_output(
            self.current_directory
        )

    # =================================================
    # MKDIR
    # =================================================

    def make_directory(self, name):

        if not name:

            self.print_output(
                "Usage: mkdir <folder>"
            )

            return

        # Prevent accidental absolute paths
        if os.path.isabs(name):

            self.print_output(
                "Please provide a folder name or relative path."
            )

            return

        path = os.path.abspath(
            os.path.join(
                self.current_directory,
                name
            )
        )

        if os.path.exists(path):

            self.print_output(
                "Folder already exists."
            )

            return

        try:

            os.makedirs(
                path
            )

            self.print_output(
                f"Directory created: {name}"
            )

        except Exception as error:

            self.print_output(
                f"Error: {error}"
            )

    # =================================================
    # CREATE FILE
    # =================================================

    def create_file(self, filename):

        if not filename:

            self.print_output(
                "Usage: create <filename>"
            )

            return

        # Prevent accidental absolute paths
        if os.path.isabs(filename):

            self.print_output(
                "Please provide a file name or relative path."
            )

            return

        path = os.path.abspath(
            os.path.join(
                self.current_directory,
                filename
            )
        )

        if os.path.exists(path):

            self.print_output(
                "File already exists."
            )

            return

        try:

            # Create parent folders if needed
            parent_folder = os.path.dirname(
                path
            )

            os.makedirs(
                parent_folder,
                exist_ok=True
            )

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write("")

            self.print_output(
                f"File created: {filename}"
            )

        except Exception as error:

            self.print_output(
                f"Error: {error}"
            )

    # =================================================
    # WRITE FILE
    # =================================================

    def start_writing(self, filename):

        if not filename:

            self.print_output(
                "Usage: write <file>"
            )

            return

        # Prevent absolute paths
        if os.path.isabs(filename):

            self.print_output(
                "Please provide a relative file path."
            )

            return

        path = os.path.abspath(
            os.path.join(
                self.current_directory,
                filename
            )
        )

        # =============================================
        # CHECK FILE
        # =============================================

        if not os.path.exists(path):

            self.print_output(
                "File does not exist."
            )

            self.print_output(
                "Use 'create <file>' first."
            )

            return

        # =============================================
        # CHECK DIRECTORY
        # =============================================

        if os.path.isdir(path):

            self.print_output(
                "That is a directory, not a file."
            )

            return

        # =============================================
        # START WRITING
        # =============================================

        self.writing = True

        self.current_file = path

        self.file_content = []

        self.print_output()

        self.print_output(
            "=============================================="
        )

        self.print_output(
            f"Writing to: {filename}"
        )

        self.print_output(
            "Type your content below."
        )

        self.print_output(
            "Type 'save' when you are finished."
        )

        self.print_output(
            "=============================================="
        )

    # =================================================
    # SAVE FILE
    # =================================================

    def save_file(self):

        if not self.current_file:

            self.print_output(
                "No file is currently open."
            )

            return

        try:

            with open(
                self.current_file,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    "\n".join(
                        self.file_content
                    )
                )

            filename = os.path.basename(
                self.current_file
            )

            self.print_output()

            self.print_output(
                "=============================================="
            )

            self.print_output(
                f"File saved: {filename}"
            )

            self.print_output(
                "=============================================="
            )

        except Exception as error:

            self.print_output(
                f"Error saving file: {error}"
            )

        # Reset writing mode
        self.writing = False

        self.current_file = None

        self.file_content = []

        self.update_prompt()

    # =================================================
    # DELETE FILE
    # =================================================

    def delete_file(self, filename):

        if not filename:

            self.print_output(
                "Usage: delete <file>"
            )

            return

        # Prevent absolute paths
        if os.path.isabs(filename):

            self.print_output(
                "Please provide a file name or relative path."
            )

            return

        path = os.path.abspath(
            os.path.join(
                self.current_directory,
                filename
            )
        )

        # =============================================
        # CHECK EXISTENCE
        # =============================================

        if not os.path.exists(path):

            self.print_output(
                "File does not exist."
            )

            return

        # =============================================
        # ONLY DELETE FILES
        # =============================================

        if os.path.isdir(path):

            self.print_output(
                "Delete currently works only for files."
            )

            return

        # =============================================
        # DELETE
        # =============================================

        try:

            os.remove(
                path
            )

            self.print_output(
                f"File deleted: {filename}"
            )

        except Exception as error:

            self.print_output(
                f"Error deleting file: {error}"
            )

    # =================================================
    # CLEAR TERMINAL
    # =================================================

    def clear_terminal(self):

        self.output.config(
            state=tk.NORMAL
        )

        self.output.delete(
            "1.0",
            tk.END
        )

        self.output.config(
            state=tk.DISABLED
        )


# =====================================================
# START APPLICATION
# =====================================================

if __name__ == "__main__":

    root = tk.Tk()

    terminal = MiniTerminal(
        root
    )

    root.mainloop()