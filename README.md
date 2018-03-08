# term_extraction

Consider "term_extraction.py" as the main code to be executed. The other python files are *mandatory* however. They are helper functions to generate the various text manipulation / replacement dictionaries, to avoid the primary code from being too terribly long.

term_extraction.py will import the various filter words, EC dictionary, concept dictionary, and weightings from all of other python files. Feel free to make updates to the dictionaries as you see fit. Disagree with our concept categorizations? Make your own!

Before running term_extraction.py, you *must* edit the global variables corpus_path, and output_path, so that the code knows where to access the corpus materials on your drive, and where you want to output the various materials.

You also have the option to customize the number of clusters to be formed, as well as the number of terms you want to be reported for each cluster.

Use the excel file to aid in quickly creating / updating the various dictionaries to help categorize terms, set ECs, etc.

Note on output: since KMeans starts with a randomized vector it means that cluster assignment can change for any "marginal" DSI. For that reason, I output two cluster maps, for both terms matrix, and cluster matrix. The "A" map is set with a fixed seed, so that you can compare the changes you make to the EC / Concepts / Weighting dictionaries on a fixed set. The "B" output is a randomized seed, intended to all you to compare A vs. B, so you can identify which DSI are borderline. Any DSI that jump between clusters should be investigated as likely needing improved EC mapping, more concept separation, or improved term weighting.
