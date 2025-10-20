#!/usr/bin/env python3
"""
Secure Enclave
--------------
This CLI application allows users to store encrypted artefacts.
It implements CRUD operations with role-based access control using secure coding practices.
"""

import argparse
import datetime
import getpass
import hashlib
import os
import sqlite3

import bcrypt  # External library for secure password hashing
from cryptography.fernet import Fernet  # External library: cryptography


# DbAdmin: Manages SQLite connection and queries
class DbAdmin:
    def __init__(self, db_path="artefacts.db"):
        self.db_path = db_path
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
        except Exception as e:
            print("Problem connecting to database:", e)
            raise

    def execute(self, query, params=()):
        try:
            cur = self.conn.cursor()
            cur.execute(query, params)
            self.conn.commit()
            return cur
        except Exception as e:
            print("DB execution problem:", e)
            raise

    def close(self):
        if self.conn:
            self.conn.close()


# EncryptionAdmin: Handles encryption/decryption
class EncryptionAdmin:
    def __init__(self, key_file="secret.key"):
        self.key_file = key_file
        self.key = self.load_key()
        self.cipher = Fernet(self.key)

    def load_key(self):
        try:
            if not os.path.exists(self.key_file):
                key = Fernet.generate_key()
                with open(self.key_file, "wb") as f:
                    f.write(key)
                return key
            else:
                with open(self.key_file, "rb") as f:
                    return f.read()
        except Exception as e:
            print("Problem loading encryption key:", e)
            raise

    def encrypt(self, data):
        try:
            return self.cipher.encrypt(data)
        except Exception as e:
            print("Encryption problem:", e)
            raise

    def decrypt(self, token):
        try:
            return self.cipher.decrypt(token)
        except Exception as e:
            print("Decryption problem:", e)
            raise


# Utility: Processes SHA-256 checksum
def calculate_checksum(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()


# User model and repository
class Person:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password  # plaintext during creation; will be hashed
        self.role = role


class UserVault:
    def __init__(self, db_admin: DbAdmin):
        self.db = db_admin
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password BLOB NOT NULL,
                role TEXT NOT NULL
            )
        """
        self.db.execute(query)

    def add_user(self, user: Person):
        try:
            hashed = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
            self.db.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (user.username, hashed, user.role),
            )
            print(f"User '{user.username}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"User '{user.username}' already exists.")
        except Exception as e:
            print("Problem adding user:", e)

    def authenticate(self, username, password):
        try:
            cur = self.db.execute(
                "SELECT id, password, role FROM users WHERE username=?", (username,)
            )
            row = cur.fetchone()
            if row and bcrypt.checkpw(password.encode(), row["password"]):
                return (row["id"], row["role"])
            return None
        except Exception as e:
            print("Authentication problem:", e)
            return None


# Artefact vault
class ArtefactVault:
    def __init__(self, db_admin: DbAdmin):
        self.db = db_admin
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS artefacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id INTEGER NOT NULL,
                file_name TEXT NOT NULL,
                file_path TEXT NOT NULL,
                checksum TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES users(id)
            )
        """
        self.db.execute(query)

    def add_artefact(
        self, owner_id, file_name, file_path, checksum, created_at, updated_at
    ):
        try:
            self.db.execute(
                "INSERT INTO artefacts (owner_id, file_name, file_path, checksum, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                (owner_id, file_name, file_path, checksum, created_at, updated_at),
            )
            print("Artefact created successfully with checksum:", checksum)
        except Exception as e:
            print("Problem creating artefact:", e)

    def get_artefact(self, artefact_id):
        try:
            cur = self.db.execute("SELECT * FROM artefacts WHERE id=?", (artefact_id,))
            return cur.fetchone()
        except Exception as e:
            print("Problem fetching artefact:", e)
            return None

    def update_artefact(self, artefact_id, file_path, checksum, updated_at):
        try:
            self.db.execute(
                "UPDATE artefacts SET file_path=?, checksum=?, updated_at=? WHERE id=?",
                (file_path, checksum, updated_at, artefact_id),
            )
            print("Artefact updated successfully with new checksum:", checksum)
        except Exception as e:
            print("Problem updating artefact:", e)

    def delete_artefact(self, artefact_id):
        try:
            self.db.execute("DELETE FROM artefacts WHERE id=?", (artefact_id,))
            print("Artefact deleted successfully.")
        except Exception as e:
            print("Problem deleting artefact:", e)

    def list_artefacts(self, owner_id=None):
        try:
            if owner_id:
                cur = self.db.execute(
                    "SELECT id, file_name, created_at FROM artefacts WHERE owner_id=?",
                    (owner_id,),
                )
            else:
                cur = self.db.execute("SELECT id, file_name, created_at FROM artefacts")
            return cur.fetchall()
        except Exception as e:
            print("Problem listing artefacts:", e)
            return []


# Artefact Admin: Handles file encryption and storage
class ArtefactAdmin:
    def __init__(self, encryption_admin: EncryptionAdmin):
        self.encryption_admin = encryption_admin

    def store_file(self, file_name, file_data, storage_dir="artefacts_files"):
        try:
            encrypted_data = self.encryption_admin.encrypt(file_data)
            if not os.path.exists(storage_dir):
                os.makedirs(storage_dir)
            file_path = os.path.join(storage_dir, file_name + ".enc")
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            return file_path
        except Exception as e:
            print("Problem storing file:", e)
            return None

    def read_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                return f.read()
        except Exception as e:
            print("Problem reading file:", e)
            return None


