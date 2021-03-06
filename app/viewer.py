# -*- coding: utf-8 -*-
from commands import CommandHistory, CommandUserPosts, CommandNewPost

class MainView:
    function = input
    commands = ['New post', 'User posts', 'History']
    message = '{br}Input your command: {commands} {br}' \
                .format(commands=' | '.join(commands), br='\n')

    def get_routes(self):

        return {
            'New post': CommandNewPost,
            'User posts': UserPostsView,
            'History': HistoryView
        }

    def perform_command(self, command):
        routes = self.get_routes()

        command_class = routes[command]
        command_inst = command_class()

        command_inst.perform()

    def select_choice(self):
        while True:
            try:
                choice = self.function(self.message)
                if choice not in self.commands:
                    raise Exception('Enter correct command!')
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                print('exit')
                break
            else:
                self.perform_command(choice)

class UserPostsView:

    last_id = None

    function = input
    commands = ['Home', 'Get more']
    message = '{br}Input your command: {commands} {br}' \
                .format(commands=' | '.join(commands), br='\n')

    def __init__(self):
        self.user = CommandUserPosts()

    def perform(self):
        posts_stack = self.get_stack_posts()
        self.print_posts(posts_stack)
        self.select_choice()

    def get_stack_posts(self):
        if self.last_id:
            return self.user.perform(self.last_id)
        else:
            return self.user.perform()

    def print_posts(self, data_list):
        for post in data_list:
            print('{decor} {post_id} {decor}'.format(decor='=============================', post_id=post['id']))
            print('{}\n{}'.format(post['date'], post['text']))

        self.last_id = data_list[-1]['message_id']

    def select_choice(self):
        while True:
            try:
                choice = self.function(self.message)
                if choice not in self.commands:
                    raise Exception('Enter correct command!')
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                print('Cancel')
                break
            else:
                if choice == 'Get more':
                    self.perform()

                break


class HistoryView:
    function = input
    commands = ['Home', 'Cleaner']
    message = '{br}Input your command: {commands} {br}' \
                .format(commands=' | '.join(commands), br='\n')

    def perform(self):
        data = CommandHistory()
        data_list = data.perform()
        self.print_records(data_list)

        command = self.select_choice()
        if command == 'Cleaner':
            data.cleaner()


    def print_records(self, records):
        for record in records:
            print('{decor} {date} {decor}'.format(decor='=============', date=record[2]))
            print(record[1])

    def select_choice(self):
        while True:
            try:
                choice = self.function(self.message)
                if choice not in self.commands:
                    raise Exception('Enter correct command!')
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                print('Cancel')
                break
            else:
                if choice == 'Home':
                    break
                else:
                    return choice


if __name__=='__main__':
    one = UserPostsView()
    print(one.select_choice())