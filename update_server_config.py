# Update server config files

def update_server_config_file(path,key,value):
    #open file and read the lines to a variable
    with open(path,"r") as file:
        lines=file.readlines()
        print(type(lines))
        with open(path,"w") as file:
            for line in lines:
                if key in line:
                    
                    file.write(key+"="+value+"\n")
                else:
                    
                    file.write(line) 

update_server_config_file('server.config','MAX_CONNECTIONS','1000')