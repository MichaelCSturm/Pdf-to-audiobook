import pyttsx3,PyPDF2 
pdfObj = open('chenjiahao-Real-Time-Rendering-Fourth-Edition-2018-CRC-Press.pdf','rb') 
pdfreader = PyPDF2.PdfReader(pdfObj) 
speaker = pyttsx3.init() 
audiobook = ""
numChapter = 0
for page_num in range(len(pdfreader.pages)):  
    numChapter+=1
    text = pdfreader.pages[page_num].extract_text()  ## extracting text from the PDF 
    cleaned_text = text.strip().replace('\n',' ')  ## Removes unnecessary spaces and break lines 
    
    print(numChapter)          
    #speaker.say(cleaned_text)        ## Let The Speaker Speak The Text 
    audiobook = audiobook + cleaned_text
    
    


    speaker.save_to_file(cleaned_text,"Page" +str(numChapter) +".mp3")  ## Saving Text In a audio file 'story.mp3' 
    speaker.runAndWait()

     
