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


    def __saveContact(self):
        myContactsList = open(f"Z:\pycharm\MyScheduleApp\database\myEvents.txt", "r+")
        savingContact = (self.__name, '-', self.__email, '-', self.__phone_number, "\n")
        divisor = '-'
        for contact in myContactsList:
            currentContact = myContactsList[contact].split(divisor)
            if currentContact[0] == self.__name or currentContact[1] == self.__email or currentContact[2] == self.__phone_number:
                overwrite = input("You have already saved similar information, do you want to overwrite it?  (y - yes, n - no) \n")
                if overwrite == 'y':
                    continue
                else:
                    myContactsList.close()

            myContactsList.write(savingContact)
            myContactsList.close()