# AWS_Website_VisitorCounter
A project to create a visitor counter on a website that bilaterally updates DynamoDB through an API and then links this to the front end HTML.  

I began this project by writing my CV using some basic HTML and then styling it using CSS. I made sure to link the apifetch_resume.js
within the HTML - more on this further down. 

I manually uploaded all of the front-end files to an S3 bucket and the nena bled website static hosting. For practical uses this is ok, but 
there are a couple issues with relying on this alone: 

         1 - As the S3 bucket is hosted in the us-east-1 region, users who are not located close to this geography will potentially have
             a suboptimal experience in accessing the content. 
         2 - We cannot deliver this static website using HTTPS. This means that there is no SSL certificate issued to the link and that
             the data will not be encrypted in transit: which means that malicious actors will be able to read and modify the contents of 
             the bucket. 
             
Both of these potential issues led me to look towards the main CDN (content delivery network) of AWS for solutions, cloudfront. 
This not only provides the ability to issue an SSL certificate for HTTPS security on the provided link, but gives the ability of 
an edge-location based caching system which will allow for optimal performance in accessing the content regardless of the users geography. 

After using the S3 bucket as the origin for my cloudfront distribution a link was given to access my website. Although it worked well, 
the link itself was a bit ugly and cumbersome. This led me to Route 53 to create a CNAME (a sub domain) for the main A record I had created 
to host my resume on - resume.mkalich.cloud 

With regards to the backend of this project, I began by creating a simple DynamoDB table entitled "Cloud-Resume" with a single item entitled "view count". 
Making use of Lambda's serverless feature for hosting code and triggering other services, I created 2 functions using AWS's python-based SDK, boto3. 

For the GetValue function (please see backend folder), after importing the SDKs and setting the variables to the correct services and item of the database,
I wrote a simple lambda handler which makes use of boto3's get_item function to retrieve a specific key from DynamoDB if possible and return a HTTP 200 
OK status code. 

The code is similar in the IncrementViewCount function except the update_item method is used to trigger and API endpoint which accesses the current visitor 
count item in DynamoDB, increments it by one, stores the value back in the database and returns the new value to the front end. 

After this, I made use of Lambda's proxy integration to proxy all of an API gateways requensts to both Lambda functions. 
When I first created an API to integrate these Lambda functions to the DynamoDB table, a source of confusion was whether to use a GET or POST Method as a 
means to increment the value of the databse and front end.

I realised that the POST method would be more suited to user-sided data entry, such as passwords and details, rather than them simply refreshing a URL. For 
this reason I opted to use 2 GET methods for the API. I chose to use a Rest API due to the increased customisation, integration and management features it 
posesses - but could quite as easily have used a HTTP API as my application is quite simple and doesn't require too much overhead. 

After staging this API and saving the invoke-url provided by both the get value and increment value methods in the API, I referenced this in the apifest_resume.js 
file in my S3 bucket. 

You can find my finished project at https://resume.mkalich.cloud - The visitor counter is integrated into the HTML, but works bilaterally with the API Gateway,
Lamda functions and DynamoDB to update the table. 

Finally, after I completed this project I realised that to make changes and updates to this HTML file would be cumbersome if I was to continuously reupload 
new html/js code to the S3 bucket. This was when I realised thatI could clone this repository of these files to my desktop, copy in the updated files and 
then push it straight to cloudfront via the S3 bucket using the following commands in my git-bash command terminal: 

git add -A

git commit -a 

git push -f origin main 

From here, I saved the most sensitive access credentials of the AWS bucket and account in Githubs respository secrets, and then referenced the main branch in a useful YAML workflow file found at https://github.com/jakejarvis/s3-sync-action. This allowed for the updated files that I had commited to the repository to be pushed automatically 
to the S3 bucket and Cloudfront - note that it is import to add invalidations to the CloudFront distribution to order to get rid of any previous commits that have been 
cached in one of CloudFronts edge locations. 

From my own education in DevOps and CI/CD practices, this is the most agile way to keep the content of our infrastructure stable, automated and agile. Now with every single 
small commit I add to this content, it will deployed in seconds through Github Actions. This is just a small project to demonstrate what I viewed as infrastructure as code and working within the framework of a DevOps culture.

I hope you enjoyed reading this and it was of any help to your own AWS/CDN or CI/CD projects. 


            
