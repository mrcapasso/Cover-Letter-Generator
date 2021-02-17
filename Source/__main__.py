#!/user/bin/python3

#     License Type: GNU General Public License v3.0
#     'Cover Letter Generator', generates cover letters for use in job applications.
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