### [mer](https://www.youtube.com/watch?v=EoQW03UFqQw)

Grab a random commit message from GitHub.

#### Get started

Set your own API key in the env variable:

```
token = os.environ.get('YOUR_GITHUB_API_KEY')
```

mer will prompt you for your GitHub login.

***Note*** For unauthenticated requests, the [rate limit](https://developer.github.com/v3/#rate-limiting) allows for up to 60 requests to be made per hour.



#### Install

`sudo make install`

`mer -c or --commit`

![mer in action](https://github.com/Gusbenz/mer/blob/master/merInAction.jpg)


#### TODOs

* IndexError bug
* Other bugs :smile:
* Persist user auth so as to not prompt for user login every time :thumbsup:
* Add more flags so this is more useful :grin:
