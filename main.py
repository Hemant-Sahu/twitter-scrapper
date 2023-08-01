import csv
import matplotlib.pyplot as plt
from datetime import datetime
import re

filename = "twitter.csv"
 
fields = []
rows = []

def extract_strings_after_hashtags(input_string):
    hashtags = re.findall(r'#\w+', input_string)
    strings_after_hashtags = [tag[1:] for tag in hashtags]
    return strings_after_hashtags

def extract_month_from_string(date_string):
    try:
        # Parse the string into a datetime object
        dt_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S%z")
        
        # Extract the month from the datetime object
        month = dt_object.month
        
        return month
    except ValueError:
        # Handle the case when the date_string is not in the correct format
        return None

 
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
userActivityCount = [{}, {}, {}]
clusterCount = {}
for row in rows[:]:
    # parsing each column of a row
    if len(row) != 6:
        continue
    tweetReshareCount[row[1]] = row[5]
    tweetLikeCount[row[1]] = row[4]
    clusters = extract_strings_after_hashtags(row[2])
    for k in clusters:
        clusterCount[k] = clusterCount.get(k, 0) + 1
    month = int(extract_month_from_string(row[0])) - 1
    userActivityCount[month][row[3]] = userActivityCount[month].get(row[3], 0) + 1
    
    
orderedTweetReshareCount = sorted(tweetReshareCount.items(), key=lambda item: item[1], reverse=True)
ororderedTweetLikeCount = sorted(tweetLikeCount.items(), key=lambda item: item[1], reverse=True)
ororderedUserActivityCount = [{}, {}, {}]
ororderedUserActivityCount[0] = sorted(userActivityCount[0].items(), key=lambda item: item[1], reverse=True)
ororderedUserActivityCount[1] = sorted(userActivityCount[1].items(), key=lambda item: item[1], reverse=True)
ororderedUserActivityCount[2] = sorted(userActivityCount[2].items(), key=lambda item: item[1], reverse=True)
orderedClusterCount = sorted(clusterCount.items(), key=lambda item: item[1], reverse=True)

    
    

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
values, frequencies = zip(*orderedClusterCount[:10])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('Cluster')
plt.ylabel('Number of tags')
plt.title('Cluster tag count')

# Show the plot
plt.show()

    
# Extract values and frequencies from the data list
values, frequencies = zip(*ororderedUserActivityCount[0][:3])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('User')
plt.ylabel('Number of tweets')
plt.title('Jan user activity count')

# Show the plot
plt.show()


# Extract values and frequencies from the data list
values, frequencies = zip(*ororderedUserActivityCount[1][:3])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('User')
plt.ylabel('Number of tweets')
plt.title('Feb user activity count')

# Show the plot
plt.show()


# Extract values and frequencies from the data list
values, frequencies = zip(*ororderedUserActivityCount[2][:3])

# Create a bar chart
plt.bar(values, frequencies)

# Add labels and title
plt.xlabel('User')
plt.ylabel('Number of tweets')
plt.title('March user activity count')

# Show the plot
plt.show()
