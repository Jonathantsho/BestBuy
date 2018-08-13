# Best Buy

## Built With

* [Adwords API](https://developers.google.com/adwords/api/docs/guides/start) - Google Adwords API
* [Azure Data Lake Store](https://docs.microsoft.com/en-us/azure/data-lake-store/) - NoSQL Data Store for Adwords Dummy Data + Potential Other Sources
* [Azure Data Factory](https://azure.microsoft.com/en-us/services/data-factory/) - Data Pipelining tool for SQL & NoSQL Integration
* [Azure Data Lake Analytics](https://azure.microsoft.com/en-us/services/data-lake-analytics/) - Data Transformation Tool
* [PowerBI](https://powerbi.microsoft.com/en-us/) - Visualization tool

## Getting Started

The purpose of this mini project was to demonstrate data integration of multiple data sources into the Azure Data Lake pipeline. 

### Why I used a Data Lake over a Data Warehouse?

- Data Lakes Handle unstructured to semiunstructured data types very well
- Data does not need to be structured to a set schema, thus can be read very easily and quickly
- Data is loosely structured in a lake, work can be very agile and changes can be made on the fly.
- Integrating new data sources is very easy, data does not need to be transformed prior entering the lake.

## First Step - Create Dummy Data Sources
- Created different dummy data sources with
- AWS S3 - Simple Storage Service - Adwords Dummy Data
- Local Python API: connects my Adwords account to Azure Data Lake

![screen shot 2018-08-12 at 9 18 30 pm](https://user-images.githubusercontent.com/14828681/44012632-60f91e52-9e75-11e8-9175-697b5feb3dba.png)



![screen shot 2018-08-12 at 9 21 12 pm](https://user-images.githubusercontent.com/14828681/44012676-b35b3fb8-9e75-11e8-9b5e-23c7bf1afd00.png)

## Second Step - Create Azure Data Lake Store
-Create an Azure Data Lake Store (When you first create it, theres no data)
![screen shot 2018-08-12 at 9 22 59 pm](https://user-images.githubusercontent.com/14828681/44012711-f7a95e52-9e75-11e8-9c9d-0802446a1ea5.png)


## Third Step - Create a Azure Data Factory Pipeline between S3 and ADLS
-Create a data pipeline and a job process to run batch integration jobs between S3 Data to ADLS.
- Here I'm transferring over all 75 TSV files containing dummy Adwords data into our ADLS Store.

![screen shot 2018-08-12 at 9 26 11 pm](https://user-images.githubusercontent.com/14828681/44012784-5fc4ad84-9e76-11e8-9bd4-b0115424d6e2.png)

- What the Dataset looks like 

![screen shot 2018-08-12 at 9 36 57 pm](https://user-images.githubusercontent.com/14828681/44013020-e0c37720-9e77-11e8-8287-f9bda4b11f09.png)


## Fourth Step - Create Azure Data Lake Analytics Tool
-Once data has been loaded into ADLS, it has to be transformed to be visualized or used by data scientists/analysts alike.
-We need to re-compile all 75 TSV files into 1 TSV in order to continue with our work.


### Writing a U-SQL Wrangling/Processing Script
-In order to transform the data at hand, we need to write a U-SQL Script (Combination between SQL + .NET Code)
-This helps clear out some of the Missing/Null Values
-Sets correct Encoding (Unicode-UTF-8)

![screen shot 2018-08-12 at 9 31 37 pm](https://user-images.githubusercontent.com/14828681/44012887-20022b8a-9e77-11e8-9817-709e7f8f2d47.png)

### Submit the job, and visualize the processing/computation.

![screen shot 2018-08-12 at 9 29 04 pm](https://user-images.githubusercontent.com/14828681/44012834-c4ca7e48-9e76-11e8-9fe1-c0392b2bce8b.png)


## PowerBI - Take the transformed/compiled dataset and load into PowerBI

![39070117_1350083351791227_4854565186360573952_n](https://user-images.githubusercontent.com/14828681/44012953-85810738-9e77-11e8-8bae-982160c297d0.png)



# Final Thoughts

- We weren't allowed to use our Developer Token until it was approved by Google. Couldn't pull data from our production account.
- Some of the data is not transformmed 100% correctly, but for the purpose of demonstration, this is a quick way to create a data pipeline that can allow analysts/scientists to visualize data sources quickly and responsively. 



