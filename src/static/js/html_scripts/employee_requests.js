//JS function for loading up the requests page for Managers
async function employee_requests() {
//  Fetch the JSON url for data on requests, get the <tbody> and <form> tags by ID
    const url = 'http://localhost:5000/requests.json'
    const response = await fetch(url)
    const reimbursements = await response.json()
    const tbody = document.getElementById('employee-requests')
    const form = document.getElementById('update-requests')
//  For loop to iterate over the reimbursements and dynamically make table rows for the <tbody>
    for(let index in reimbursements) {
//      Create the tr tag
        const tr = document.createElement('tr')
//      Create the td tag for the employee name, append to tr
        const td_name = document.createElement('td')
        td_name.innerText = `${reimbursements[index]._first_name} ${reimbursements[index]._last_name}`
        tr.appendChild(td_name)
//      Create the td tag for the employee job title, append to tr
        const td_job_title = document.createElement('td')
        td_job_title.innerText = `${reimbursements[index]._job_title}`
        tr.appendChild(td_job_title)
//      Create the td tag for the amount, append to tr
        const td_amount = document.createElement('td')
        td_amount.innerText = `$${reimbursements[index]._amount}`
        tr.appendChild(td_amount)
//      Create the td tag for the reason, append to tr
        const td_reason = document.createElement('td')
        td_reason.innerText = `${reimbursements[index]._reason}`
        tr.appendChild(td_reason)
//      Create the td tag for the current status, append to tr
        const td_status = document.createElement('td')
        td_status.innerText = `${reimbursements[index]._status}`
        td_status.setAttribute('id', `status-${reimbursements[index]._reimbursement_id}-${reimbursements[index]._employee_id}`)
        tr.appendChild(td_status)
//      Create the td tag for the time submitted at, append to tr
        const td_time = document.createElement('td')
        td_time.innerText = `${reimbursements[index]._date_time}`
        tr.appendChild(td_time)

//      Create a td to hold an input of type radio, pre-defining a reimbursement_employee_manager_id because it will
//      be used many times below
        const reimbursement_employee_manager_id = `${reimbursements[index]._reimbursement_id}-${reimbursements[index]._employee_id}-${reimbursements[index]._manager_id}`
        const td_change_status = document.createElement('td')
        const pending = document.createElement('input')
//      Create a pending radio button, name is status-reimbursement_id-employee_id-manager_id' e.g. 'status-1-0-0'
//      All 3 radio buttons have the same name, set value to pending, and id to pending-IDcombo
        pending.setAttribute('type', 'radio')
        pending.setAttribute('name', `status-${reimbursement_employee_manager_id}`)
        pending.setAttribute('value', 'pending')
        pending.setAttribute('id', `pending-${reimbursement_employee_manager_id}`)
//      Label for the pending radio button
        const label_pending = document.createElement('label')
        label_pending.setAttribute('for', `pending-${reimbursement_employee_manager_id}`)
        label_pending.innerText = 'Pending'

//      Create a rejected radio button, name is status-reimbursement_id-employee_id-manager_id' e.g. 'status-1-0-0'
//      All 3 radio buttons have the same name, set value to rejected, and id to rejected-IDcombo
        const rejected = document.createElement('input')
        rejected.setAttribute('type', 'radio')
        rejected.setAttribute('name', `status-${reimbursement_employee_manager_id}`)
        rejected.setAttribute('value', 'rejected')
        rejected.setAttribute('id', `rejected-${reimbursement_employee_manager_id}`)
        const label_rejected = document.createElement('label')
        label_rejected.setAttribute('for', `rejected-${reimbursement_employee_manager_id}`)
        label_rejected.innerText = 'Rejected'

//      Create an accepted radio button, name is status-reimbursement_id-employee_id-manager_id' e.g. 'status-1-0-0'
//      All 3 radio buttons have the same name, set value to accepted, and id to accepted-IDcombo
        const accepted = document.createElement('input')
        accepted.setAttribute('type', 'radio')
        accepted.setAttribute('name', `status-${reimbursement_employee_manager_id}`)
        accepted.setAttribute('value', 'accepted')
        accepted.setAttribute('id', `accepted-${reimbursement_employee_manager_id}`)
        const label_accepted = document.createElement('label')
        label_accepted.setAttribute('for', `accepted-${reimbursement_employee_manager_id}`)
        label_accepted.innerText = 'Accepted'

//      Set default buttons to be checked if the current status matches
        if (td_status.innerText === 'Pending') {
            pending.checked = true
        } else if (td_status.innerText === 'Rejected') {
            rejected.checked = true
        } else if (td_status.innerText === 'Accepted') {
            accepted.checked = true
        }

//      Input text field for the manager message, append to the td for leaving a message
        const td_leave_message = document.createElement('td')
        const input_message = document.createElement('input')
        input_message.setAttribute('type', 'text')
        input_message.setAttribute('name', `manager-message-${reimbursement_employee_manager_id}`)
        input_message.setAttribute('id', `manager-message-${reimbursement_employee_manager_id}`)
        input_message.setAttribute('autofocus', '')
        td_leave_message.appendChild(input_message)

//      Append all the labels, inputs to the td for changing the status
        td_change_status.appendChild(label_pending)
        td_change_status.appendChild(pending)
        td_change_status.appendChild(label_rejected)
        td_change_status.appendChild(rejected)
        td_change_status.appendChild(label_accepted)
        td_change_status.appendChild(accepted)
//      Append the tds to tr, and finally tr to tbody
        tr.appendChild(td_change_status)
        tr.appendChild(td_leave_message)
        tbody.appendChild(tr)
    }
}

//Call this function on load
window.onload = function() {
    this.employee_requests()
}