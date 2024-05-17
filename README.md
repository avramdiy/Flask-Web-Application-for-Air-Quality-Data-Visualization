# Flask-Web-Application-for-Air-Quality-Data-Visualization

<p>Created aq_dashboard.py to run a basic Flask application<br>
<p>Downloaded openaq.py to communicate with OpenAQ API<br>
<p>Implemented 'get_results' function to retrieve 2.5 particulate matter data with (utc_datetime, value) tuples<br>
<p>Defined a 'Record' model with '__repr__' & 'refresh' route to retrieve data from OpenAQ to fill the 'id', 'datetime', 'value' columns <br>
