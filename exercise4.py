def echo_message(message,times):
#    message = input("Please enter a message to print: ")
    message = message + "\n"
    print(message*times)

userinput = input("Please enter a message to print: ")
count = input("Please tell how many times to print: ")
if count:
    count = int(count)
else:
    count = 1
echo_message(userinput,count)
