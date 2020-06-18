# encodin=utf-8
import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {
    "server":"127.0.0.1",
    "tests":12,
    "url":"https://www.baidu.com/#/admin sss"
}
config["bit.com"] = {}
config["bit.com"]["test"] = "aaaaaaa"
config["hk.com"] = {}
test = config["hk.com"]
test["port"] = "3389"
test["if"] = "yes"

with open("example.ini",'w') as configfile:
    config.write(configfile)

with open("example.ini","r") as f:
    print(f.read())