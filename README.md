**Expense Reimbursement System (Python)**

_Project Description_

The Expense Reimbursement System (ERS) will manage the process of reimbursing employees for expenses incurred while on company time. All employees in the company can log in and submit requests for reimbursements and view their past tickets and pending requests. Managers can log in and view all reimbursement requests and past history for all employees in the company. Managers are authorized to approve and deny requests for expense reimbursements.

_Technologies Used_

    JavaScript
    HTML
    CSS
    SQL
    Python
    Flask
    Postman
    AWS RDS

_Features_

List of features ready and TODOs for future development

    Login/Logout for employees and managers
    Options to reset username/password
    Two Factor Authentication
    Both employees/managers can view past reimbursement requests
    Employees can submit requests, managers can approve or deny
    Managers can view a statistics page

To-do list:

    Improve the UI
    Add more verification for user input

_Getting Started_

Open Git Bash and enter the following commands:

git clone https://gitlab.com/christina.russ/6-7-2021-pyjwa.git

git checkout ashar_habib

git pull

_Usage_

After installing, simply run main.py and go to http:/localhost:5000/pre_login, and choose the account type to log in as (employee or manager). Enter the respective credentials, log in, and you are sent to a profile page. As employee, you may view your past reimbursement requests by clicking the Reimbursement Requests tab, and you may submit one with by clicking the link on the Requests page.

As manager, you may view a list of all your employees and their job titles on the Profile page. You may view your employees' submitted reimbursement requests by clicking the Reimbursement Requests tab, and update them by changing the status and clicking the Update Requests button. Finally, you may view the requests' statistics by clicking the Statistics tab.
