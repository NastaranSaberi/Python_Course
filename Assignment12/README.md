# Assignment 12 - Mini Project 1 :

In this project, we designed a robust Video Media Management Software to efficiently handle and manage a diverse collection of media types, including Films, Series, Documentaries, and Clips. The core of the application is built around the **MediaManager** class, which provides functionality for adding, removing, editing, and displaying media items. Each media item is modeled by extending a base **Media** class, which encompasses fundamental properties such as name, director, IMDB score, URL, duration, and a list of actors represented by the **Actor** class. Specialized media types like **Film**, **Series**, **Documentary**, and **Clip** inherit from this base class and include additional unique properties relevant to each media type.
 The **Database** class handles the persistence of media data by reading from and writing to a text file, ensuring that the media collection is maintained across sessions.


To enhance user interaction and functionality, the project uses several Python libraries. The termcolor library is utilized for color-coded terminal output, which helps in distinguishing different messages and statuses. The **pyfiglet** library is used to generate stylish ASCII art for a more engaging user interface. For downloading media, the **pytube** library facilitates the retrieval of video content from URLs, ensuring that users can directly access media files through the application. The **Database** class handles the persistence of media data by reading from and writing to a text file, ensuring that the media collection is maintained across sessions.

**Run the Application:** Execute the **main.py** file to start the program.
