import Constants

class Callbacks():
    '''Model for Callback results'''
    def __init__ (self, update_id, timestamp, id, chat_id, user_id, username, callback_data):
        '''initialises an instance with the different properties'''
        self.update_id = update_id
        self.timestamp = timestamp
        self.id = id
        self.chat_id = chat_id
        self.user_id = user_id
        self.username = username
        self.callback_data = callback_data
        if str(self.callback_data)[0] == Constants.ADD_EXPENSE:
            self.command_type = Constants.ADD_EXPENSE
        else:
            self.command_type = Constants.UNRECOGNISED_COMMAND
        self.type = Constants.BUTTON

    def display(self):
        '''returns information about the instance of the class'''
        return "update_id: " + str(self.update_id) + "\ttime: " + str(self.timestamp) + "\tid: " + str(self.id) + "\tchat_id: " + str(self.chat_id)+ "\tuser_id: " + str(self.user_id) + "\tusername: " + str(self.username) + "\tcommand_type: " + str(self.command_type) + "\tcallback_data: " + str(self.callback_data)