# UCB-Pseudosensor-Project-1

This is the first project required for Rapid Prototyping of Embedded Interface Designs (ECEA 5347) at the University of Colorado - Boulder. I have included three files:
  1. UCB-Pseudosensor-Project1.pdf: This is a project overview, including requirements, assumptions, and other notes, as well as screenshots of the application in several scenarios.
  2.  buttonTable.ui: Qt design file used for the initial layout of the user interface.
  3.  weatherApp.py: Bread and butter python code clarifying paramaters for the UI design, generating weather data, and executing logic for events. Once weather data is generated,   it is stored in MySQL, and then retrieved as one instantaneous reading, or 10 readings, taken 1 second apart. The temperature and humidity values are pseudorandom per project     requirements.

# What I learned

At the time I completed this project, I had a fair amount of time put into python coding so that made the process much more comfortable overall. On the other hand, I had not been introduced to Qt, nor PyQt5 prior to this project. My initial inclination was to code the UI from scratch, until I later learned that Qt Designer will do much of the heavy lifting for you if you have a general idea of what you want your UI to look like. 

Once your interface is designed in Qt Designer, much of the remaining work is to fine-tune visual parameters, and build the logic of the application (i.e. the fun part!). I can certainly see why Qt is a popular option for embedded design, due to relatively basic UIs as compared to front-end web development. This doesn't mean Qt isn't capable of aesthetically pleasing design, but one would be able to present a variety of designs for a client in a rather short period of time.
