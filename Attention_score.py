def attention_score(iris, blinks):
    total_blinks = 0
    for b in blinks:
        total_blinks = b + total_blinks
    average_blinks = total_blinks / len(blinks)

    print("Average Blinks : " + str(average_blinks))
    print("total: " + str(total_blinks))
    print("Iris Info : " + iris)

    '''
    Algorithm Goes Here
    '''