# Blockchain_NLP

# Natural Language Processing and the Currency of the Future
Team members: **Jeremy Lagunas**, **Lindy Castellaw**, **Luis Arce**, **Tim Keriazes**

## [Final Presentation](https://docs.google.com/presentation/d/1c7miCoOi6WboRbjxgJ3QwWLkWU0SzZHA5WGdjdK600U/edit?usp=sharing)

September 08, 2022

***

## Introduction

Given the rise in popularity in cryptocurrencies, the rise in awareness of sound money and monetary curiosity, as well as the current, very real, rise in inflation, we thought it would be fitting to incorporate the topic of defi, or Decentralized Finance, into our Natural Language Processing Project. Defi is a new field of technology which utilizes distributed ledgers and smart contracts. It seeks to disrupt the current centralized financial system controlled by banks and institutions by providing alternate means of money, financial interactions and services. 

## Project Description

Utilizing the contents of readme files within repositories on github, we set out to build a predictive model that would allow us to determine the programming language of the repository/project based on the contents of the readme. Utilizing web scraping techniques, we built a dataset containing the name of the repository, the programming language utilized, and the contents of the readme. Through some basic cleaning and preparation, we will explore the dataset, looking for patterns, and creating some visualizations that show the most common words in the readme, whether the length varies by programming language, unique words, and any other identifying features. We will utilize the TfidfVectorizer() to transform the contents of the readme into features that will be fed into our predictive classification models. Utilized the following libraries; pandas, numpy, matplotlib, seaborn, wordcloud, nltk, unicodedata. Modeled using sklearn’s DecisionTreeClassifier and RandomForestClassifier and evaluated with sklearn’s metrics including classification report, confusion matrix, and mean squared error.. 

## 📈   Project Goals

- Successfully acquire and clean necessary data.
- Generate insightful visuals to show findings and data relationships.
- Generate a predictive model which accurately predicts the main programming language of a Repo based on that Repo's README text. 

## 📅  Project Outline

1. Investigate the repository search #defi.
2. Capture the urls and endpoints for each repo.
3. Acquire the data: Use the GitHub API to access the data and convert it into a DataFrame. (Our data comes from searching #defi as of 09/02/2022)
4. Clean the data: Remove special characters, lemmatize it, remove stop words, and handle nulls.  
5. Explore the data: Find the most common words overall, see each programming language's most common words, and try to see if there are words which uniquely identify a programming language. 
6. Model the data : Establish baseline, transform the data for modeling, fit the models, and build a function that will take in the text of a README file, and try to predict the programming language.
7. Evaluate the models: Compare the performace of the models to each other and to the baseline. Determine which model will be used on test data.
8. Perform final model evaluation on test data.
9. Conclusion, Takeaways, and Next Steps. 

***

## :open_file_folder:   Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*language* | string | The primary programming language of the repo.
*repo* | string | The name of the repository.
*readme_contents* | string | The text in the README of the repo.



<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

## Exploration Key Findings

1. The 10 most common words and number of appearances in the READMEs:
    **Word** | **Appearances**
    ---|---
    contract | 3914
    token | 3460
    run | 1740
    1 | 1722
    smart | 1622
    ethereum | 1530
    project | 1530
    address | 1503
    detail | 1499
    install | 1438
    
2. Of the 1000 repositories that were pulled, the most common languages were as follows:
    **Language** | **Breakdown**
    ---|---
    JavaScript | 0.237624
    TypeScript | 0.221782
    Solidity | 0.165347
    Not Specified | 0.127723
    Python | 0.058416
    Rust | 0.031683
    Go | 0.025743

3. The top ten bigrams that appeared and their number of occurences across all languages:
    **Bigram** | **Occurences**
    --- | ---
    (smart, contract) | 1348
    (git, clone) | 759
    (detail, detailssummaryba) | 670
    (styledisplayinline, width13) | 414
    (npm, install) | 350
    (srchttpsgitioj9co9, styledisplayinline) | 342
    (npm, run) | 321
    (decimal, 18) | 315
    (chainid, 1) | 309

4. The length of READMEs did vary by programming language. 

5. JavaScript and TypeScript utilized characters/words much more than other programming languages. 

***

## <a name="model"></a>Modeling


### Baseline
    
Baseline will be predicting the language to be the most popular language (JavaScript).
- Baseline Results: 0.243351
    

       
## Model Performance on Validate

### Model 1: Decision Tree (DT)


- Model 1 results: 0.351064



### Model 2 : Random Forest (with a max depth of 6)


- Model 2 results: 0.734043



## Selecting the Best Model:


| Model | Performace |
| ---- | ----|
| Baseline | 0.243351 |
| Decision Tree (DT) | 0.351064 |  
| Random Forest | 0.734043 |   


- Random Forest model performed the best


## Testing the Model

- Model Testing Results: 0.684211

***

## Steps to Reproduce
    1. Ensure you have the necessary token to access GitHub's API.
    2. Import the necessary libraries.
    3. Utilize the acquire.py file to acquire the data. 
    4. Utilize the prepare.py file to clean the data. 
    5. Run the nlp_repository_classification_project_final_nb.ipynb

***

## <a name="conclusion"></a>Conclusion

We found that the most popular languages were JavaScript, TypeScript, Solidity, and Python.
The most common words used across all READMEs were contract, token, and run.
Our final model (Random Forest max depth of 6) performed with an accuracy of 68.4%. 
We didn’t expect there to be so many repos that aren’t labeled with a language and we didn’t expect so many random numeric strings to show up during our Feature Engineering.

If we had more time, we would investigate similarities across languages to see if we can determine the computing language used by unlabeled repositories. 

***

[[Back to top](#top)]

