###### importing libraries #####

import os
import math
import re


#### Defining the class BookReader which returns an index which is written to a file ####

class BookReader:

    ### constructor takes in list of file names and list of excluded words ###

    def __init__(self,file_list,exclude_words):

        self.file_list=file_list
        self.exclude_words=exclude_words

    #### reader method is used to read a page and return a set of  unique words in the file ####
      
    def reader(self,file_name):
        
        # opens a file

        file=open(file_name,"r",encoding="mbcs")

        # reterieve sentences from the file

        sentences=file.readlines()

        # obtain set of words from each sentence

        word_list=[]

        for sent in sentences:   
            
            word_list.extend(re.split('\s',sent.lower()))

        #close the file

        file.close()

        #returns the unique set

        return set(word_list)-set(self.exclude_words)


    ### read_pages is used to read the entire set of files and create the index ###    

    def read_pages(self):

        # initializes index and word_set to be used

        index={}
        word_set=set()

        # creates a word set

        for file_name in self.file_list:

            words=self.reader(file_name)
            word_set=word_set.union(words)

        # exclude the excluded set from word set

        word_set=word_set-set(self.exclude_words)

        """
        checking for each word,if the word is not an excluded word and is not already present in the index
        an entry is created
        
        """ 

        for word in word_set:

            if word not in index:

                index[word]=[]

            if word in self.exclude_words:

                continue

            # initializes a counter

            count=1

            # checking whether the word is present in each of the file

            for file_name in self.file_list:

                words=self.reader(file_name)

                if word in words:
                    index[word].append(count)

                count+=1
        
        # sorting the index

        index_keys=sorted(list(index.keys()))

        index={i:index[i] for i in index_keys}

        # returns the index

        return index

    ### writer method is used to write the results to a file ###

    def writer(self):

        # opens a file to write contents to

        write_file=open("index2.txt","w",encoding="mbcs")

        # invokes read_pages method to obtain the index

        words=self.read_pages()   
        

        # writes the result to the file

        for key,value in words.items():

            write_file.write("%s:%s\n"%(key,value))

        
        # closes the write file

        write_file.close()


    

######## Driver code #######

file_list=['Page1.txt','Page2.txt','Page3.txt']     # List of file names

fp=open('exclude-words.txt',"r")      # opens exclude_words file

# get exclude_words

exclude_words=fp.readlines()

# creates a BookReader object and invokes the writer method

obj=BookReader(file_list,exclude_words)
obj.writer()

# closes the file

fp.close()





    





            



