# ssh-bot

_ssh-bot_ is a botnet command and control that uses SSH to communicate.

## FAQ

### What's a botnet?

A botnet is a distributed system made of hijacked computers. The bots 
(infected machines) maintain a connection with the botnet administrator, who
can fire commands to the bots, like "Do a DDoS attack at `<host>`", "Mine 
<cripto-coin>", "Spy the victim", etc.

There is a few botnet architectures, and this one is a "Client-server" model.

### So, this is a dangerous malware?

Not exactly. This code doesn't contains any sort of spread function or 
auto-attack, so it won't take control of your network or steal your credentials
by default. To case any harm, the user need to explicitly command or modify
the code to do so.

### Is this illegal?

Write code that connects to machines which you do have authorization to 
connect isn't illegal. But, connecting to machines where you do not have such
permission, probably is.

This software was created for study reasons and I do not take responsibility
for any crazy action you take with this. Have fun!

### Is this technically practical?

To turn on a SSH server or create new users, one needs to have admin rights on
that machine. So, you already need to exploit some kind of vulnerability in
order to connect a new machine, and will probably involve privilege escalation.

If the machine already have a SSH server running, you may have luck that the 
system has an old and vulnerable SSH version. Otherwise, you will need to
enter by others breach, use social engineering or
 [brute force](https://charlesreid1.com/wiki/Metasploitable/SSH/Exploits) the
password.

SSH is secure and encrypted, so it will prevent some analysis on your packet 
content. Although, SSH connections could draw a lot of attention if the
victim's servers isn't used to have it.


