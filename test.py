from slacker import Slacker

slack = Slacker('xoxp-1590896034022-1597673179266-3977416434902-fdd26c7b22b7e619e230f00ba3caf46c')

# Send a message to #general channel
slack.chat.post_message('#general', 'Hello fellow slackers!')
