class Contact:
    """
        A class that instance a contact.

    """

    def __init__(self, name, phone_number):
        """
        The constructor ensures that the minimum information is presented.


        :param name: String
        :param phone_number: String (00000-0000) - expected a number with "-" in the middle of the information
        """

        self.__name = name
        self.__email = ''
        self.__phone_number = phone_number

        print("The class 'Contact' was successfully instantiated.")
        pass

    def setName(self, name):
        """
        A Set method to change the attribute 'name'.
        """
        self.__name = name
        pass

    def setEmail(self, email):
        """
        A Set method to change the attribute 'email'.
        """
        self.__email = email
        pass

    def setPhoneNumber(self, phone_number):
        """
        A Set method to change the attribute 'phone_number'.
        """
        self.__phone_number = phone_number
        pass

    def getName(self):
        """
        A get method to display the "name" attribute.
        """
        print("Contact Name:", self.__name)
        pass

    def getEmail(self):
        """
        A get method to display the "email" attribute.
        """
        print("Email for contact:", self.__email)
        pass

    def getPhoneNumber(self):
        """
        A get method to display the "phone_number" attribute.
        """
        print("Phone number:", self.__phone_number)
        pass

    def showContact(self):
        """
        A get method to display all the informations of the contact.
        """
        print("Name:", self.__name)
        print("Email for contact:", self.__email)
        print("Phone number:", self.__phone_number)
        print("===================================================\n")
