#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# CBuffalow, 2021-Mar-06, added code to class CD, added save/load 
#    inventory functions to FileIO class, and added code to IO class
# CBuffalow, 2021-Mar-06, added code to main body, added __str__ method to CD class
# CBuffalow, 2021-Mar-06, updated docstrings, changed from dat to txt data 
#   storage,  added file_string function
# CBuffalow, 2021-Mar-07, updated save_inventory function
#------------------------------------------#

# -- DATA -- #
#Global Variables
strFileName = 'cdInventory.txt'  # text storage file
lstOfCDObjects = [] # table to hold data (list of objects)
strChoice = '' # user input (string)
strYesNo = '' # user input for yes/no question (string)
intID = 0 # ID number of CD (integer)
strTitle = '' # user input (string)
strArtist = '' # user input (string)
cdObj = None # object with CD info

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__ (): returns a formatted string with cd_id, cd_title, and cd_artist
        file_string(): returns a formatted string with cd_id, cd_title, and cd_artist for txt file
    """
    
    # -- Fields -- #
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
    #    -- Attributes -- #
        self.__cd_id = None
        self.__cd_title = None
        self.__cd_artist = None
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist
    
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, new_id):
        if type(new_id) == int:
            self.__cd_id = new_id
        else:
            raise Exception('This is not an integer.')
            
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, new_title):
        if type(new_title) == str:
            self.__cd_title = new_title
        else:
            raise Exception('This is not a string.')
            
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, new_artist):
        if type(new_artist) == str:
            self.__cd_artist = new_artist
        else:
            raise Exception('This is not a string.')
    
    # -- Methods -- #
    def __str__(self):
        """Returns a formatted string with cd_id, cd_title, and cd_artist
                
        Args:
            None.
        
        Returns:
            cdRow (str): CD Info in string formatted for display
        
        """
        cdRow = '{:<10}{:<25}{:<25}'.format(str(self.cd_id), self.cd_title, self.cd_artist)
        return cdRow
    
    def file_string(self):
        """Returns a formatted string with cd_id, cd_title, and cd_artist for a text file
        
        Args:
            None.
        
        Returns:
            fileRow (str): CD Info in string formatted for comma-separated txt file
        
        """
        fileRow = '{},{},{}\n'.format(str(self.cd_id), self.cd_title, self.cd_artist)
        return fileRow

            
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties: None

    methods:
        save_inventory(file_name, table): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    # -- Fields -- #
    # -- Constructor -- #
    #    -- Attributes -- #
    # -- Properties -- #
    # -- Methods -- #
    
    @staticmethod
    def save_inventory(file_name, table):
        """Function to write data from current runtime into a text file.

        For each row, the data is converted into a string with a comma separating
        each piece of data and then a new line is started.  The data is then saved
        out to the designated txt file.

        Args:
            file_name (string): name of file used to write data to
            table (list of objects): 2D data structure (list of objects) that holds data during runtime

        Returns:
            None.
        """
        try:
            objFile = open(file_name, 'w')
            for obj in table:
                objFile.write(obj.file_string())
            objFile.close()
        except Exception as e: #if there is a general error with the save process
            print('There has been a ', type(e), ' error with the save process. File not saved.')
    
    
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects

        Function checks to make sure specified txt file exists.  If yes, continues by reading
        the data from file identified by file_name into a 2D table
        (list of objects) table. One line in the file represents one row in table.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime
        """
        table = []
        try: 
            objFile = open(file_name, 'r')
            for row in objFile:
                data = row.strip().split(',')
                obj = CD(int(data[0]), data[1], data[2])
                table.append(obj)
            objFile.close()
        except FileNotFoundError:
            print('File not found. Inventory is still empty.')
        except Exception as e:
            print('There has been a ', type(e), ' error with the read process. Inventory is still empty.')
        return table

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output

    properties: None

    methods:
        print_menu(): -> None
        menu_choice(): -> (string of choice)
        show_inventory(a list of CD objects): -> None
        get_cd_data(): _> (integer of cd_id, str of cd_title, str of cd_artist)
    """
    # -- Fields -- #
    # -- Constructor -- #
    #    -- Attributes -- #
    # -- Properties -- #
    # -- Methods -- #
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user.

        Args:
            None.

        Returns:
            None.
        """
        print('\n')
        print(' MENU '.center(30,'-'))
        print('[L] Load Inventory from file\n[A] Add CD\n[I] Display Current Inventory')
        print('[S] Save Inventory to file\n[X] Exit')
        print('-'*30)
        print('\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection.

        Args:
            None.

        Returns:
            choice (string): an upper case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['L', 'A', 'I', 'S', 'X', 'l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [L, A, I, S or X]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table.


        Args:
            table (list of obj): 2D data structure (list of obj) that holds the data during runtime.

        Returns:
            None.

        """
        print('\n')
        print(' The Current Inventory: '.center(60,'='))
        print('{:<10}{:<25}{:<25}'.format('ID', 'CD Title', 'Artist'))
        print('-'*60)
        for row in table:
            print(row)
        print('='*60)

    @staticmethod
    def get_cd_data():
        """Collects information about CD from user.

        Asks user to input the name of the CD and the artist of the CD.

        Args:
            None

        Returns:
            cd_id (int): ID number of CD, provided by user
            cd_title (str): name of CD, provided by user
            cd_artist (str): name of artist, provided by user

        """
        try: 
            cd_id = int(input('What is the CD\'s ID Number? '))
            cd_title = input('What is the CD\'s title? ')
            cd_artist = input('What is the CD\'s artist? ')
            return cd_id, cd_title, cd_artist
        except ValueError: #if user enters a non-integer for cd_id
            print('The number you entered for the CD\'s ID is not an integer.')
        except Exception as e: #if user manages to cause an error with their input
            print('You have entered an response that caused a ', type(e),' error.')


# -- Main Body of Script -- #

# 0 general blanket try/except block around main script to catch anything I missed
try:
# 1. When program starts, read in the currently saved inventory, print program header
    lstOfCDObjects = FileIO.load_inventory(strFileName)
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('The Magic CD Inventory'.center(62))
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 2. start main loop
    while True:
        # 2.1 Display Menu to user and get choice
        IO.print_menu()
        strChoice = IO.menu_choice()
        # 3. Process menu selection
        # 3.1 process exit first
        if strChoice == 'x':
            print('Goodbye!')
            break
        # 3.2 process load inventory
        if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory will be reloaded from file.')
            try:
                strYesNo = input('Type \'yes\' to continue and reload from file - otherwise reload will be cancelled. ')
                strYesNo.lower() #testing to see if lower() causes an error
            except Exception as e: #if user manages to cause an error with their input
                print('You have entered an response that caused a ', type(e),' error. Returning to Main Menu.')
                continue #returns user to Main Menu
            else:
                if strYesNo.lower() == 'yes':
                    print('Reloading...')
                    lstOfCDObjects = FileIO.load_inventory(strFileName)
                    print('Inventory Loaded.')
                else:
                    print('Cancelling... Inventory data NOT reloaded.')
                IO.show_inventory(lstOfCDObjects)
            try: input('Press [ENTER] to return to Main Menu. ')
            except Exception as e: #if user manages to cause an error with their input
                print('You have entered an response that caused a ', type(e),' error. Returning to Main Menu.')
            finally: continue  # start loop back at top.
        # 3.3 process add a CD
        elif strChoice == 'a':
            # 3.3.1 Generate ID and Ask user for CD Title and Artist
            #intID = DataProcessor.calculate_cd_id(lstTbl)
            try:
                intID, strTitle, strArtist = IO.get_cd_data()
            except Exception as e: #if user manages to cause an error with their input
                print('You have entered an response that caused a ', type(e),' error. Returning to Main Menu.')
                continue
            # 3.3.2 Add item to the table
            cdObj = CD(intID, strTitle, strArtist)
            lstOfCDObjects.append(cdObj)
            IO.show_inventory(lstOfCDObjects)
            try: input('CD Added. Press [ENTER] to return to Main Menu. ')
            except Exception as e: #if user manages to cause an error with their input
                print('You have entered an response that caused a ', type(e),' error. Returning to Main Menu.')
            finally: continue  # start loop back at top.
        # 3.4 process display current inventory
        elif strChoice == 'i':
            IO.show_inventory(lstOfCDObjects)
            try: input('Press [ENTER] to return to Main Menu. ')
            except Exception as e: #if user manages to cause an error with their input
                print('You have entered an response that caused a ', type(e),' error. Returning to Main Menu.')
            finally: continue  # start loop back at top.
        # 3.5 process save inventory to file
        elif strChoice == 's':
            # 3.5.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstOfCDObjects)
            try:
                strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.5.2 Process choice
                if strYesNo == 'y':
                    # 3.5.2.1 save data
                    FileIO.save_inventory(strFileName, lstOfCDObjects)
                    input('The inventory was saved to file. Press [Enter] to return to Main Menu.')
                else:
                    input('The inventory was NOT saved to file. Press [Enter] to return to Main Menu.')
            except Exception as e: #if user manages to cause an error with their input
                print('You have entered an response that caused a ', type(e),' error. Returning to Main Menu.')
            finally: 
                continue  # start loop back at top.
        # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
        else:
            print('General Error')
except Exception as e: #if user manages to cause an error with their input
    print('You have entered an response that caused a ', type(e),' error')