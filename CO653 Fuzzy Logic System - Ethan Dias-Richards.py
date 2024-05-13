import json

print("\n\nFuzzy Logic System - Ethan Dias-Richards\n")

Q1 = input("What is your favourite movie genre?\n\n")

#Rules

# IMDB rating over 8 means movie is good but can also be considered very good by critics and people who have reviewed it

if Q1 == "action":
    
   print("\nRecommendations\n\n")
   
   with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/action_movies.json') as f:           
                array = json.load(f)
                
   for item in array:
            if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
                        
                
elif Q1 == "comedy":
     
               print("\nRecommendations\n\n")
                           
               with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/comedy_movies.json') as f:           
                    array = json.load(f)
                 
               for item in array:
                    if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
                       
                
                    
elif Q1 == "romance":

   print("\nRecommendations\n\n")
   
   with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/romance_movies.json') as f:           
                array = json.load(f)
                
   for item in array:
            if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
                
                
                    
elif Q1 == "sci-fi":
     
   print("\nRecommendations\n\n")
   
   with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/sci-fi_movies.json') as f:           
                array = json.load(f)
                 
                for item in array:
                    if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
                    
                    
elif Q1 == "horror":

   print("\nRecommendations\n\n")
   
   with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/horror_movies.json') as f:           
                array = json.load(f)
                
                for item in array:
                    if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
                    
elif Q1 == "animation":
    
   print("\nRecommendations\n\n")
    
   with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/animation_movies.json') as f:           
                array = json.load(f)
                
   for item in array:
            if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
               
elif Q1 == "adventure":
    
   print("\nRecommendations\n\n")
    
   with open('C:/Users/Ethan Dias-Richards/Documents/Bucks New University/Year 3/Learning Machines & Intelligent Agents/adventure_movies.json') as f:           
                array = json.load(f)
                         
   for item in array:
            if item['imdb_rating'] >= str(8):
                       print("Title:" + "\n" + item['title'] + "\n" + "Genres:" + "\n" + item['genres'] + "\n" 
                      + "IMDB Rating:" + "\n" + str(item['imdb_rating']) + "\n" + "Meta Score:" + "\n" + str(item['meta_score']) + "\n") 
              


            
                    
                    
                    
            




       
       
       
       

    
    
    