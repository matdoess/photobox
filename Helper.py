class Helper():

    def getTasks(self):
        file = open("./config/tasks.txt");
        lines = file.readlines();
        tasks = {}
    
        for line in lines :
            # line = lines[line]
            line = line.replace("\n", "");
            # print(line.split(":"))
            shortTask = line.split(":")[0]
            longTask = line.split(":")[1]
            tasks[shortTask] = longTask
        
        return tasks

    def getMailText(self):
        file = open("./config/mailtext.txt");
        mailtext = file.read()
        return mailtext

    def getMailAddresses(self):
        print("getMailAddresses")



# helper = Helper()

