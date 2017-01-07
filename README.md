### M.E.R

Meaningless Experiment Realized

Grab a random commit from GitHub.

#### Get started

Set your own API key in the env variable:

`token = os.environ.get('YOUR_GITHUB_API_KEY')`

***Note*** For unauthenticated requests, which these would be, the [rate limit](https://developer.github.com/v3/#rate-limiting) allows for up to 60 requests to be made per hour.

#### Install

`sudo make install`

`mer -c or --commit`

![mer in action](https://github.com/Gusbenz/mer/blob/master/mer.jpg)
