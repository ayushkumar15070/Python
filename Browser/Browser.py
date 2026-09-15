import socket
import tkinter as tk
from tkinter import scrolledtext


class Browser:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("My Browser")
        self.root.geometry("1000x700")

        # -------------------------
        # ADDRESS BAR
        # -------------------------

        self.address = tk.Entry(
            self.root,
            font=("Arial", 14)
        )

        self.address.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.address.bind(
            "<Return>",
            self.open_page
        )

        # -------------------------
        # PAGE AREA
        # -------------------------

        self.page = scrolledtext.ScrolledText(
            self.root,
            font=("Consolas", 11)
        )

        self.page.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=(0, 10)
        )

        self.address.insert(
            0,
            "example.com"
        )

    # =====================================
    # USER ENTERED URL
    # =====================================

    def open_page(self, event=None):

        url = self.address.get().strip()

        if not url:
            return

        # Remove protocol if supplied
        if url.startswith("http://"):
            url = url[7:]

        if url.startswith("https://"):
            url = url[8:]

        # Remove path for this first version
        host = url.split("/")[0]

        self.page.delete(
            "1.0",
            tk.END
        )

        self.page.insert(
            tk.END,
            "Connecting to " + host + "...\n\n"
        )

        try:

            html = self.download_page(host)

            self.page.delete(
                "1.0",
                tk.END
            )

            self.page.insert(
                tk.END,
                html
            )

        except Exception as error:

            self.page.insert(
                tk.END,
                "\n\nERROR:\n"
                + str(error)
            )

    # =====================================
    # DOWNLOAD PAGE
    # =====================================

    def download_page(self, host):

        # ---------------------------------
        # DNS
        # ---------------------------------

        ip = socket.gethostbyname(host)

        # ---------------------------------
        # TCP SOCKET
        # ---------------------------------

        connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        connection.settimeout(10)

        # ---------------------------------
        # CONNECT TO SERVER
        # ---------------------------------

        connection.connect(
            (ip, 80)
        )

        # ---------------------------------
        # HTTP REQUEST
        # ---------------------------------

        request = (
            "GET / HTTP/1.1\r\n"
            "Host: " + host + "\r\n"
            "Connection: close\r\n"
            "User-Agent: MyBrowser/0.1\r\n"
            "\r\n"
        )

        connection.send(
            request.encode()
        )

        # ---------------------------------
        # RECEIVE RESPONSE
        # ---------------------------------

        response = b""

        while True:

            data = connection.recv(4096)

            if not data:
                break

            response += data

        connection.close()

        # ---------------------------------
        # CONVERT BYTES → TEXT
        # ---------------------------------

        return response.decode(
            "utf-8",
            errors="replace"
        )


# =========================================
# START BROWSER
# =========================================

browser = Browser()

browser.root.mainloop()