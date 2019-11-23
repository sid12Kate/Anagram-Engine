"# Assignment_01_Anagram" 

1.	Project Description

This project is built using Python 2.7 and Google App Engine. As the name suggests , an anagram engine is designed. Every user has the ability , to create his own lists, add anagrams of these words as well sub anagram of the same . User lists are kept separate. A search option is provided to the user so as to find out anagrams of the word that he enters ( only if it exists in the user’s list).
      
2.	Methods and Databases 

•	User Login/Logout
        The first page of the application is the login page. When the user clicks login, the    user is asked to enter his email id and then login. If it is an existing user, the user can see his list and search for anagrams as well add new ones. If a new user logs in , he can create a new list of his own and add words to the same.
	     
•	Main Page
After the user logs in, he is directed to the main page. On this page he is provided with several options such as add words to his list, search for anagrams in his list as well as search for sub anagrams. The main method of the page is explained as follows:
The get method :

1.	Every user is associated with an unique key which is a set of numbers. When a new user logs in, a new key is created and then associated with the user. If an existing user logs in , the database is searched for the existing key and all the actions that this user performs are stored in the sections associated with the key. The get_current_user() method is also used, which is predefined method in Google App Engine Python.
2.	A ‘Search’ option is also provided to the user on the main page. In this when a user enters a particular word that he had previously stored in the database, and searches for anagrams, a list of all anagrams that exist in his list are displayed to him. For fetching the right output, every word and its anagram is stored in the database with an unique key .
3.	An ‘Add Words’ option is provided, which directs the user to new page for adding words to his list.


•	Add Words

This page allows user to add words to his lists by two methods namely:
1.	By entering words one by one manually
2.	By uploading a text file consisting a list of words.

The post method : 
This method is triggered when the user clicks one of the two buttons that is Add or Upload. 
Add :
1.	An input box is provided to the user , where the user can enters words. The input is restricted to alphabets (lowercase/uppercase) only. If the user enters anything else other than the above format, an error is shown and he is asked to enter the text as specified.
2.	After entering the word and clicking add, the word is first sorted in lexographic/alphabetical order. Then a new key is created, which consists of user’s unique key + order. Then the entire database is searched for the key using key.get(). If the key exists, then the word that the user entered is added to the list of strings associated with that particular key as it as an anagram . If the key does not exists , then a new one is created with the same process as specified above and a new list is created to which the word entered by the user is stored.
3.	A particular user can enter many different words that are not anagrams of each other, in such a scenario , the key that will be generated will have the same unique key just the attached order of the words will be different so as to keep words separate.

Upload :
1.	If the user wants to upload a text file , he is provided an option to choose a text file from the computer that he is accessing the application through.
2.	When the user clicks upload, the file is read using read() function.
3.	A for loop is created that iterates through the file and takes one word at a time, till the end of the file.
4.	The procedure that is explained above, is then applied to every word and the words and if anagrams are stored in the database.
   

3.  Data structures 

                   Two data structures are used and they are explained as follows :
•	MyUser():
The datastructre is created using an NDB model of the Google App Engine. Every property of the database is modelled as an ndb property. In this datastructre the following information is stored : 
1.	User Email : The one is which user enters while logging in.
2.	Key name : An id that is automatically created and which is used for future reference of the user. It is unique for every user.
3.	Anagram Count : The count of total unique anagrams in user’s list.
4.	Word Count : The count of total words in the user’s list.

This information is kept separate for every user.



•	WordList()

The datastructre is created using an NDB model of the Google App Engine. Every property of the database is modelled as an ndb property. Every different word which is not an anagram has a unique separate entry. in the In this datastructre the following information is stored : 
1.	Key : This key is the combination of user’s unique id and the lexographical order of the word .
2.	List : This is a string property , which is a list of words that are anagrams of each other . They are stored under the same key.
3.	Wordcount : It is the count of the words in that particular list.
4.	Letter count : It is the count of the letters in the word associated with that list.


4. User Interface Design
A simple and a basic user interface is designed .  A faint blue background colour is used. The navigation bar consists of following options :
1.	AddWords
2.	Logout
The navigation bar , is in dark black colour so as to highlight the main options available to the user.
Below the navigation bar a search option is provided and based on the same, a list of anagrams currently in the system is displayed. The list is displayed exactly in the  centre  of the page, one below the other with the required spacing so as to give a good view to the webpage overall.
The rest of the webpages follow a simple design which is easier to fill out by the user and color combination is simple black and white . Every other page has a ‘Back/Cancel’ button which redirects the user to the main page of the website. 

  

 


