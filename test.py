from slacker import Slacker

slack = Slacker('')

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackers!')
