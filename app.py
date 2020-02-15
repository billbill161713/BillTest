import util
print("#1")
util.TestUrl01("https://mydomain/todo?tempId=-1&title=lunch","tempId=-1") 
print("#2")
util.TestUrl02("https://www.google.com/search?client=firefox-b-1-d&q=curricular")
print("#3")
util.TestUrl03("<html>\n<head>\n<title>Hellow World</title>\n</head>\n<body>\n  Hi {invitee}, <br><br>\n  Please come to {event} at {time}.<br><br>\n  From {name}\n</body>\n</html>")
