<h1>Syllahub</h1>
<p>Revamping the syllabus management system</p>

<hr>
<h3>Python</h3>
<p>I am using <a href="https://www.python.org/downloads/">python 3.7.2</a>. I think this is the most recent stable version. <strong>Make sure you are using the correct python command that is mapped to the correct python version.</strong></p>
<h5>Common python commands are:</h5>
<ul>
    <li>$ python</li>
    <li>$ python3</li>
    <li>$ py</li>
    <li>$ py3</li>
</ul>
<h5>Check python version for each command with: </h5>
<ul>
    <li>$ python -V</li>
    <li>$ python3 -V</li>
    <li>$ py -V</li>
    <li>$ py3 -V</li>
</ul>

<h3>Flask Instalation instructions</h3>
Once you clone the git repository, you must do a couple things to get this working on your local machine. 
<ul>
    <li>
        cd to Syllahub directory
    </li>
    <li>
        Create Virtual Environment
        $ python -m venv venv<br>
    </li> 
    <li>
        Activate virtual environment <br>
        $ source venv/bin/activate<br>
        (venv) $ _
    </li>
    <li>
        install all required packages from requirements.txt<br>
        (venv) $ pip install -r requirements.txt<br>
        <strong>Note:</strong> if you change the packages you must update requirements.txt with: <br>
        (venv) $ pip freeze > requirements.txt
    </li>   
</ul>

<hr>
<h3>Related Flask Tutorial</h3>
<p><a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">The Flask Mega Tutorial</a> is a good start if anything here confuses you.</p>