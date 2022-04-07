# spotify_tweet
A python script used to tweet out your recent top tracks on spotify, utilizing AWS lambda.

Remember:
1. Don't put your API credentials in your source code
2. API creds are sensitive info

## Setup Steps
Here are some things you should make sure are
done before working with this repository.

1. Install pip

    http://pip.readthedocs.io/en/latest/installing/#install-pip


2. Install virtualenv
    
    pip install virtualenv
    
    sudo pip install virtualenv

3. Install boto3

    pip install boto3

4. Install the AWS CLI

    pip install awscli

    sudo pip install awscli

    sudo pip install awscli --ignore-installed six

5. Get your AWS Access Keys
    Log into the aws console and follow these
    instructions:

    1. Go to https://console.aws.amazon.com/iam/home?#home
    2. Choose "Users"
    3. Choose your IAM username (not the check box)
    4. Choose the Security Credentials tab and 
    then choose Create Access Key.
    5. To see your access key, choose Show User 
    Security Credentials. Your credentials will 
    look something like this:

    Access Key ID: 
    Secret Access Key: 

    6. Choose Download Credentials, and store 
    the keys in a secure location.
    
6. Configure the AWS CLI

    Open a shell and use this command:

    aws configure

    Follow the prompts and enter in your keys 
    and the reigon you are working in. You can
    see a list of regions and region codes here:
    http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

    AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
    AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    Default region name [None]: us-east-1
    Default output format [None]: ENTER


7. Twython
    pip install twython

    But if you have any issues you can check the 
    documentation here: 
    https://twython.readthedocs.io/en/latest/usage/install.html

8. Spotify
    pip install spotipy

9. Retrieve a refresh token from Spotify (requires a registered Spotify app)
    https://accounts.spotify.com/authorize?client_id=<YOUR CLIENT ID>&redirect_uri=<YOUR REDIRECT URI>&response_type=code&scope=<YOUR SCOPES>

    curl -H "Authorization: Basic <YOUR BASE-64'd APP TOKEN>" -d grant_type=authorization_code -d code=<YOUR ACCESS CODE> -d redirect_uri=<YOUR CALLBACK URL> https://accounts.spotify.com/api/token`

10. Encrypt the refresh token using aws KLM and store in spotify_creds.json

11. Run the setup.sh

12. Upload your package to lambda

13. Set up an event trigger


