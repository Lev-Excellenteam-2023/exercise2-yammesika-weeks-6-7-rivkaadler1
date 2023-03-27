class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """
    UN_READ = 0
    READ = 1

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [[], []] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_title (str): The title of the message.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'][self.UN_READ]+po_box.boxes['b'][self.READ])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box[self.UN_READ].insert(0, message_details)
        else:
            user_box[self.UN_READ].append(message_details)
        return self.message_id

    def read_inbox(self, user_name, N=None):
        """Read the N first unread messages in the user's inbox.

        Args:
            user_name (str): The username of the user whose inbox we want to read.
            N (int, optional): The maximum number of messages to return. Defaults to None (return all unread messages).

        Returns:
            list: A list of dictionaries representing the N first messages to be read  in the user's inbox.
       """
        unread_messages = self.boxes[user_name][self.UN_READ]
        messages = []
        if N is None or N > len(unread_messages):
            N = len(unread_messages)
        for i in range(N):
            messages.append[unread_messages[i]]
        self.boxes[user_name][self.READ] += unread_messages[:N]
        del unread_messages[:N]
        return messages

    def search_inbox(self, user_name, searched_str):
        """Searches for messages containing a specific string  in a specific user's  inbox.

        Args:
            user_name (str): The username of the user whose in his inbox we want to search.
            searched_str(str): The string we want to search for.

        Returns:
            list: A  list of all the messages in the user's inbox that contain the searched_str, in their title
             or in their body .

       """
        user_box = self.boxes[user_name][self.UN_READ] + self.boxes[user_name][self.READ]
        messages = []
        for message in user_box:
            if searched_str in message["title"] or searched_str in message["body"]:
                messages.append(message)
        return messages
