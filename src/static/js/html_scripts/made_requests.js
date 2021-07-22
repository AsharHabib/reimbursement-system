//JS function for loading up the requests page for employees
async function made_requests() {
//  Fetch the JSON url for data on requests, get the <tbody> and <form> tags by ID
    const url = 'http://localhost:5000/requests.json'
    const response = await fetch(url)
    const reimbursements = await response.json()
    const tbody = document.getElementById('made-requests')
    const form = document.getElementById('delete-requests')
//  Pre-define a button so it can be dynamically appended to the form in the for loop
    const delete_button = document.createElement('button')
    delete_button.innerText = 'Delete Request(s)'
    delete_button.setAttribute('type', 'submit')
    delete_button.setAttribute('id', 'delete-button')

//  For loop to iterate over the reimbursements and dynamically make table rows for the <tbody>
    for(let index in reimbursements) {
//      Create the tr tag
        const tr = document.createElement('tr')
        tr.setAttribute('class', 'tr-class')
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
        tr.appendChild(td_status)
//      Create the td tag for the time submitted at, append to tr
        const td_time = document.createElement('td')
        td_time.innerText = `${reimbursements[index]._date_time}`
        tr.appendChild(td_time)
//      Create the td tag for the manager message, append to tr
        const td_message = document.createElement('td')
        td_message.innerText = `${reimbursements[index]._manager_message}`
        tr.appendChild(td_message)
//      Create an input for type checkbox with value reimbursement_id-employee_id ie 1-0
        const delete_box = document.createElement('input')
        delete_box.setAttribute('type', 'checkbox')
        delete_box.setAttribute('name', 'delete-request')
        delete_box.setAttribute('value', `${reimbursements[index]._reimbursement_id}-${reimbursements[index]._employee_id}`)
        delete_box.setAttribute('id', `${reimbursements[index]._reimbursement_id}-${reimbursements[index]._employee_id}`)
//      Event listener for clicking on the checkbox, when it is checked the button is appended to the form dynamically
//      Try catch in case the button is already gone when the user unchecks a box
        delete_box.addEventListener("click", () => {
            try {
                if (delete_box.checked) {
                    form.appendChild(delete_button)
                }
                else {
                    form.removeChild(delete_button)
                }
            } catch (error) {}
        })
//      append the input to tr, and tr to tbody
        tr.setAttribute('id', `row-${index}`)
        tr.appendChild(delete_box)
        tbody.appendChild(tr)
    }

}
// Call the function on window load
window.onload = function() {
    this.made_requests()
}