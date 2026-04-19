import json
import os

class MiniBank:
    DB_FILE = "user_data.txt"

    def __init__(self):
        self.main_userInfo = self.load_data()

    def load_data(self):
        if not os.path.exists(self.DB_FILE):
            return {}
        try:
            with open(self.DB_FILE, "r") as file:
                data = json.load(file)
                
                return {int(k): v for k, v in data.items()}
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save_data(self):
        with open(self.DB_FILE, "w") as file:
            json.dump(self.main_userInfo, file, indent=4)

    def firstOption(self):
        try:
            option = int(input("Press 1 to Login / Press 2 to Register / Press 3 to Exit: "))
            if option == 1:
                self.login()
            elif option == 2:
                self.register()
            elif option == 3:
                exit()
        except (ValueError, EOFError):
            pass

    def returnId(self, username):
        for uid, details in self.main_userInfo.items():
            if details["r_username"] == username:
                return uid
        return None

    def menu(self, loginId):
        try:
            menu_input = int(input("1: Transfer | 2: Withdraw | 4: Logout: "))
            if menu_input == 1:
                target_name = input("Enter Username: ")
                target_id = self.returnId(target_name)
                amount = int(input(f"Amount for {target_name}: "))
                
                if self.main_userInfo[loginId]["amount"] >= amount:
                    self.main_userInfo[loginId]["amount"] -= amount
                    self.main_userInfo[target_id]["amount"] += amount
                    self.save_data() 
                    print(f"Transfer Successful! New Balance: {self.main_userInfo[loginId]['amount']}")
        except (ValueError, KeyError, EOFError):
            print("Action failed.")

    def login(self):
        print("\n__________This is Login__________")
        try:
            l_username = input("username: ")
            l_password = int(input("passcode: "))
            loginId = self.returnId(l_username)
            if loginId and self.main_userInfo[loginId]["r_password"] == l_password:
                print("Login Successfully")
                self.menu(loginId)
            else:
                print("Login Failed")
        except (ValueError, EOFError):
            pass

    def register(self):
        print("This is Register")
        try:
            r_username = input("username: ")
            r_password = int(input("passcode: "))
            r_passcode1 = int(input("confirm: "))
            r_amount = int(input("amount: "))

            if r_password == r_passcode1:
                new_id = len(self.main_userInfo) + 1
                self.main_userInfo[new_id] = {
                    "r_username": r_username, 
                    "r_password": r_password, 
                    "amount": r_amount
                }
                self.save_data() 
                print("Register successfully!")
        except (ValueError, EOFError):
            pass

if __name__ == "__main__":
    bank = MiniBank()
    while True:
        bank.firstOption()
