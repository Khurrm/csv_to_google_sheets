# csv_to_google_sheets
 A task to read data from csv file (located on a local server) and then write it to a defined Google sheets
 
## Step 1: Create a Project on Google Console
i) Go to  => [Google Console Link](https://console.developers.google.com) 
ii) Create a project as shown in snapshot below

![automated like clockwork](https://user-images.githubusercontent.com/107587130/189553687-24fbfa44-1d7b-4150-a579-2c8b7ec13132.JPG)

## Step 2: Enable Goolge Sheets API
i) Go to _Enabled API and services_ as shown in the figure below

![automated like clockwork](https://user-images.githubusercontent.com/107587130/189553647-4d12099e-222b-4f9c-a1ab-0ad69bd7917a.JPG)

ii) Click on Enable API and Services as shown in figure below 

![automated like clockwork](https://user-images.githubusercontent.com/107587130/189553706-2a621f59-6d2d-435a-b908-270dc37c7ec8.JPG)

iii) Click on Enable as shown in the figure below
![automated like clockwork](https://user-images.githubusercontent.com/107587130/189553730-ba05cf19-55db-41a2-a567-f1588ebb1e59.JPG)

## Step 3: Create a Service Account 
i) Go to APIs and Services and click on create credentials (as shown in figure below)
![Gitu1](https://user-images.githubusercontent.com/107587130/190009791-4fc75664-04a2-4385-98e2-5856ebd22ada.JPG)
ii) Click on Service Accounts (as shown in the figure below). 
![Gitu2](https://user-images.githubusercontent.com/107587130/190009802-6e003c93-b393-4f90-af5e-6d306b7d6a6e.JPG)
iii) Make sure to select _Project_ and then afterwards _Owner_ (as shwon in the figure below)
![Gitu3](https://user-images.githubusercontent.com/107587130/190009810-b930b6a2-de5b-4ea5-b741-2fb47f77f8f9.JPG)

## Step 4: Create a project in Python Environment
i) Create a project in Python environment. For that purpose I have already created a virtaul environment. And Python 3.X version is installed. 

