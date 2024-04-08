import spacy

############# loading model #################
nlp = spacy.load("en_core_web_md")
# 'en_core_web_md' the model is able to identify similarities in words through categorisations such as whether they are animals and fruits, 'en_core_web_sm' this model does not have a vector model so it does not give useful judgement because you are using a smaller model.

############## comparable description ##############
description_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

############# Movie recommendation function ###############
print("Recommended Movies:")

# recommended movie list initialized
recommended_movies = []

# defining the movie recommendation function
def movie_Recommendation(description_to_compare):
    '''This method will be used to evaluate different movie descriptions and return movie titles that have a similiar descriptions

        :param string description_to_compare: the movie description

        :returns: the movie title with a similiar description

        :rtype: string
    '''
    # opening and reading the movie file
    with open("movie_collection/movies.txt", "r") as file:
        # reading each individual line
        lines = file.readlines()
        # looping through each line
        for line in lines:
            # splitting the movie title and description through ':'
            the_Movie = line.split(":")
            # processing comparable description
            model_sentence = nlp(description_to_compare)

            similarity = nlp(the_Movie[1]).similarity(model_sentence)
            # Assuming the similarity threshold within the similarity spectrum is 0.85 
            if similarity >= 0.85:
                recommended_movies.append(the_Movie[0])
        return recommended_movies
# running the function
result = movie_Recommendation(description_to_compare)
print(result)