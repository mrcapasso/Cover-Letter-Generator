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
