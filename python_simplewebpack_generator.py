import os

#Sezione cartella
directory = "Test" #Immettere il nome della cartella

percorsoDiDestinazione = "?" #Inserire il percorso di salvataggio al posto di ?


path = os.path.join(percorsoDiDestinazione, directory) 
 
os.mkdir(path) 
print("Cartella '% s' creata" % directory) 

#Sezione HTML
percorso = "?" + directory   #Inserire il percorso di salvataggio al posto di ?
filename = "index.html"
file_path = os.path.join(percorso, filename)
f = open(file_path, "w")
codice = """
<!DOCTYPE html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title></title>
    <link rel="stylesheet" href="main.css" />
  </head>

  <body>
    <script src="script.js"></script>
  </body>
</html>
"""
f.write(codice)
f.close()
print("File index.html creato") 

#Sezione CSS

percorso = "?" + directory          #Inserire il percorso di salvataggio al posto di ?
filename = "style.css"
file_path = os.path.join(percorso, filename)
f = open(file_path, "w")
codice = """
*{
    box-sizing: border-box;
}
body{
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height:100vh;
    overflow:hidden;
    margin:0;


}

"""
f.write(codice)
f.close()
print("File style.css creato")

#Sezione JavaScript

percorso = "?" + directory              #Inserire il percorso di salvataggio al posto di ?
filename = "script.js"
file_path = os.path.join(percorso, filename)
f = open(file_path, "w")
f.close()

print("File script.js creato") 


print("Happy Coding!") 