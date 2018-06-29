import discord
import json

client = discord.Client()

try:
    config = json.loads(open('config.json').read())

    token = config['bot_token']
    server_id = config['server_id']
    role_name = config['role_name']
except:
    print("FATAL ERROR: Couldn't read config file")
    exit()


@client.event
async def on_ready():
    print("SD verification bot")
    print('Logged in as %s' %client.user.name)
    print("Client User ID: %s" %client.user.name)
    print('------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('!authorize'):
        try:
            parameter = message.content.lower().split(" ")[1]
        except:
            print("Failed to authorize user %s due to invalid paramaters" % (str(message.author)))
            await client.send_message(message.author, "Invalid parameters")
            return

        try:
            ver_lines = []
            un_lines = open('verification.txt', 'r').readlines()
            for line in un_lines:
                if '\n' in line:
                    ver_lines.append(line.split('\n')[0])
                else:
                    ver_lines.append(line)

        except:
            print("Internal server error, could not read verification file")
            await client.send_message(message.author, "Internal server error")
            return

        if parameter in ver_lines:
            server = client.get_server(server_id)
            try:
                role = discord.utils.get(server.roles, name=role_name)
            except:
                print("Internal server error, could not find role")
                await client.send_message(message.author, "Internal server error")
                return

            if role == None:
                print("Internal server error, could not find role")
                await client.send_message(message.author, "Internal server error")
                return

            author_id = message.author.id
            user = get_user(server, author_id)

            if user == 'none':
                print("Could not find user %s" % (str(message.author)))
                await client.send_message(message.author, "Failed to authorize user")
                return

            if role_name in user.roles:
                print("User %s is already authorized" % (str(message.author)))
                await client.send_message(message.author, "User is already authorized")
                return

            await client.add_roles(user, role)
            print("Successfully authorized user %s with parameter %s" % (str(message.author), parameter))
            await client.send_message(message.author, "Successfully authorized user")
            return
        else:
            print("Failed to authorize %s with parameter %s" %(str(message.author), parameter))
            await client.send_message(message.author, "Failed to authorize user")
            return

def get_user(server, id):
    for member in server.members:
        if member.id == id:
            user = member
            return user
    return 'none'

try:
    client.run(token)
except:
    print("FATAL ERROR: Failed to connect to Discord application.")
    exit()