# Command-Line Interface (CLI)
def main():
    # Initialize managers
    db_admin = DbAdmin()
    encryption_admin = EncryptionAdmin()
    user_repo = UserVault(db_admin)
    artefact_repo = ArtefactVault(db_admin)
    artefact_admin = ArtefactAdmin(encryption_admin)

    parser = argparse.ArgumentParser(description="Secure Enclave")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Register command
    reg_parser = subparsers.add_parser("register", help="Register a new user")
    reg_parser.add_argument("--username", required=True, help="New username")
    reg_parser.add_argument("--password", required=True, help="Password")
    reg_parser.add_argument(
        "--role", required=True, choices=["admin", "user"], help="User role"
    )

    # Login command
    login_parser = subparsers.add_parser("login", help="Login as a user")
    login_parser.add_argument("--username", required=True, help="Username")
    login_parser.add_argument("--password", required=True, help="Password")

    # Add artefact command
    add_parser = subparsers.add_parser("add", help="Add a new artefact")
    add_parser.add_argument("--file", required=True, help="Path to the file")
    add_parser.add_argument("--name", required=True, help="Artefact name")

    # View artefact command
    view_parser = subparsers.add_parser("view", help="View an artefact")
    view_parser.add_argument("--id", type=int, required=True, help="Artefact ID")

    # Update artefact command
    update_parser = subparsers.add_parser("update", help="Update an existing artefact")
    update_parser.add_argument("--id", type=int, required=True, help="Artefact ID")
    update_parser.add_argument("--file", required=True, help="Path to the new file")

    # Delete artefact command
    delete_parser = subparsers.add_parser("delete", help="Delete an artefact")
    delete_parser.add_argument("--id", type=int, required=True, help="Artefact ID")

    # List artefacts command
    list_parser = subparsers.add_parser("list", help="List artefacts")

    args = parser.parse_args()

    # Process commands
    if args.command == "register":
        user = Person(args.username, args.password, args.role)
        user_repo.add_user(user)
    elif args.command == "login":
        user = user_repo.authenticate(args.username, args.password)
        if user:
            print("Login successful. Role:", user[1])
        else:
            print("Invalid credentials.")
    else:
        # For artefact operations, prompt for credentials
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        current_user = user_repo.authenticate(username, password)
        if not current_user:
            print("Authentication problem.")
            return

        if args.command == "add":
            try:
                with open(args.file, "rb") as f:
                    file_data = f.read()
                file_path = artefact_admin.store_file(args.name, file_data)
                if file_path is None:
                    return
                checksum = calculate_checksum(file_data)
                now = datetime.datetime.now().isoformat()
                artefact_repo.add_artefact(
                    current_user[0], args.name, file_path, checksum, now, now
                )
            except FileNotFoundError:
                print("File not found.")
        elif args.command == "view":
            artefact = artefact_repo.get_artefact(args.id)
            if artefact:
                if (
                    current_user[1] != "admin"
                    and current_user[0] != artefact["owner_id"]
                ):
                    print("Access denied: You do not shall not see this artefact.")
                    return
                file_data = artefact_admin.read_file(artefact["file_path"])
                if file_data:
                    try:
                        decrypted_data = encryption_admin.decrypt(file_data)
                        print("Artefact:", artefact["file_name"])
                        print("Checksum:", artefact["checksum"])
                        print("Created At:", artefact["created_at"])
                        print("Updated At:", artefact["updated_at"])
                        print("File Content (first 200 bytes):", decrypted_data[:200])
                    except Exception as e:
                        print("Problem decrypting file:", e)
            else:
                print("Artefact not found.")
        elif args.command == "update":
            artefact = artefact_repo.get_artefact(args.id)
            if not artefact:
                print("Artefact not found.")
                return
            if current_user[1] != "admin" and current_user[0] != artefact["owner_id"]:
                print("Access denied: You shall not update this artefact.")
                return
            try:
                with open(args.file, "rb") as f:
                    new_file_data = f.read()
                new_file_path = artefact_admin.store_file(
                    artefact["file_name"], new_file_data
                )
                new_checksum = calculate_checksum(new_file_data)
                now = datetime.datetime.now().isoformat()
                artefact_repo.update_artefact(args.id, new_file_path, new_checksum, now)
            except FileNotFoundError:
                print("File not found.")
        elif args.command == "delete":
            artefact = artefact_repo.get_artefact(args.id)
            if not artefact:
                print("Artefact not found.")
                return
            if current_user[1] != "admin" and current_user[0] != artefact["owner_id"]:
                print("Access denied: You shall not delete this artefact.")
                return
            artefact_repo.delete_artefact(args.id)
            try:
                if os.path.exists(artefact["file_path"]):
                    os.remove(artefact["file_path"])
            except Exception as e:
                print("Problem removing file:", e)
        elif args.command == "list":
            if current_user[1] == "admin":
                artefacts = artefact_repo.list_artefacts()
            else:
                artefacts = artefact_repo.list_artefacts(current_user[0])
            if artefacts:
                for row in artefacts:
                    print(
                        "ID:",
                        row["id"],
                        "Name:",
                        row["file_name"],
                        "Created At:",
                        row["created_at"],
                    )
            else:
                print("No artefacts found.")
        else:
            parser.print_help()


if __name__ == "__main__":

    main()
