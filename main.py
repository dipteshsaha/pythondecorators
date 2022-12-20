def log_message(diptesh): 
    def simple(*args,**saha):
        output = diptesh(*args,**saha)
        with open('decorator_logs.txt', 'a') as f: 
            f.write(output+"\n")
        return output
    return simple
@log_message
def a_function_that_returns_a_string():
    return "A string"
@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)
@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"
a_function_that_returns_a_string() 
a_function_that_returns_a_string_with_newline("Shinhan Nohara")
a_function_that_returns_another_string()