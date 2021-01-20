#command_line_test.py
import cmd

class NetworkShell (cmd.Cmd):
    intro = "Command Line: Type ? to list all commands"
    
    prompt = " / "
    
    file = None


net = NetworkShell()

if __name__ == '__main__':
    net.cmdloop()