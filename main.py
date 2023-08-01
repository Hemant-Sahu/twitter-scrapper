import csv
import matplotlib.pyplot as plt
 
filename = "twitter.csv"
 
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
# date, id, content, username, like_count, retweet_count
#   0     1       2       3           4           5   

# Work:
# Build analytics like which tweets got most reshares,
# which tweets are most commented,
# what are the top 5 clusters of discussions of tweets,
# top 3 users of each month, etc.

tweetReshareCount = {}
tweetCommentCount = {}
tweetLikeCount = {}
userActivityCount = {}
for row in rows[:]:
    # parsing each column of a row
    if len(row) != 6:
        continue
    tweetReshareCount[row[1]] = row[5]
    tweetLikeCount[row[1]] = row[4]
    if row[3] in userActivityCount:
        userActivityCount[row[3]] += 1
    else:
        userActivityCount[row[3]] = 1
    
orderedTweetReshareCount = sorted(tweetReshareCount.items(), key=lambda item: item[1], reverse=True)
ororderedTweetLikeCount = sorted(tweetLikeCount.items(), key=lambda item: item[1], reverse=True)
ororderedUserActivityCount = sorted(userActivityCount.items(), key=lambda item: item[1], reverse=True)

    
    

# Extract values and frequencies from the data list
values, frequencies = zip(*orderedTweetReshareCount[:10])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('Tweet')
plt.ylabel('Number of likes')
plt.title('Like count')

# Show the plot
plt.show()
    
    
    
# Extract values and frequencies from the data list
values, frequencies = zip(*ororderedTweetLikeCount[:10])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('Tweet')
plt.ylabel('Number of reshares')
plt.title('Reweet count')

# Show the plot
plt.show()


    
# Extract values and frequencies from the data list
values, frequencies = zip(*ororderedUserActivityCount[:3])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('User')
plt.ylabel('Number of tweets')
plt.title('User activity count')

# Show the plot
plt.show()




