
class Token:
    """Class which contains token for telegram bot."""

    # Security token for telegram bot.
    __token = '661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0'

    def __init__(self, token=__token):
        self.__token = token

    @property
    def user_token(self, __token):
        return self.__token

    def __str__(self):
        return self.__token
