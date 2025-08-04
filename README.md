# OOP-Math-microservice
A python developed Math microservice that uses predefined functions like fib, power and ! to calculate equations.



	Database visualization : https://inloop.github.io/sqlite-viewer/ -> request.db introduced in this sqlite viewer to view the database

	JSON visualization : log.json - visualizing the querrys live being introduced

	Directors : -db -> Database (director where the Python database code is located)
            -services -> MathService ( director where are the three main functions used in Python: fibonacci, power and factorial)
            -templates -> index.html ( template for the API )
	    
	Math_microservice_main : the main Python code where the applications start.
	Requirements: install flask - pip install flask
	      install pydantic - pip install pydantic


	STEP 1.
	
	Creating the python scripts :

	1.Database.py            - creates the database in which the querrys are storaged.
	2.inputs.py              - it includes the pydantic library into the main project, creating an alert when the users introduce a   number that can't be calculated.
	3.MathService.py         - script where can be found the three main functions used: fibonacci, power and factorial.
	4.Math_microservice_main - this script is where the main project can be run .
