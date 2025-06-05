import numpy
        
def main():# This is the correct way to make code run only when the file is executed directly
    if __name__ == "__main__":
        print("Main code executed")

def npexample():
    ar1 = numpy.array([1,2,3,4,5])
    print(numpy.mean(ar1))

#this exectued only if run in greetings.py
main()