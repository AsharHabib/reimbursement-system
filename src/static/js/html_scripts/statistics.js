//JS function for loading up the statistics page
async function statistics() {
//  Fetch requests data from the JSON route
    const url = 'http://localhost:5000/requests.json'
    const response = await fetch(url)
    const reimbursements = await response.json()
//  Grab the header tags by ID
    const largest_request = document.getElementById('largest-request')
    const most_requests = document.getElementById('most-requests')
    most_requests.innerHTML = ``
    const total_money_requested = document.getElementById('total-money-requested')
    const mean_request = document.getElementById('mean-request')
//  Declare collections that will be pushed onto
    let amounts = []
    let full_names = []
    const employee_ids = []
    for (let index in reimbursements) {
//  Fill the above collections, full_names is made of first_name + ' ' + last_name
        const amount = reimbursements[index]._amount
        const employee_id = reimbursements[index]._employee_id
        const first_name = reimbursements[index]._first_name
        const last_name = reimbursements[index]._last_name
        amounts.push(amount)
        full_names.push(first_name + ' ' + last_name)
        employee_ids.push(employee_id)
    }
//  Find the highest individual request amount
    max_amount = Math.max.apply(null, amounts)
    index_of_max_amount = amounts.indexOf(max_amount)
    largest_request.innerText = `$${amounts[index_of_max_amount]} made by ${full_names[index_of_max_amount]}`
//  Find the employee with the mode of requests
    var frequency = {}; // array of frequency.
    var maxFreq = 0; // holds the max frequency.
    var modes = [];

    for (var i in full_names) {
      frequency[full_names[i]] = (frequency[full_names[i]] || 0) + 1; // increment frequency.
      if (frequency[full_names[i]] > maxFreq) { // is this frequency > max so far ?
        maxFreq = frequency[full_names[i]]; // update max.
      }
    }
    for (var k in frequency) {
      if (frequency[k] == maxFreq) {
        modes.push(k);
      }
    }
    for (let i = 0; i < modes.length; i++) {
        const mode = modes[i]
        index_of_mode = full_names.indexOf(mode)
        const mode_amount = frequency[full_names[index_of_mode]]
        most_requests.innerHTML += `<p>${full_names[index_of_mode]} with ${mode_amount} requests<br></p>`
    }
//  Total money requested, and mean request amount
    var total = 0;
    for(var i = 0; i < amounts.length; i++) {
        total += amounts[i];
    }
    var avg = total / amounts.length;
    total_money_requested.innerText = `$${total}`
    mean_request.innerText = `$${avg.toFixed(2)}`
}
// Call the above function on window load
window.onload = function() {
    this.statistics()
}