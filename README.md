# Hold the door

This is a very fun project done to cast online votes on a website. But the twist is that there must be a lot of votes to be casted, so no simple human can't do the trick. That is where python comes to the rescue. The idea is to write scripts that can bypass captchas, server limits and more to cast the required amount of votes.

There are 6 site trying to hold the door, the idea is to breach them all.

<img src='./giphy_hodor.gif '/>
art by [@mthbitencourt](https://twitter.com/mthbitencourt)

Each level gets harder and harder, as more complex captchas, restriction
like 'only from windows users' and 'one voter per person per day' are added.

## Files

My id is 98, and here are the sites that were fooled into voting for me.

* Level_0

The level_0 challenge is to vote on this [site](http://158.69.76.135/level0.php). This is a rather simple task, and the purpose it to understand how `http` requests work and how to send them using `python`. 

The task has been accomplished with the scripts under the [Level_0](./Level_0) folder.  To acomplish this task different liberaries like the python `requests` liberary has been utilized

* Level_1

The level_1 challenge is to vote on this [site](http://158.69.76.135/level1.php). This is one introduced me to the idea of sessions as session keys were utilized to communicate with the server. 

The task has been accomplished with the scripts under the [Level_1](./Level_1) folder.  To acomplish this task different liberaries like the python `requests` liberary has been utilized, along with its `sessions` class.

* Level_2

The level_2 challenge is to vote on this [site](http://158.69.76.135/level2.php). This is one introduced me to the idea of headers as the only accepted votes can came from windows users. 

The task has been accomplished with the scripts under the [Level_2](./Level_2) folder.  To acomplish this task different liberaries like the python `requests` liberary has been utilized, along with its `sessions` class and the idea of `headers`.

* Level_3

The level_3 challenge is to vote on this [site](http://158.69.76.135/level3.php). This is one introduced me to the idea of bypassing simple captchas using simple image processing and OCR's. 

The task has been accomplished with the scripts under the [Level_4](./Level_4) folder.  To acomplish this task different liberaries like the python `PIL`, `requests` liberary has been utilized, along with its `sessions` class, and the `tesseract OCR` progam.

* Level_4

The level_4 challenge is to vote on this [site](http://158.69.76.135/level4.php). This is one introduced me to the idea of `proxies` as one person was only allowed to vote once per day.

The task has been accomplished with the scripts under the [Level_4](./Level_4) folder.  To acomplish this task different liberaries like the python `scrapeproxy`(which scraps free proxies out there), and `requests` liberary has been utilized, along with its `sessions` class.

* Level_5

The level_5 challenge is to vote on this [site](http://158.69.76.135/level5.php). This is the accumulation of all the difficulties, it has a little bit more harder captcha's and it conly take votes from windows users. So it required the merging of all the knoweldge aquaired over the course of the previous projects.

The task has been accomplished with the scripts under the [Level_5](./Level_5) folder.  To acomplish this task different liberaries like the `PIL` and `requests` liberary has been utilized.

## Tools Used

Here is a summary of all the python liberaries and tools used.

* `requests`
* `PIL`
* `time`
* `bs4`
* `os`
* `subproccess`
* `proxyscrape`
* `tempfile`
* `concurrent`
* `io`
* `tesseract` - for extacting text from images

## Author

Hileamlak M. Yitayew

