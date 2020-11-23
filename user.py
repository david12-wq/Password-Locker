class User:
    """
    Class that generates new instances of users.
    """

    user_list = []
    def __init__(self,first_name,second_name,username,password):
        self.first_name = first_name
        self.second_name = second_name
        self.username = username
        self.password = password

  