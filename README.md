<p>Please refer to https://github.com/velinovasen/bethub_rebuild for the rebuild version.</p>

<h1>BETHUB</h1>
    <b>A web-crawler which checks multiple websites and stores the data into postgres.
    Then we use data to create a bookmaker, where you could place bets and participate in a
    betting competition. Every user can place predictions while using our widgets, which are
    following the most placed odds in Europe at the moment, an automatic prediction and 
    current value bets.</b>

<h2>Installation</h2>
    <b>Pull the repo, install the requirements.txt file and run run_all.py from our scrapers to get the most recent information.</b>
    <b>Don't forget to change the path we append in the top of each scraper!!! -> </b>
    <b>sys.path.append('enter the path to your project')</b>
    
<h3>Things working on:</h3>
<ul>
    <li>Hook celery worker to automate the process</li>
    <li>Add few more scrapers to help the process</li>
    <li>Finishing the trends scraper, which we can hook to a twitter bot</li>
    <li>Add another app, which users can buy other users bets, simulating a market</li>
</ul>


<b>Home page</b>
<img src="https://serving.photos.photobox.com/2642966131f0d7b5cba0929c1f123c7d53be8587e111a63579c15354167ac927e12ee69a.jpg">

<b>Traffic page</b>
<img src="https://serving.photos.photobox.com/67491438c6cca24f52d9669fbf4531bb6b62e7c741496e4a9ae02073fd0cd1c015abd510.jpg">

<b>Predictions page</b>
<img src="https://serving.photos.photobox.com/97665076bb2e31b5daaac003915cd5cfed098de1ae854ed69d0958bf8b0d36d3ddad9bfd.jpg">
