message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        #message = 'local' # this creates a new binding, doesn't override the more global one

        global message
        message = 'local' # this impacts the outer binding
        print(f"setting message to {message}")
    
    print(f"enclosing message before: {message}")
    local()
    print(f"enclosing message after: {message}")



print(f"global message before: {message}")
enclosing()
print(f"global message after: {message}")
