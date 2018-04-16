# -*- coding: utf-8 -*-
from twitter_api import NewPost as TwitterNewPost


class NewPost:

    def perform(self):
        while True:
            try:
                text = str(input('Enter post text: '))
                TwitterNewPost(text)
            except KeyboardInterrupt:
                return('Cancel')
            else:
               return('post was published')
        

class UserPosts:

    def search_message(self, username):
        user_db = {'test': ['message 1','message 2','message 3','message 4','message 5','message 6']}
        return user_db[username]
    
    def perform(self):
        for message in self.search_message('test'):
            print(message)


class History:
    def read_db(self):
        db = {'1': 'NewPost',
              '2': 'UserPosts',
              '3': 'UserPosts',
              '4': 'NewPost',
              '5': 'NewPost',
              '6': 'UserPosts',
              '7': 'NewPost'}
        
        return db

    def perform(self):
        for read in self.read_db():
            print(self.read_db()[read])