import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')
    createIfNotExist('Programming')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".mp4", ".mp3", ".flv",".wav"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    
    codeExts = [".py", ".java", ".h",".html",".bat",".md"]
    Code = [file for file in files if os.path.splitext(file)[1].lower() in codeExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file) and (ext not in codeExts):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Programming",Code)
    move("Others", others)
    

