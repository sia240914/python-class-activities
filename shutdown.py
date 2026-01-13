def shutdown(input):
    if input.lower()=="yes":
        return "shutting down your system"
    elif input.lower()=="no":
        return("abort shutdown")
    else:
        return"sorry"

shutdown_command=input(str(" do you want to shutdown your system ?"))

print(shutdown(shutdown_command))