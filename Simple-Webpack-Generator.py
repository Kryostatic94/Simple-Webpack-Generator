import os

#Sezione cartella
print("Inserisci il nome della cartella: ")
directory = input() #Immettere il nome della cartella

percorsoDiDestinazione = "?" #Inserire il percorso di salvataggio


path = os.path.join(percorsoDiDestinazione, directory) 
 
os.mkdir(path) 
print("Cartella '% s' creata" % directory) 

#Sezione HTML
percorso = percorsoDiDestinazione + "/" + directory
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
    <link rel="stylesheet" href="style.css" />
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

percorso = percorsoDiDestinazione + "/" + directory
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

percorso = percorsoDiDestinazione + "/" + directory
filename = "script.js"
file_path = os.path.join(percorso, filename)
f = open(file_path, "w")
f.close()

print("File script.js creato") 


print("Happy Coding!") 