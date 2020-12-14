 DONE Print a welcome message to the user, explaining the Madlib process and command line interactions

 TODO Read a template Madlib file (Example), and parse that file into usable parts.

 TODO Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.

 TODO With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.

 TODO After the resulting Madlib has been completed, provide the completed response back to the user in the command line.

 TODO Write the completed text (Example)to a new file on your file system (in the repo).

---

 TODO Create and test a read_template function that takes in a path to text file and returns a stripped string of the file’s contents.

 TODO read_template should raise a FileNotFoundError if path is invalid.

---

 TODO Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.

 # def parse_template():

---

 TODO Create and test a merge function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.


#def merge():