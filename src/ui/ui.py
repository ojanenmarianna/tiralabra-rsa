import tkinter as ttk
from tkinter import constants
from services.rsa_service import RsaService

class UI:

    def __init__(self, root):
        self.keys_generated = False
        self._root = root
        self.rsa_service = RsaService()


    def start(self):
        """
        Luo ja näyttää käyttöliittymän.
        """

        head_label = ttk.Label(self._root, text="RSA-salausgeneraattori")
        generate_button = ttk.Button(self._root, text="Luo avainpari", command=self.generate())

        message_label = ttk.Label(self._root, text="Salattava viesti:")
        message_entry = ttk.Text(self._root, width=25, height=6)

        encrypt_button = ttk.Button(self._root, text="Salaa viesti", command=self.encrypt())
        encrypted_label = ttk.Label(self._root, text="Salattu viesti:")
        encrypted_entry = ttk.Text(self._root, width=25, height=6)

        decrypt_label = ttk.Label(self._root, text="Purettava viesti:")
        decrypt_entry = ttk.Text(self._root, width=25, height=6)

        decrypt_button = ttk.Button(self._root, text="Pura viesti", command=self.decrypt())
        decrypted_label = ttk.Label(self._root, text="Purettu viesti:")
        decrypted_entry = ttk.Text(self._root, width=25, height=6)

        head_label.grid(row=0, column=0, columnspan=2,
                        sticky=(constants.W, constants.E))
        generate_button.grid(row=1, column=0, sticky=(constants.W, constants.E))

        message_label.grid(row=3, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        message_entry.grid(row=4, column=0, sticky=constants.W)

        encrypt_button.grid(row=5, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        encrypted_label.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        encrypted_entry.grid(
            row=4, column=1, sticky=(constants.E, constants.W))

        decrypt_label.grid(row=6, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        decrypt_entry.grid(row=7, column=0, sticky=constants.W)

        decrypt_button.grid(row=8, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        decrypted_label.grid(row=6, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        decrypted_entry.grid(
            row=7, column=1, sticky=(constants.E, constants.W))
    
    def generate(self):
        """
        Kutsuu tarvittavia metodeita avainparin luomiseksi.
        """
        self.rsa_service.generate_keys()
        self.keys_generated = True

    def encrypt(self):
        """
        Kutsuu tarvittavia metodeita viestin salaamiseksi.
        """
        pass

    def decrypt(self):
        """
        Kutsuu tarvittavia metodeita viestin purkamiseksi.
        """
        pass