# pylint: disable=too-many-instance-attributes
# pylint: disable=attribute-defined-outside-init
import tkinter as ttk
from tkinter import constants, messagebox

from services.rsa_key import RsaKey
from services.rsa_service import RsaService
from services.prime_service import PrimeService
from services.encryption_decryption_service import EncryptAndDecrypt

class UI:

    def __init__(self, root):
        self.keys_generated = False
        self._root = root


    def start(self):
        """
        Luo ja näyttää käyttöliittymän.
        """

        head_label = ttk.Label(
            master=self._root, text="RSA-salausgeneraattori", font="Arial 20 bold")
        key_length_label = ttk.Label(
            master=self._root, text="Anna avainten pituus biteissä (min. 500 bittiä):", font=("Arial 12")) # pylint: disable=C0301
        self.key_length_entry = ttk.Entry(master=self._root)
        generate_button = ttk.Button(
            master=self._root, text="Luo avainpari", command=self.generate)

        encryptable_label = ttk.Label(
            master=self._root, text="Salattava viesti (max pituus 127 merkkiä):", font="Arial 12")
        self.encryptable_entry = ttk.Text(self._root, width=32,
                               height=7, font=("Arial 11"))

        encrypt_button = ttk.Button(
            master=self._root, text="Salaa viesti", command=self.encrypt)
        encrypted_label = ttk.Label(
            master=self._root, text="Salattu viesti:", font="Arial 12")
        self.encrypted_entry = ttk.Text(self._root, width=32,
                               height=7, font=("Arial 11"))

        decryptable_label = ttk.Label(
            master=self._root, text="Purettava viesti:", font="Arial 12")
        self.decryptable_entry = ttk.Text(self._root, width=32,
                               height=7, font=("Arial 11"))
        decrypt_button = ttk.Button(
            master=self._root, text="Pura salattu viesti", command=self.decrypt)

        decrypted_label = ttk.Label(
            master=self._root, text="Purettu viesti:", font="Arial 12")
        self.decrypted_entry = ttk.Text(self._root, width=32,
                               height=7, font=("Arial 11"))

        head_label.grid(row=0, column=0, columnspan=2,
                        sticky=(constants.W, constants.E))
        key_length_label.grid(row=2, column=0, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        self.key_length_entry.grid(row=2, column=1, sticky=(
            constants.W, constants.E), padx=5, pady=5)
        generate_button.grid(
            row=3, column=1, sticky=constants.W, padx=5, pady=5)

        encryptable_label.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.encryptable_entry.grid(row=5, column=0, sticky=constants.W)
        encrypt_button.grid(row=6, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        encrypted_label.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.encrypted_entry.grid(
            row=5, column=1, sticky=(constants.E, constants.W))

        decryptable_label.grid(row=7, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.decryptable_entry.grid(row=8, column=0, sticky=constants.W)

        decrypt_button.grid(row=9, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        decrypted_label.grid(row=7, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self.decrypted_entry.grid(
            row=8, column=1, sticky=(constants.E, constants.W))

        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        #self._root.grid_rowconfigure(0, minsize=60)

    @staticmethod
    def show_keys_generated():
        """
        Ilmoittaa avainten luomisesta.
        """

        messagebox.showinfo("RSA salaus", "Avainpari generoitu!")

    @staticmethod
    def show_key_entry_error():
        """
        Ilmoittaa virhesyötteestä.
        """

        messagebox.showerror("Error", "Avainten pituus pitää olla luku väliltä 500-5000.")

    @staticmethod
    def show_key_error():
        """
        Ilmoittaa viestin saalmisesta ilman generoituja avaimia
        """

        messagebox.showerror("Error", "Ei generoituja avaimia.")

    @staticmethod
    def show_encrypt_error():
        """
        Ilmoittaa virhesyötteestä.
        """

        messagebox.showerror("Error", "Viestin salaus epäonnistui.")

    @staticmethod
    def show_decrypt_error():
        """
        Ilmoittaa virhesyötteestä.
        """

        messagebox.showerror("Error", "Viestin purku epäonnistui.")


    def generate(self):
        """
        Kutsuu tarvittavia metodeita avainparin luomiseksi.
        """
        try:
            length = int(self.key_length_entry.get())
        except: # pylint: disable=bare-except
            self.show_key_entry_error()
            return
        if length < 500 or length > 5000:
            self.show_key_entry_error()
            return
        self.rsa_service = RsaService(int(length), PrimeService, RsaKey)
        self.rsa_service.generate_keys()
        self.key_length_entry.delete(0, ttk.END)
        self.keys_generated = True
        self.show_keys_generated()

    def encrypt(self):
        """
        Kutsuu tarvittavia metodeita viestin salaamiseksi ja ilmoittaa onnistumisesta käyttäjälle.
        """

        if not self.keys_generated:
            self.show_key_error()
            return
        message = str(self.encryptable_entry.get("1.0", "end-1c"))
        self.msg_size = len(message.encode())
        try:
            encrypted_message = EncryptAndDecrypt().encrypt(message, self.rsa_service.pub_key)
        except: # pylint: disable=bare-except
            self.show_encrypt_error()
            return
        self.encrypted_entry.insert(ttk.END, encrypted_message)
        self.decryptable_entry.insert(ttk.END, encrypted_message)

    def decrypt(self):
        """
        Kutsuu tarvittavia metodeita viestin purkamiseen ja ilmoittaa onnistumisesta käyttäjälle.
        """

        encrypted_message = self.decryptable_entry.get("1.0", "end-1c")
        try:
            decrypted_message = EncryptAndDecrypt().decrypt(
                int(encrypted_message), self.msg_size, self.rsa_service.pvt_key)
        except: # pylint: disable=bare-except
            self.show_decrypt_error()
            return
        self.decrypted_entry.insert(ttk.END, decrypted_message)
