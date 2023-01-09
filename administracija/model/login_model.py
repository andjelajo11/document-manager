class LoginModel:
    def __init__(self, user_id=None, user_password=None, user_registered=False):
        self.user_id = user_id
        self.user_password = user_password
        self.user_registered = user_registered