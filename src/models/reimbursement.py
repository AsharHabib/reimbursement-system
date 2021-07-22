# Import the JSONEncoder from json so we can serialize the dictionary from the service methods,
# make the controller return a JSON object
from json import JSONEncoder

class Reimbursement():
    #Constructor for Reimbursement object
    def __init__(self, reimbursement_id, employee_id, amount, reason, date_time, status, first_name, last_name,
                 manager_message = 'N/A', job_title=None):
        self._reimbursement_id = reimbursement_id
        self._employee_id = employee_id
        self._amount = amount
        self._reason = reason
        self._date_time = date_time
        self._status = status
        self._first_name = first_name
        self._last_name = last_name
        self._manager_message = manager_message
        self._job_title = job_title

    #Setter for the manager_id
    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

# Define the ReimbursementEncoder, have it inherit from JSONEncoder
class ReimbursementEncoder(JSONEncoder):
    # Override the default
    def default(self, reimbursement):
        if isinstance(reimbursement, Reimbursement):
            return reimbursement.__dict__
        else:
            return super().default(self, reimbursement)