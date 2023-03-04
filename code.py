# PrivacyGuard
# BSD 2-Clause License
# 
# Copyright (c) 2023, GeorgeSEC1 - George Wagenknecht
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import random
import re
token = "."
def convert(lst):
    return (lst.split())
def statFind(sentenceA,sentenceB,arr,threshold):
      var = 0
      for word in arr:
         try:
            if sentenceA.count(" " + word + " ") > threshold and sentenceB.count(" " + word + " ") > threshold:
               var += sentenceA.count(" " + word + " ") +  sentenceB.count(" " + word + " ")
         except:
               False
      return var
def gather(file,user):    
    output = ""   
    return output
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.readlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
filename = "privacy#" + str(random.randint(0,10000000)) + ".txt"
random.shuffle(questions)
with open("nouns.txt", encoding='ISO-8859-1') as f:
     nouns = f.read()
random.shuffle(files)  
for file in files:
                with open(file.strip(), encoding='ISO-8859-1') as f:
                    textA = f.read()
                if len(textA) > 0:
                      for  fileX in files:
                            with open(file.strip(), encoding='ISO-8859-1') as f:
                                textB = f.read()
                            sentencesA= textA.split(token)
                            sentencesB= textB.split(token)
                            for threshold in range(100):
                                 sentenceA = sentencesA[ random.randint(0,len(sentencesA)-1)]
                                 sentenceB = sentencesA[ random.randint(0,len(sentencesB)-1)]
                                 if statFind(sentenceA,sentenceB,nouns,threshold) < threshold:
                                          print("score:" , threshold)
                                          print("[" + sentenceA + token + "]")
                                          print("[" + sentenceB + token + "]")
                                          print()
                                          f = open(filename, "a", encoding="utf8")
                                          f.write("\n")
                                          f.write("using " + file.strip() + " answering: " + user)
                                          f.write("\n")
                                          f.write("score: " + str(threshold))
                                          f.write("\n")
                                          f.write("[" + sentenceA + token + "]")
                                          f.write("\n")
                                          f.write("[" + sentenceB + token + "]")
                                          f.write("\n")
                                          f.close()
   