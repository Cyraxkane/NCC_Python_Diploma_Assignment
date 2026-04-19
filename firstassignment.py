class MiniBank:
    main_userInfo: dict = {}

    def firstOption(self):
        option: int = int(input("Press 1 to Login / Press 2 to Register: "))
        if option == 1:
            self.login()
        else:
            self.register()

    def returnId(self, transfer_username):
        userInfo_length: int = len(self.main_userInfo)
        for i in range(1, userInfo_length + 1):
            if self.main_userInfo[i]["r_username"] == transfer_username:
                return i
        return None

    def menu(self, loginId):
        menu_input: int = int(input("Press 1 to Transfer / Press 2 to Withdraw / Press 3 to update user data: "))
        if menu_input == 1:
            transfer_username: str = input("Enter Username to transfer to: ")
            transfer_id: int = self.returnId(transfer_username)
            
            if transfer_id is None:
                print("User not found!")
                return

            print("\nWe get to Transfer ID:", transfer_id)
            print("myID:", loginId)

            amount: int = int(input("Enter amount to Transfer to {0}: ".format(self.main_userInfo[transfer_id]["r_username"])))
            
            if self.main_userInfo[loginId]["amount"] >= amount:
                self.main_userInfo[loginId]["amount"] -= amount
                self.main_userInfo[transfer_id]["amount"] += amount
                print("Transfer Successful! New Balance:", self.main_userInfo[loginId]["amount"])
            else:
                print("Insufficient balance!")

    def login(self):
        print("\n__________This is Login__________")
        l_username: str = input("pls enter username to login: ")
        l_password: int = int(input("please enter passcode to login: "))
        
        if self.exitUser(l_username, l_password):
            print("Login Successfully")
            loginId: int = self.returnId(l_username)
            self.menu(loginId)
        else:
            print("You cannot login. Incorrect username or password.")

    def exitUser(self, l_username, l_password):
        user_count = len(self.main_userInfo)
        for i in range(1, user_count + 1):
            if self.main_userInfo[i]["r_username"] == l_username and self.main_userInfo[i]["r_password"] == l_password:
                return True
        return False
    
    def register(self):
        print("This is Register")
        r_username: str = input("Enter username to register: ")
        r_password: int = int(input("Enter Passcode: "))
        r_passcode1: int = int(input("Enter Passcode Again: "))
        r_amount: int = int(input("Enter Amount: "))

        if r_password == r_passcode1:
            user_id: int = self.checkingUserCount()
            self.main_userInfo[user_id] = {"r_username": r_username, "r_password": r_password, "amount": r_amount}
            print("Register successfully!")
            print(self.main_userInfo)
        else:
            print("Passwords do not match!")

    def checkingUserCount(self):
        return len(self.main_userInfo) + 1

if __name__ == "__main__":
    miniBank: MiniBank = MiniBank()
    while True:
        miniBank.firstOption()
