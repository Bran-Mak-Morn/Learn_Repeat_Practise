import os
from app import main

# set paths for tkinter because Python 3.13 doesn't have tcl/tk paths
os.environ['TCL_LIBRARY'] = r'C:\Users\georg\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\georg\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

if __name__ == "__main__":
    file_path = 'words_to_review.csv'  # Your file path here
    main(file_path)
