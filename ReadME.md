Requirements:
Swarm Challenge

Basic Specifications
1.  request: url <String>
    output: shortened Link <String>
2.  Request: Url With Shortened Link
    output: Redirection to previous URL

Optional Features
1.  allow user to choose the hash-code.
2. 

Folder Structure:
Basic -> Fulfilling bare minimum requirements. Minimal testing.

Optional1 -> Basic + Optional Feature 1


Optional2 -> Optional 1 +


REQUEST: Actual link -> RESPONSE: return hash or full shortened link

REQUEST: Shortened/hidden link -> RESPONSE: should redirect IF HAS MATCHING LINK otherwise return not found response
In the request body, the user may also provide an “alias”, using the alias, they can be redirected to the actual link (optional)

Tech
Language: Python - vanilla, flask, django
Database: Feel free to use any, can use in-memory (lists/dicts)

Deployment/Demo
Local OR 
AWS lambda/GCP cloud functions (optional)
