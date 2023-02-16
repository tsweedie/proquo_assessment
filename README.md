# Tshidi's ProQuo AI Assessment

This file contains the instructions on how to run the respective programs for each question. The last questions answers are contained within the README.

 Repo Organization
------------

    ├── README.md          
    ├── data
    │    ├── dob.txt          <- Pipe delimited `name|date-of-birth` data
    ├── 1_file_reading.py     <- Answer to assesment Question 1
    ├── 2_beep_boop.py        <- Answer to assesment Question 2
    └── 3_smoothy.py          <- Answer to assesment Question 3 
------------

Question 1 – File Reading
------------
1. In your terminal navigate to the `proquo_assessment` project folder
2. run `python 1_file_reading.py data/dob.txt`

_Note: You can add own pipe delimited (`name|date-of-birth`) data source to `data/`_


Question 2 – Beep Boop
------------
1. In your terminal navigate to the `proquo_assessment` project folder
2. run `python 2_beep_boop.py`

Question 3 – SmOOthy
------------
1. In your terminal navigate to the `proquo_assessment` project folder
2. To create two different flavour smoothies:
    - `python 3_smoothy.py --name "Strawberry Blaze" --fruit strawberry 200 --fruit banana 100 --fruit apple 50`
    - `python 3_smoothy.py --name "Citrus Infusion" --fruit orange 100 --fruit apple 75 --fruit lemon 100 --fruit orange 50`
3. To create your own smoothie use `--name [SMOOTHY_NAME]` to name your smoothy and `--fruit [FRUIT] [GRAMS]` to add fruit to your smoothie
4. Fruit options: `banana, orange, apple, strawberry, lemon`

_Note: Run `python 3_smoothy.py -h` for help and to get the allowed arguments for the program_

Question 4 – SQL
------------

4.1 - Show the total sum of all polices by policy type
```sql
SELECT 
       SUM(Balance) AS Total, 
       PolicyType, 
FROM Policy
GROUP BY PolicyType

```

4.2 - Show the total of sum of all account transactions for each account by transaction type (TranTypeId)
```sql
DECLARE @colnameList varchar(200)
SET @colnameList = NULL
SELECT @colnameList = COALESCE(@colnameList + ',','') + TranTypeId FROM AccTran;
DECLARE @SQLQuery NVARCHAR(MAX)
SET @SQLQuery =
'SELECT AccountId , '+@colnameList+'
FROM
(
    SELECT AccountId, TranTypeId, Amount FROM AccTran
) AS tbl
PIVOT 
( 
    SUM(Amount)
    FOR TranTypeId IN ('+@colnameList+') 
) AS pvt'

EXEC(@SQLQuery)
```

4.3 Show a breakdown of each policy balance by account
```sql
SELECT a.Balance, a.PolicyName, b.Name, b.ID AS ID
FROM Policy AS a
JOIN Account AS b 
ON a.AccountID = b.ID
GROUP BY ID
```

4.4 Show all policies whose balance does not equal the sum of their respective AccTran transactions, sort by account name
```sql
SELECT a.PolicyId, a.Total, b.Balance, b.ID
FROM (
        SELECT SUM(Amount) AS Total,
               PolicyId
        FROM AccTran
        GROUP BY PolicyId
) AS a
JOIN Policy AS b 
ON a.PolicyId = b.ID
GROUP BY ID
WHERE a.Total != b.Balance
```