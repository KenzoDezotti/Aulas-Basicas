import webbrowser

url='https://www.youtube.com/watch?v=tqF0MjcOqcI'
download=url[:12]+"ss"+url[12:]
webbrowser.open(download)
