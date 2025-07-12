"""
Problem Statement:
    Design a Notification System (like in Instagram)
        Users get notifications for likes/comments
        Notifications can be seen/unseen
        They can be listed, marked as read, etc.

----------------------------------------------------------

***PRO TIP***

entities -> classes
responsibilities -> methods

Step 1: Read and extract nouns → they become your entities/classes
Step 2: For each class, ask:
    What should this class know? → these become attributes
    What should this class do? → these become methods

"""

from typing import List


class Notification:
    def __init__(self, content):
        self.content = content
        self.is_seen = False

    def mark_read(self):
        self.set_seen()

    def set_seen(self):
        self.is_seen = True

    def set_unseen(self):
        self.is_seen = False


class LikeNotification(Notification):
    type = "Like"


class CommentNotification(Notification):
    type = "Comment"


class Notifications:
    def __init__(self, notifications: List[Notification]):
        self.notifications = notifications

    def list(self):
        return self.notifications
