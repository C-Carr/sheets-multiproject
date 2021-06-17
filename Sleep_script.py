#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BEDTIME
"""
Run this when you go to sleep to record time into google sheet
"""

import pygsheets
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

"""
Connect to the google sheet and open it
"""
scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sleep schedule-7dd92de5dbe9.json', scope)
client = pygsheets.authorize(service_account_file='Sleep schedule-7dd92de5dbe9.json')
sheet = client.open("sleep schedule")
wk1 = sheet.sheet1

class starting_times():
    """
    Current Year-Month-Day, Hour:Minute and timestamp
    """
    s1 = (f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")
    s2 = ("%s:%s" % (datetime.now().hour, datetime.now().minute))

class update_sheet_night():
    """
    creates new row and fills cells 1 and 2
    """
    wk1.insert_rows(row = 1, 
                    number = 1, 
                    values =[starting_times.s1, starting_times.s2, starting_times.timestamp])    


# In[5]:


#WAKE UP TIME
"""
Run this in the morning to record wake up time into google sheet
"""

import pygsheets
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

"""
Connect to the google sheet and open it
"""
scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sleep schedule-7dd92de5dbe9.json', scope)
client = pygsheets.authorize(service_account_file='Sleep schedule-7dd92de5dbe9.json')
sheet = client.open("sleep schedule")
wk1 = sheet.sheet1

class starting_times():
    """
    Retrieves value for bedtime, current Hour:Minute and difference between the two
    """
    s2 = wk1.get_value('B2')
    s3 = ("%s:%s" % (datetime.now().hour, datetime.now().minute))
    FMT = '%H:%M'
    time = datetime.strptime(s3, FMT) - datetime.strptime(s2, FMT)
    s4 = str(time)

class update_sheet_morning():
    """
    Fills cells 3 and 4
    """
    wk1.update_values('C2', [[starting_times.s3, starting_times.s4]])  


# In[3]:


#when the program runs for the first time append
#datetime day column 1
#datetime current time column 2
#when the program runs for the second time append
#datetime current time column 3
#datetime difference column 4


# In[1]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




