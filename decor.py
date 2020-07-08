
def hello(parameter):
    def inner():
        print("Hello")
        parameter()
    return inner

def afterHello(parameter):
    def inner():
        parameter()
        print("After hello")
    return inner

@hello
@afterHello
def szia():
    print("Szia")

szia()