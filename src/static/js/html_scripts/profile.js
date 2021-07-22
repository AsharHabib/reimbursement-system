//JS function for loading up the profile page
async function profile() {
//  Fetch profile data from the JSON route
    const url = 'http://localhost:5000/profile.json'
    const response = await fetch(url)
    const user_data = await response.json()
//  Find the one h1 tag on the page, set it to be 'Hello first_name last_name'
    let header_one = document.getElementsByTagName('h1')
    header_one = header_one[0]
    header_one.innerHTML = `Hello ${user_data.first_name} ${user_data.last_name}`
//  Grab the ol, create a form and pre-define a button to dynamically append it to the form in the for loop
    const form = document.getElementById('delete-employees')
    let ol = document.getElementsByTagName('ol')
    ol = ol[0]
    const button = document.createElement('button')
    button.setAttribute('type', 'submit')
    button.setAttribute('id', 'delete-employees')
    button.innerText = 'Delete Employee(s)'
//  For loop to iterate over the reimbursements and dynamically make table rows for the <ol>
    for (let index in user_data.employee_ids) {
//      Create the li tag, set it's text to be 'first_name last_name, job_title'
        const li = document.createElement('li')
        li.innerText = `${user_data.employee_first_names[index]} ${user_data.employee_last_names[index]}, ${user_data.job_titles[index]}`
//      Create the checkbox input, value = employee_id
        const delete_box = document.createElement('input')
        delete_box.setAttribute('type', 'checkbox')
        delete_box.setAttribute('name', 'delete-employees')
        delete_box.setAttribute('id', `employee-${user_data.employee_ids[index]}`)
        delete_box.setAttribute('value', `${user_data.employee_ids[index]}`)
//      Event listener for clicking on the checkbox, when it is checked the button is appended to the form dynamically
//      Try catch in case the button is already gone when the user unchecks a box
        delete_box.addEventListener("click", () => {
            try {
                if (delete_box.checked) {
                    form.appendChild(button)
                }
                else {
                    form.removeChild(button)
                }
            } catch (error) {}
        })
//      Append the input to li, and li to ol
        li.appendChild(delete_box)
        ol.append(li)
    }
}
// Call the above function on window load
window.onload = function() {
    this.profile()
}