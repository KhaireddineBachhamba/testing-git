import fire
#i hope this works
#it worked !!! trying this again 
def hello(name = "World"):
    return "Hello %s!" % name


if __name__ == '__main__':

    fire.Fire(hello)