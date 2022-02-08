# AWS_Website_VisitorCounter
A project to create a visitor counter on a website that bilaterally updates DynamoDB through an API

Step 1 - use the HTML and CSS files to style your own CV with your details 

Step 2 - put all of these in a folder with the apifetch_resume.js file and upload them to an S3 bucket 

Step 3 - Enable static website hosting, make the bucket public 

step 4 - Create a cloudfront origin and use the S3 bucket as an origin 

step 5 - Create a table in dynamoDB called "cloud-resume" with a new item called "view-count" and a "quantity" key 

step 6 - Create two Lambda functions (see backend folder in this respository) and link each one to API Gateway 

step 7 - Create an api with two GET methods that are triggered by the Lambda functions respectively 

step 8 - take the invoke URLs from both the ViewCount method and the IncrementViewCount methods and paste them into the fetch link part of 
         the .js api file in the front end folder 
         
step 9 - visit your website using the cloudfront distribution link and you should see the "you are the * visitor" html update with each refresh 
         of the page. 
         
Step 10 - check the dynamoDB table you made earlier to see if it updates to the same number as that you see on the html of the website. 
