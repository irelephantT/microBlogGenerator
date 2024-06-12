This is a simple microblog generator written in python.
It depends on tk, beautifulSoup and markdown2

to install these run
``` shell
pip install bs4 markdown2
```
To use it make a template file. Make a div that wraps all of the code you want the posts to be wrapped in with an id of "template". Add a comment saying "<!--contenthere-->" where you want the content to be.
Here is a simple example template:
``` html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="en">
        <style>
            #box {
                border: 3px solid black;
            }
        </style>
    </head>
    <body>
        <h1>Test</h1>
            <div id="template">
                <div id="box">
            
                <!--contenthere-->

                </div>
            </div>
    </body>
</html>
```
To run the generator download the file and run:
``` shell
python3 mbgenTemplate.py
```
You can write the posts in markdown.
