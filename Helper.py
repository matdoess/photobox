import random
import threading

class Helper():

    def getTasks(self):
        file = open("./config/tasks.txt");
        lines = file.readlines();
        tasks = {}
    
        for line in lines :
            line = line.replace("\n", "");
            shortTask = line.split(":")[0]
            longTask = line.split(":")[1]
            tasks[shortTask] = longTask
        
        return tasks

    def getRandomTask(self):
        tasks = self.getTasks();
        randomTaskKey = random.choice(list(tasks.keys()))
        randomTask = {"short": randomTaskKey, "long": tasks[randomTaskKey]}
        return randomTask


    def getMailText(self):
        file = open("./config/mailtext.txt");
        mailtext = file.read()
        return mailtext

    def getMailAddresses(self):
        print("getMailAddresses")

        try:
            filepath = "./config/mailaddresses.txt"
            file = open(filepath);
            addresses = file.read().splitlines();
            return addresses
        except IOError as err:
            print("Error reading the file {0}: {1}".format(filepath, err))
            return None

    def findMailAddressByMail(self, mail):
        print("findMailAddressByMail")

        addresses = self.getMailAddresses()

        for address in addresses:
            if address == mail:
                return address

        return None


    def addMailAddress(self, mail):
        print("addMailAddress")

        address = self.findMailAddressByMail(mail)

        if address == None:
            filepath = "./config/mailaddresses.txt"
            file = open(filepath, "a");
            file.write("\n")
            file.write(mail)
            file.close()

    def isThreadAlive(self, threadname):
        
        for thread in threading.enumerate():
            print(thread.name)
            if thread.name == threadname:
                return thread.is_alive()
            else:
                return False


if __name__ == "__main__":
    helper = Helper()
    print(helper.getRandomTask())
# helper = Helper()
# helper.getMailAddresses()
# foundAddress = helper.findMailAddressByMail("elisabethkeller1@web.des")
# helper.addMailAddress("test@web.de")

# print(foundAddress)

