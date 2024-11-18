"# Solving-problems-using-the-Huffman-tree"

"Version 1:

A program that calculates the compression ratio. Compresses the string itself by creating a tree using the Huffman algorithm. Tasks from the computer science course 11th grade"

To launch the first version, download/open the file "huffmanSolutionVersion1"

"Version 2:

>1.1

1. Everything that includes version 1
2. The program now also draws the tree itself to you in the terminal"

>1.2

To work with the second version, follow these conditions:
1) Download a file huffman.zip
2) Unzip the archive into a folder (only Latin letters and numbers in the name)
3) Right-click on the "huffman" folder and open it via vs code
4) Open the file with the second version "index.py"
5) Open the "cmd" terminal

>1.3

Enter the following commands into the terminal(WITHOUT THE ">" SIGN):

1) > .\myenv\Scripts\activate 
2) > pip install -r requirements.txt

>1.4

What should I do if I don't have vs code?

You can run this code in cmd. How to do it? Here are the instructions:

1) Open the cmd itself. Via Win + R -> cmd
2) Navigate to the folder where all files are stored using cmd commands:
    a. To switch between disks, write in cmd: "name disks" + :
        Example:
        >d:
        >c:
    b. To navigate to a folder, use the command:
        cd "name folder"
            Example:
            >cd huffman
3) Enter the commands from point 1.4

>1.5

If you have an error:

"pip is not an internal or external command executable program or batch file"

Then you need to go:

Control Panel -> System -> Advanced System Settings -> Environment Variables 

You will see 2 windows, User environment Variables for <username> and System variables. 
You need the first one, click on the Path -> Change variable, then you will see the Variable Value field, 
put a separator at the end; and add the path to the directory where pip is located (for example, C:\Python\Scripts the path to the Python directory may differ).

The usual way is like this:

C:\Users\<username>\AppData\Local\Programs\Python\Python311\Scripts

"#002Corp"

"P.S:
If anything, I left the first version"
