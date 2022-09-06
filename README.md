# Blockchain_NLP

# Natural Language Processing and the Currency of the Future
Team members: **Jeremy Lagunas**, **Lindy Castellaw**, **Luis Arce**, **Tim Keriazes**

## [Final Presentation](https://docs.google.com/presentation/d/1c7miCoOi6WboRbjxgJ3QwWLkWU0SzZHA5WGdjdK600U/edit?usp=sharing)

September 2022

## 📈   Project Goals

We will build a model to succesfully predict the programming language of a DeFi (Decentralized Finance) respository, given the text of the README file. 



## :open_file_folder:   Data Dictionary
**Variable** |    **Value**    | **Meaning**
---|---|---
*date* | datetime | The date of log entry
*time* | datetime | The time of the day of log entry
*path* | string | The path the user is on
*user id* | float | The primary key of log table, indicating each user
*ip* | string | The user's ip address
*name* | string | The name of user's cohort
*slack* | string | The name of the slack chanel that user belongs to
*start date*| datetime | The start date of the cohort
*end date* | datetime | The end date of the cohort
*program id* | datetime | This indicates which program is the user in


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

## :placard:    Project Plan
#### :one:   Data Acquisition

<details>
<summary> Gather data from GitHub Repositories</summary>

- Create env.py file to establish connection with GitHub

- Use **curriculum_log** database in the mySQL server

- Write query to join useful tables:  <u>cohorts, logs</u>
     ```sh
      SELECT 
        date,
        time,
        ip,
        path,
        user_id,
        cohort_id,
        name as cohort_name,
        slack,
        start_date,
        end_date,
        program_id
     FROM
        curriculum_logs.logs
     join
        curriculum_logs.cohorts on cohort_id = id
     ```
</details>

<details>
<summary> acqure.py</summary>

- Create acquire.py and user-defined function `get_data()` to gather data from mySQL
     ```sh
     def get_data():
        if os.path.isfile('curriculum.csv'):
    
            df = pd.read_csv('curriculum.csv', index_col=0)
        
        else:

            df = new_data()

            df.to_csv('curriculum.csv')
        
        return df
    ```
- Import [acquire.py](acquire.py)

- Test acquire function

- Calling the function, and store the table in the form of dataframe
    ```sh
    df = acquire.get_data()
    ```
</details>

#### :two:   Data Preparation

<details>
<summary> Data Cleaning</summary>


</details>

#### :three:   Exploratory Analysis

    
## 📅 Timeline for Data Science Team
By September 2nd
- [x] Sketch out plan and assign each team member task
- [x] Data Acquisition: acquire data from GitHub repositories
- [x] README initial structure



## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]

