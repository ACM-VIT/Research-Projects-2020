# Text-Summarization
Articles from wikipedia can be extracted and can be summarized down to a short and simple paragraph for a quick read.The summary contains the parts which is most repeated in the text because a good summary does not go into the details too much but tells only the most important part.If you observe any speech or article closely , you will notice that emphasis is always put on important parts by repetetive discussion over that topic or even by repeating the same sentences. The unimportant facts(to the summary) are left out hence, because a summary is only a gist of the main thoughts behind the article. 

Step1:
Fetch the article you want to summarize using the urllib module.This returns the HTML of the article page.

Step2:
Install and import the required libraries. I have used BeautifulSoup and lxml for parsing the article.In Wikipedia articles, all the text for the article is enclosed inside the <p> tags.So we extract all the text from the paragraphs and add them into the common article_text variable.
  
 Step3: (PREPROCESSING)
 
 We remove the references(using re-"import re") from the article which are found enclosed in square brackets.We also create a formatted text variable which doesn't contain any numbers or punctuations (using re itself) etc.
 
 Step 4:
 Import nltk. Using the formatted article(the one without punctuations and stuff) , we find the weighted frequency of each word. The weighted frequency of a word is nothing more than the frequency of that word in the whole article divided by the frequency of the most used word.
 
 Step5:
 We then find the sentence score which is the sum of the weighted frequencies of the words(not stopwords though-their weighted frequencies are not even calculated) which are present in the sentence.
 
 Step6:
 The top 7 sentences (depends on how big you want the summary to be)  , that is the sentences with the highest sentence scores are joined together to form the final summary which is displayed.
 To find the top 7 sentence scores, i have used heapq which has to be imported.

