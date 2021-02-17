#!/user/bin/python3

#     License Type: GNU General Public License v3.0
#     'Cover Letter Generator', generates cover letters.
#     Copyright (C) 2021 Matteo Capasso (matteo@capasso.dev)

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program in the parent folder.
#     If not, see <https://www.gnu.org/licenses/>.


################################(Misc. Functions)###############################
#License Function
#Program Purpose Function
#Clipboard Word Consolidator

#############################(Validation Functions)#############################
#Program Up to Date
#Settings.txt Integrity&Validation Function (bool) --FINISHED--
    #is there a settings file?
        #if yes:
            #is file modified?
                #if yes:
                    #Proper keys and key values (compare from hidden)?
                        #if no:
                            #Open up read only copy of settings.txt from hidden
                            #for comparison and inform the user that 
                            #styles need to match and they need to save the
                            #document
                            #return false
                        #if yes:
                            #return true
                #if no:
                    #open up file and remind them to save & close... 
                    #...it once they are done filling in the blanks
                    #return false
        #if no, copy from hidden then:
            ##open up file and remind them to save & close... 
            #...it once they are done filling in the blanks
            #return false       
#User Programs Check (Necessary?) --WIP--
    #Check for default .pdf editor
        #if none sumatraPDF
    #Check for default word processor
        #if noone
    #Is it possible to do both of these in the browser? 
    #Word Processor Check
        # ?) Function to find default word processor?
        # *) If no, gather list of most popular and reference them internally
    #PDF Reader Check
        # ?) Function to find default PDF reader? 
        # *) If no, gather list of most popular and reference them internally
#Template Integrity&Validation Function (bool) --FINISHED--
    #Are there files in Cover Letter templates?
            #If one:
                #Good file type?
                    #if good:
                        #continue
                    #if bad:
                        #Warn user of bad file type
                        #restore default from hidden
                        #Would you like to use default template? 
                            #if yes:
                                #return true
                            #if no:
                                #print please pick compatible file type
                                #and add it to Cover Letter Templates folder
                                #**open folder for them too
                                #pause program
                                #return false
                    #return True
            #If multiple: #! Fix this logic for valid and invalid file types
                #Retrive list based on valid file extensions
                #Prompt user to pick desired file
                #Would you like to make this your default? 
                    #if yes:
                        #Update settings.txt
                    #This can be changed at any time by going to Settings.txt
                    #return true 
            #else: (no files case)
                #Copy template from hidden
                #Send warning of missing document
                #Default template has been restored
                #Would you like to use default template? 
                    #if yes: 
                        #return True
                    #if no:
                        #open cover letter templates
                        #remind them file extensions
                        #pause program
                        #return false
#Backup Folder Integrity&Validation Function (bool)

########################(Document Manipulation Functions)#######################
#Word Document to PDF Converter
#CSV/Excel File Updater
#Document Name Changer
#Document Open

########################(Backup & Compression Functions)########################
#Last Backup Compression Date Checker

####################################(Main Body)#################################
#print(License Function String)
#print(Project Purpose Function String)
#pause
#Last Backup Date Retrival from Resources.json
    #compress files
    #record compression date
#Main Loop
    #Clear Terminal
    #Print Welcome Message
        #This program uses text and your clipboard (copy and paste)
    #Clipboard Check Input Loop
        #Please copy clip board
        #Type hotkeys for Windows, Linux, and Apple
        #pause
        #Retrive Clipboard
        #Paste part of clipboard to screen (use function from old project)
        #Does this look like the text? 
            #if yes
                #Subloop exit condition
    #! Analyze clipboard text
    #Make copy of template to generated folder
    #Fill generated document in generated with text and WIP name
    #Open .doc to user, make changes obvious and easy to go through w/ fields
    #User Input Validation Loop
        #Parse new document to ensure fields have been changed
            #if changed
                #break / exit condition
            #if not changed
                #notify user they missed a field
                #open document if not already open
                #pause
    #Remove WIP from document name
    #Create PDF of the document
    #Update CSV/Excel File with information
    #Copy pdf, .doc, and csv to backup folder


    

    




