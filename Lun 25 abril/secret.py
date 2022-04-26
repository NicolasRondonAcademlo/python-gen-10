class SecretString:
    """
    A not-at-all secure way to store a secret string
    """

    def __init__(self, plain_string: str, pass_prhase: str) -> None:
        self.__plain_string = plain_string
        self.__pass_prhase = pass_prhase

    def decrypt(self, pass_phrase: str) -> str:
        """
        Only show the string if the pass prahse is correct
        """
        if pass_phrase == self.__pass_prhase:
            return self.__plain_string
        else:
            return ""


secret_string = SecretString("ACME: Top Secret", "antwerp")
print(secret_string.decrypt("antwerp"))
# print(secret_string.__plain_string)
print(secret_string._SecretString__plain_string)

