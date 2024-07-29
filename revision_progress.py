def print_header():  
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~                                        ~")
    print("~    Engineering Interview Revision      ~")
    print("~            Progress Tracker            ~")
    print("~                                        ~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

def input_topics():
    
    topics = []
    print("Enter the topics you need to study for an interview, separated by a comma: ")
    topics = input().split(", ")
    return topics

def calculate_score(topics):

    revisionScore = 0

    for topic in topics:
        revised = input("Did you complete your revision about " + topic + "? (Yes or No)")
        if revised == "Yes":
            revisionScore += 1
        else:
            continue

    percentage = (revisionScore / len(topics)) * 100
    return percentage

def main():

    print_header()
    topics = input_topics()
    percentage = calculate_score(topics)
    print("Your revision score: " + percentage + "%")

if __name__ == '__main__':
    main()